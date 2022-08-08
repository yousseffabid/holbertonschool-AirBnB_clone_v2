#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""

from json import dumps, loads
from os.path import exists
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is not None:
            cls_obj = {}

            for k, v in self.__objects.items():
                if type(v) == cls:
                    cls_obj[k] = v
            return cls_obj
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            my_json = dict()
            for key, value in self.__objects.items():
                my_json[key] = value.to_dict()
            with open(self.__file_path, mode='w', encoding='utf-8') as my_file:
                my_file.write(dumps(my_json))
    
    def reload(self):
        """Loads storage dictionary from file"""
        if exists(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as my_file:
                my_json = loads(my_file.read())
                for key, value in my_json.items():
                    self.__objects[key] = eval(value['__class__'])(**value)

    def delete(self, obj=None):
        """delete obj from __objects"""
        if obj is not None:
            try:
                del self.__objects[f"{type(obj).__name__}.{obj.id}"]
                self.save()
            except (AttributeError, KeyError):
                pass
