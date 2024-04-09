#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """
        Initialize a new BaseModel instance.

        Args:
            *args: Variable length argument list - not used here,
            but allows flexibility for future enhancements.
            **kwargs: Arbitrary keyword arguments.
            Contains attributes and their values as key-value pairs.

        If 'kwargs' is provided and contains key-value pairs,
        each key-value pair is used to set attributes on the instance.
        Specifically, if 'created_at' or 'updated_at' keys are present,
        their string values are converted to datetime objects.
        If 'kwargs' does not contain 'id', 'created_at', or 'updated_at',
        these attributes are initialized with default values:
        a new UUID string for 'id', and the current
        datetime for 'created_at' and 'updated_at'.

        If 'kwargs' is not provided or is empty, 'id', 'created_at',
        and 'updated_at' are set to their
        default values immediately.
        his ensures that every instance has a unique identifier and timestamps
        that reflect when the instance was created and last updated.
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.utcnow()
        else:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)

            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.utcnow()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.utcnow()

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def delete(self):
        """
        Delete the current instance from the storage.

        This method calls the delete method of the storage object, effectively
        removing the instance from the storage. For DBStorage, it translates to
        removing the instance from the database session
        and committing the change,
        while for FileStorage, it means removing
        the instance from the file system
        where instances are serialized and saved.
        """
        from models import storage
        storage.delete(self)

    def to_dict(self):
        """
        Convert instance into a dictionary format.

        Returns:
            dict: A dictionary representation of the instance,
            which includes all
            attributes of the instance.
            This method also adds a class name to the dictionary.
            If '_sa_instance_state' is present in the dictionary,
            it is removed to avoid
            including SQLAlchemy-specific internal
            information in the returned dictionary.
        """
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = dictionary['created_at'].isoformat()
        dictionary['updated_at'] = dictionary['updated_at'].isoformat()
        dictionary.pop('_sa_instance_state', None)

        return dictionary
