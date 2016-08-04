import sys
from cx_Freeze import setup, Executable


setup(
    name="cbr2cbz",
    version="1.0",


    author="Derrick Hinkle",
    description="A utility for converting CBR files to CBZ",
    url="https://github.com/dark12222000/cbr2cbz",

    executables=[Executable("cbr2cbz/main.py")]
)
