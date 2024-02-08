#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class FileStorage:
    """Represents a storage engine for serializing and deserializing objects.

    Attributes:
        _file_path (str): The path to the JSON file for saving objects.
        _objects (dict): A dictionary to store objects.
    """
    _file_path = "file.json"
    _objects = {}

    def all_objects(self):
        """Returns the dictionary of stored objects."""
        return FileStorage._objects

    def add_object(self, obj):
        """Adds an object to the storage."""
        class_name = obj.__class__.__name__
        FileStorage._objects["{}.{}".format(class_name, obj.id)] = obj

    def save_objects(self):
        """Serializes objects to the JSON file."""
        objects_dict = {key: obj.to_dict() for key, obj in FileStorage._objects.items()}
        with open(FileStorage._file_path, "w") as file:
            json.dump(objects_dict, file)

    def load_objects(self):
        """Deserializes the JSON file to objects."""
        try:
            with open(FileStorage._file_path) as file:
                objects_dict = json.load(file)
                for obj_data in objects_dict.values():
                    class_name = obj_data["__class__"]
                    del obj_data["__class__"]
                    obj = eval(class_name)(**obj_data)
                    self.add_object(obj)
        except FileNotFoundError:
            pass

