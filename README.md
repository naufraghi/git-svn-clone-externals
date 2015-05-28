Clone an svn repo with externals
================================

[![Join the chat at https://gitter.im/naufraghi/git-svn-clone-externals](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/naufraghi/git-svn-clone-externals?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Usage
-----

`git-svn-clone-externals svn-working-copy dest-dir`

The main difference between this and other alternative scripts is that this
one starts from an svn checkout to discover the externals.

Depends
-------

`sudo apt-get install git-svn`


TODO
----

* git-ignore externals
* test on convoluted externals (relative paths)
* manage fixed revision externals
