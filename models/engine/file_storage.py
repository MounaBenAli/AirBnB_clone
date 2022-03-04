#!/usr/bin/python3
"""FILE STORAGE"""
import json
from models.base_model import BaseModel


class FileStorage:
    """File Ftorage Class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets __objects"""
        if obj:
            self.__objects["{}.{}".format(obj.__class__.__name__,
                                          obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file        """
        my_dic = {}
        for key, value in self.__objects.items():
            my_dic[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="UTF-8") as f:
            json.dump(my_dic, f)

    def reload(self):
        """deserializes the JSON file to __objects """
        try:
            with open(self.__file_path, "r", encoding="UTF-8") as f:
                obj = json.load(f)
            for key, value in obj.items():
                class_name = key.split('.')[0]
                self.__objects[key] = eval(class_name)(**value)
        except BaseException:
            pass
