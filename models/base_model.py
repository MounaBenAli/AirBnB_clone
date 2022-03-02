#!/usr/bin/python3
"""BaseModel Class Module."""


import uuid
from datetime import datetime
import models


class BaseModel():
    """BaseModel - defines all common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """__init__ - intantiates attributes"""
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
        else:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    setattr(
                        self, key, datetime.strptime(
                            value, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, key, value)

    def __str__(self):
        """Return the str() representation of the BaseModel instance."""
        return (
            "[{}] ({}) {}".format(
                type(self).__name__,
                self.id,
                self.__dict__))

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary with a new key __class__"""
        new_dict = self.__dict__.copy()
        new_dict['__class__ '] = type(self).__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
