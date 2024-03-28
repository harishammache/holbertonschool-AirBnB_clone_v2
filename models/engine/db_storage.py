#!/usr/bin/python3
"""New engine DBStorage"""
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User
from os import getenv
import os


class DBStorage:
    """Database Storage Manager"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializing the Database Storage Manager"""
        mysql_env = getenv("HBNB_ENV", "none")
        mysql_user = getenv("HBNB_MYSQL_USER")
        mysql_passwd = getenv("HBNB_MYSQL_PWD")
        mysql_host = getenv("HBNB_MYSQL_HOST")
        mysql_data = getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine(
            f'mysql+mysqldb://\
            {mysql_user}:{mysql_passwd}@{mysql_host}/{mysql_data}',
            pool_pre_ping=True
            )

        if mysql_env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects from the database session."""
        all_classes = [User, State, City, Amenity, Place, Review]
        objects = {}

        if cls is None:
            for obj_class in all_classes:
                for obj in self.__session.query(obj_class).all():
                    objects[f"{obj_class.__name__}.{obj.id}"] = obj

        else:
            for obj in self.__session.query(cls).all():
                objects[f"{cls.__name__}.{obj.id}"] = obj

        return objects

    def new(self, obj):
        """Add the object to the current database session."""
        self.__session.add(obj)

    def save(self):
        """changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """Closes the session"""
        self.__session.close()
