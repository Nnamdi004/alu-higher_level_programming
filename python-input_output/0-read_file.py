#!/usr/bin/python3
"""
Module for reading and printing the contents of a UTF-8 encoded text file.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its content to stdout.

    Args:
        filename (str): The name of the file to read.
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
