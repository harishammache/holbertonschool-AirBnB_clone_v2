#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
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
