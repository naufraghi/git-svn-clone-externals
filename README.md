Clone an svn repo with externals
================================

[![Join the chat at https://gitter.im/naufraghi/git-svn-clone-externals](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/naufraghi/git-svn-clone-externals?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![PyPI version](https://img.shields.io/pypi/v/git-svn-clone-externals.svg)](https://pypi.python.org/pypi/git-svn-clone-externals)
[![PyPI downloads](https://img.shields.io/pypi/dm/git-svn-clone-externals.svg)](https://pypi.python.org/pypi/git-svn-clone-externals#downloads)
[![GitHub license](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/naufraghi/git-svn-clone-externals)

Usage
-----

`git-svn-clone-externals svn-working-copy dest-dir`

The main difference between this and other alternative scripts is that this
one starts from an svn checkout to discover the externals.

Installation
------------

The scritps depends on `git svn`, in Ubuntu you can get the package with:

`$ sudo apt-get install git-svn`

and than instal the script with:

`$ pip install git-svn-clone-externals`


License
-------

This script is released under the [MIT License](http://naufraghi.mit-license.org)

TODO
----

* git-ignore externals
* test on convoluted externals (relative paths)
* manage fixed revision externals
