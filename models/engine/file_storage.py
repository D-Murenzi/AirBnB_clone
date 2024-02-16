"""This module is a file that stores other objects."""
import json
import os


class FileStorage():
    """Serialize instances to a JSON and deserialize JSON to instances."""

    __file_path = "file.json"
    __objects = {}

    @property
    def objects(self):
        """Return the object dictionary."""
        return FileStorage.__objects.copy()

    @objects.setter
    def objects(self, newdict):
        """Set new value to the objects dictionary."""
        FileStorage.__objects = newdict

    def all(self):
        """Return dictionary of an instance attributes."""
        return FileStorage.__objects.copy()

    def new(self, obj):
        """Set new object in object dictionary."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        new_dict = FileStorage.__objects.copy()
        new_dict[key] = obj
        FileStorage.__objects = new_dict

    def save(self):
        """Serialize __objects dictionary to JSON file."""
        with open(str(self.__class__.__file_path), mode='w') as file:
            json_to_dict = {}
            for key, value in self.__class__.__objects.copy().items():
                json_to_dict[key] = value.to_dict()
            json.dump(json_to_dict, file)

    def reload(self):
        """Deserialize the JSON file to _objects."""
        if self.__class__.__file_path is not None:
            if os.path.exists(self.__class__.__file_path):
                with open(self.__class__.__file_path, mode='r') as file:
                    temp_dict = json.load(file)
                from_json = {}
                from .. import base_model
                for key, value in temp_dict.items():
                    from_json[key] = base_model.BaseModel(value)
                FileStorage.__objects = from_json
