#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel
from models.base_model import Base
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """inheritated class State from BaseModel"""
    __tablename__ = "state"
    name = Column(String(128), nullable=False)

    citie = relationship("City", backref="state", cascade="all, delete")

    @property
    def cities(self):
        from models import storage
        city_instances = storage.all(City)

        for city in city_instances.values():
            if city.state_id == self.id:
                return city
