VERSION = $(subst v,,$(shell git describe --tags))

all: README.rst


README.rst: README.md
	pandoc -f markdown -t rst -o $@ $<


upload: all
	python setup.py bdist upload
	python setup.py sdist upload

.PHONY: all upload
