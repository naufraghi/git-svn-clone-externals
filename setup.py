from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='git-svn-clone-externals',
    version='1.1.1',
    description='Clone an svn checkout in a tree of nested git-svn repos and helper tools',
    long_description=long_description,
    url='https://github.com/naufraghi/git-svn-clone-externals',
    author='Matteo Bertini',
    author_email='matteo@naufraghi.net',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Developers',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Version Control',
        'Topic :: Utilities'
    ],
    keywords='svn git git-svn externals',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=[],
    py_modules=["git_svn_clone_externals"],
    entry_points={
        'console_scripts': [
            'git-svn-clone-externals=git_svn_clone_externals:run',
            'git-svn-dcommit=git_svn_clone_externals:run_dcommit',
            'git-svn-rebase=git_svn_clone_externals:run_rebase',
            'git-svn-outgoing=git_svn_clone_externals:run_outgoing',
        ],
    },
)
