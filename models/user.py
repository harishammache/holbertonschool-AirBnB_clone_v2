#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class User(BaseModel):
    """update user inherits for BaseModel"""
    __tablename__ = "users"

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        """inherits for basemodel"""
        super().__init__(*args, **kwargs)