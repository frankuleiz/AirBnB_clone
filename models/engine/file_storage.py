#!/usr/bin/python3
"""this module is for FileStorage"""
import json
import models
from models.base_model import BaseModel

classes = {"BaseModel": BaseModel}

class FileStorage:
    """class for serializing and desirializing objects to/from JSON"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary of serialized objects"""
        return self.__objects

    def new(self, obj):
        """adds a new object to the dictionary of serialized objects"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes objects and saves them to a JSON file"""
        serial_obj = {}

        for key in self.__objects:
            serial_obj[key] = self.__objects[key].to_dict()

        with open(self.__file_path, 'w') as f:
            json.dump(serial_obj, f)

    def reload(self):
        """deserializes objects from a JSON file
        and loads them into the dictionary"""
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
        except FileNotFoundError:
            pass
