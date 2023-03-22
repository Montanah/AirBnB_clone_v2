#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
import models
from sqlalchemy import Column, Integer, String, DateTime, inspect
from sqlalchemy.ext.declarative import declarative_base
from os import getenv


if getenv('HBNB_TYPE_STORAGE') == 'db':
    Base = declarative_base()
else:
    class Base:
        pass


class BaseModel:
    """A base class for all hbnb models"""

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        id = Column(String(60), unique=True, nullable=False, primary_key=True)
        created_at = Column(DateTime, nullable=False,
                            default=datetime.utcnow())
        updated_at = Column(DateTime, nullable=False,
                            default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if id not in kwargs:
            self.id = str(uuid.uuid4())
        if 'created_at' not in kwargs:
            self.created_at = datetime.now()
        else:
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
        if 'updated_at' not in kwargs:
            self.updated_at = datetime.now()
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
        for key, val in kwargs.items():
            if "__class__" not in key:
                setattr(self, key, val)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        models.storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def delete(self):
        """delete the current instance from the storage"""
        models.storage.delete(self)
