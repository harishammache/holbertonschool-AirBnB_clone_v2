#!/usr/bin/python3
""" This module defines the class User """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Represents an user for a MySQL database.

    Public class attributes (with sqlalchemy):

        __tablename__ (str): Name of MySQL table to store users.

        email: (Columns: String): User's email address.
        password (Columns: String): User's password.
        first_name (Columns: String): User's first name.
        last_name (Columns: String): User's last name.

        places (Relationship User --> Place): Links user with places.
        reviews (Relationship User --> Review): Links user with reviews.
    """
    __tablename__ = "users"

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))

    places = relationship("Place", backref="user",
                          cascade="all, delete", passive_deletes=True)
    reviews = relationship("Review", backref="user",
                           cascade="all, delete", passive_deletes=True)
