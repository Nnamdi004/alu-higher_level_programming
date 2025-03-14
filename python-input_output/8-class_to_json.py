#!/usr/bin/python3
"""
Module for converting a class instance to a dictionary for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns the dictionary description for JSON serialization of an object.

    Args:
        obj (object): An instance of a class.

    Returns:
        dict: A dictionary representation of the object's attributes.
    """
    return obj.__dict__
