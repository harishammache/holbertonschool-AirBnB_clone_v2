#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
import sqlalchemy
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from models.city import City
from models.review import Review
from models.amenity import Amenity


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
    longitude = Column(Float, Default=0, nullable=False)
    amenity_ids = Column(String(60), ForeignKey('cities.id'), nullable=False)
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True, nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True, nullable=False))
    reviews = relationship("Review", backref="place", cascade="all, delete")
    amenities = relationship("Amenity", secondary=place_amenity,
                             viewonly=False)

    @property
    def reviews(self):
        """Getter attribute that returns the list of Review instances"""
        from models import storage
        reviews_list = []
        for review in storage.all(Review).values():
            if review.place_id == self.id:
                reviews_list.append(review)
        return reviews_list

    @property
    def amenities(self):
        """Getter attribute that returns the list of Amenity"""
        return [amenity_id for amenity_id in self.amenity_ids]

    @amenities.setter
    def amenities(self, amenity):
        """Setter attribute that handles append method"""
        if isinstance(amenity, Amenity):
            self.amenity_ids.append(amenity.id)
