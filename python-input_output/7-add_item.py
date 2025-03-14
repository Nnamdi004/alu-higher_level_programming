#!/usr/bin/python3
"""
Script that adds all command-line arguments to a Python list
and saves them to a JSON file.
"""

import sys
from os.path import exists
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"

if exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

items.extend(sys.argv[1:])
save_to_json_file(items, filename)
