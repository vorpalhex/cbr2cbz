#!/usr/bin/env python3

import argparse
import os.path
import zipfile
import sys

import rarfile

def convert_file(cbr, output):
    """Given a string pointing to a cbr file, output a cbz file to output

    Arguments:
        cbr - a string containing the path to a particular cbr file
        output - a string containing the desired output path to write the cbz to

    Return:
        Boolean value indicating success or failure
    """

    with zipfile.ZipFile(output, mode="w") as cbz:
        with rarfile.RarFile(cbr) as rf:
            for entry in rf.infolist():
                cbz.writestr(entry.filename, rf.read(entry), compress_type=zipfile.ZIP_DEFLATED)

    return True


parser = argparse.ArgumentParser(prog="cbr2cbz", description="A posix friendly"
" utility to convert cbr archives to cbz");

parser.add_argument("source", nargs="?", default=".", help="Either a cbr file or a directory"
" containing cbr files")

parser.add_argument("target", nargs="?", default=".", help="Output path, optionally specifying a name."
"specifying a name when converting multiple will concatenate all input "
"into a single output")

args = vars(parser.parse_args());
if os.path.isdir(args["target"]):
    args["target"] = os.path.join(args["target"], args["source"].split("/")[-1].replace(".cbr", ".cbz"))
if os.path.isdir(args["source"]):
    quit()
else:
    convert_file(args["source"], args["target"])
quit()
