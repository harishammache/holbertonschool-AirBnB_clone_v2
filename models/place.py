#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
import sqlalchemy
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from models.city import City
from models.review import Review


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, Default=0, nullable=False)
    number_bathrooms = Column(Integer, Default=0, nullable=False)
    max_guest = Column(Integer, Default=0, nullable=False)
    price_by_night = Column(Integer, Default=0, nullable=False)
    latitude = Column(Float, Default=0, nullable=False)
    longitude = Column(Float,Default=0, nullable=False)
    amenity_ids = Column(String(60), ForeignKey('cities.id'), nullable=False)
    reviews = relationship("Review", backref="place", cascade="all, delete")

    @property
    def reviews(self):
        """Getter attribute that returns the list of Review instances"""
        from models import storage
        reviews_list = []
        for review in storage.all(Review).values():
            if review.place_id == self.id:
                reviews_list.append(review)
        return reviews_list