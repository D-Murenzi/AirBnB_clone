#!/usr/bin/python3
"""Defines the base class that all the object inherit from."""
import uuid
import datetime as a


class BaseModel():
    """define the common attributes and methods for other classes."""
    def __init__(self):
        self.id = str(uuid.uuid4())
        b = a.datetime.now()
        self.created_at = b
        self.updated_at = b

    def __str__(self):
        return "[{:s}] ({:s}) {:}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        c = a.datetime.now()
        self.updated_at = c

    def to_dict(self):
        created = self.created_at.isoformat()
        updated = self.updated_at.isoformat()
        in_dict = self.__dict__.copy()
        in_dict['__class__'] = self.__class__.__name__
        in_dict['created_at'] = created
        in_dict['updated_at'] = updated
        return in_dict
