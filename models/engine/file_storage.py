#!/usr/bin/python3
"""
file storage module
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """
    file storage class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects of the file
        """
        return self.__objects

    def new(self, obj):
        """
         sets in __objects the obj with key <obj class name>.id
        """
        if obj:
            self.__objects["{}.{}".format(obj.__class__.__name__,
                                          obj.id)] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        new_dict = {}
        for k, v in self.__objects.items():
            new_dict[k] = v.to_dict()
        with open(self.__file_path, "w", encoding="UTF-8") as f:
            json.dump(new_dict, f)

    def reload(self):
        """
        deserializes the JSON file to __objects from the file
        """
        try:
            with open(self.__file_path, "r", encoding="UTF-8") as f:
                obj = json.load(f)
            for k, v in obj.items():
                class_name = k.split('.')[0]
                self.__objects[k] = eval(class_name)(**v)
        except BaseException:
            pass
