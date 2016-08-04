#!/usr/bin/env python3

import argparse
import os.path
import os
import zipfile
import sys
import glob

import rarfile

def get_output_name(path):
    """Given some path of form /my/dir/myfile.ext, return myfile.cbz

    Arguments:
        path - the input path which points to a specific file

    Return:
        A filename ending in .cbz
    """

    if not path:
        return "comic.cbz"
    name = path.split("/")[-1]
    if name.find(".cbr"):
        return name.replace(".cbr", ".cbz")
    else:
        return name + ".cbz"

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
    args["target"] = os.path.join(os.getcwd(), args["target"], args["source"].split("/")[-1].replace(".cbr", ".cbz"))
if os.path.isdir(args["source"]):
    comics = glob.glob(os.path.join(os.getcwd(), args["source"], "*.cbr"))
    for comic in comics:
        comic_path = os.path.join(args["source"], comic)
        comic_name = get_output_name(comic)
        comic_output = os.path.join(args["target"], comic_name)
        convert_file(comic_path, comic_output)
else:
    convert_file(args["source"], args["target"])
quit()
