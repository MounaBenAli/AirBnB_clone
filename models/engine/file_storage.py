#!/usr/bin/python3
"""FileStorage Class Module."""

import json
from os.path import exists


class FileStorage():
    """FileStorage - serializes instances toa JSON file
    and deserializes JSON file to instances"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects = obj

    def save(self):
        """serializes __objects to the JSON file """
        filename = self.__file_path
        obj = self.__objects
        with open(filename, "w") as f:
            json_rep = json.dumps(obj)
            f.write(json_rep)

    def reload(self):
        """deserializes __objects to the JSON file and checks if file exits """
        filename = self.__file_path
        obj = self.__objects

        if exists(filename):
            with open(filename, "r") as f:
                return json.loads(f.read())






