#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Copyright 2011 by Matteo Bertini <matteo@naufraghi.net>

import os
import sys
import argparse
import logging
import subprocess
from contextlib import contextmanager
from functools import wraps

os.environ["LANG"] = "C"

logging.basicConfig(format='%(asctime)s %(levelname)s[%(name)s]: %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger("git-svn-clone-externals")

class col:
    PINK = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'

@contextmanager
def cd(path):
    cur_dir = os.getcwd()
    os.chdir(path)
    yield
    os.chdir(cur_dir)

def logged_call(func, log=logger.debug):
    @wraps(func)
    def _logged(args, **kwargs):
        color = col.BLUE
        if log is logger.info:
            color = col.GREEN
        elif log is logger.warning:
            color = col.YELLOW
        elif log is logger.error:
            color = col.RED
        end_color = col.ENDC
        cwd = os.getcwd()
        command = " ".join(args)
        log("{cwd}$ {color}{command}{end_color}".format(**locals()))
        res = func(args, **kwargs)
        if res and func is subprocess.call:
            color = col.RED
            logger.error("{cwd}$ {color}{command}{end_color}".format(**locals()))
        return res
    return _logged

def svn_info():
    info = logged_call(subprocess.check_output)(["svn", "info"])
    info_dict = {}
    for line in info.split("\n"):
        if ":" in line:
            key, value = line.split(":", 1)
            info_dict[key.strip()] = value.strip()
    return info_dict

def svn_externals():
    externals = logged_call(subprocess.check_output)(["svn", "st"])
    seen = set()
    for line in externals.split("\n"):
        if line.strip() and line.startswith("X"):
            path = line.split()[1].strip()
            root = os.path.dirname(path)
            if root not in seen:
                seen.add(root)
            else:
                continue
            props = logged_call(subprocess.check_output)(["svn", "propget", "svn:externals", root])
            for prop in props.split("\n"):
                if prop.strip():
                    yield root, prop.strip()

def extpath_join(root, uri):
    if uri.startswith("^"):
        return root + uri[1:]
    else:
        raise NotImplementedError

def normalize_externals(repo_root, externals):
    # Old syntax: third-party/sounds   http://svn.example.com/repos/sounds [UNSUPPORTED]
    # New syntax: -r148 ^/skinproj third-party/skins
    # peg syntax: ^/skinproj@148 third-party/skins
    for root, external in externals:
        parts = external.split()
        if len(parts) == 2:
            rev = None
            uri, path = parts
            if "@" in uri:
                uri, rev = uri.split("@")
        elif len(parts) == 3:
            rev, uri, path = parts()
            rev = rev.strip("-r")
        yield rev, extpath_join(repo_root, uri), os.path.normpath(os.path.join(root, path))

def check_svn(path):
    try:
        out = logged_call(subprocess.check_output)(["svn", "info", path])
    except subprocess.CalledProcessError:
        raise argparse.ArgumentError("Invalid svn working copy!\nsvn info {0} returned:\n\n{1}".format(path, out))
    return path

def run():
    parser = argparse.ArgumentParser(description="git svn clone and follow svn:externals")
    parser.add_argument("working_copy", help="Point to an existing svn checkout", type=check_svn)
    parser.add_argument("destination", help="Destination folder")

    parser.add_argument("-v", "--verbosity", action='count', default=0)
    parser.add_argument("-q", "--quiet", action='count', default=0)

    args, other_args = parser.parse_known_args()
    logger.setLevel(max(1, logging.INFO-10*(args.verbosity - args.quiet)))

    externals = []
    with cd(args.working_copy):
        repo_info = svn_info()
        repo_root = repo_info["Repository Root"]
        for rev, uri, path in normalize_externals(repo_root, svn_externals()):
            externals += [(rev, uri, path)]

    repo_url = repo_info["URL"]
    commands = ["git", "svn", "clone"]
    commands += other_args
    commands += [repo_url, args.destination]
    logged_call(subprocess.call, logger.info)(commands)
    with cd(args.destination):
        for rev, uri, path in externals:
            commands = ["git", "svn", "clone"]
            commands += other_args
            commands += [uri, path]
            logged_call(subprocess.call, logger.info)(commands)
            if not [x for x in os.listdir(path) if x != ".git"]:
                logger.warning("{0}Foder {path} is empty after clone!{1}".format(col.YELLOW, col.ENDC, **locals()))

if __name__ == "__main__":
    run()
