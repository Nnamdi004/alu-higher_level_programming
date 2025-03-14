#!/usr/bin/python3
"""
Module defining a Student class with selective JSON serialization and data reloading.
"""

class Student:
    """
    A class representing a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): A list of attribute names to retrieve.
        
        Returns:
            dict: A dictionary containing the specified attributes, or all attributes if attrs is None.
        """
        if attrs is None:
            return self.__dict__
        return {k: v for k, v in self.__dict__.items() if k in attrs}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance using a JSON dictionary.

        Args:
            json (dict): A dictionary containing attribute names and their new values.
        """
        for key, value in json.items():
            setattr(self, key, value)
