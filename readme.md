# cbr2cbz

While most comic book readers these days support the cbr format, there are a few that don't. In addition, the cbr format isn't as free (as in speech) as one might like. This is a handy utility to convert cbr files to cbz, keeping the contents intact. Standard zip compression is used, so the output size may exceed the original input.

## Requirements

You'll need to have an 'unrar' implementation installed and accessible. On OS X with brew this is as simple as `brew install unrar`. On most Linuxes, you'll want to install __unrar__ proper (sometimes called _unrar-notfree_), [but please avoid _unrar-free_](https://github.com/markokr/rarfile/issues/10).

To run from source, you'll need `rarfile`.

To build from source, you'll need `cx_Freeze`.

## Usage

Basic Usage is as simple as

`cbr2cbz ~/comics/some-comic.cbr`

which will drop `some-comic.cbz` in your current directory. Optionally you can specify an output directory by:

`cbr2cbz ~/comics/some-comic.cbr ~/my_converted_comics/`

The program will gladly handle a directory of comics too, if you'd like:

`cbr2cbz ~/comics`

though by default it'll only convert files actually ending in .cbr.

## Building From Source

Building is done via `cx_Freeze`, just run:

`python setup.py cx_Freeze`

A platform compatible executable should appear in the _build_ directory.
