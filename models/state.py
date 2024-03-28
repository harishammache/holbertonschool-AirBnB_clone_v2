#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel):
    """inheritated class State from BaseModel"""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")

    @property
    def cities(self):
        """Getter attribute for cities"""
        from models import storage
        city_instances = storage.all("City")

        cities_list = []
        for city in city_instances.values():
            if city.state_id == self.id:
                cities_list.append(city)

        return cities_list
