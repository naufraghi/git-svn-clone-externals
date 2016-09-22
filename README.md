Clone an svn repo with externals
================================

[![PyPI version](https://img.shields.io/pypi/v/git-svn-clone-externals.svg)](https://pypi.python.org/pypi/git-svn-clone-externals)
[![PyPI downloads](https://img.shields.io/pypi/dm/git-svn-clone-externals.svg)](https://pypi.python.org/pypi/git-svn-clone-externals#downloads)
[![GitHub license](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/naufraghi/git-svn-clone-externals)

Usage
-----

`git-svn-clone-externals svn-working-copy dest-dir`

The main difference between this and other alternative scripts is that this
one starts from an svn checkout to discover the externals, so it's faster.

The package comes with some utility command to manage a nested `git-svn` clone:

- `git-svn-dcommit` and `git-svn-rebase`: as `git svn <command>` but with automatic `stash save` and `stash pop`
- `git-svn-outgoing`: shows a diff of dcommit'able commits

All scripts are offering a `--recursive` option.

Installation
------------

The scritps depends on `git svn`, in Ubuntu you can get the package with:

`$ sudo apt-get install git-svn`

and than install the script with:

`$ pip install git-svn-clone-externals`


License
-------

This script is released under the [MIT License](http://naufraghi.mit-license.org)

TODO
----

* git-ignore externals
* test on convoluted externals (relative paths)
* manage fixed revision externals
