#!/usr/bin/python3
"""This module defines a class User"""
import models
from models.base_model import BaseModel
from models.base_model import Base
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """update user inherits for BaseModel"""
    __tablename__ = "users"

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    places = relationship("Place", backref="user", cascade="delete")
    reviews = relationship("Review", backref="user", cascade="delete")