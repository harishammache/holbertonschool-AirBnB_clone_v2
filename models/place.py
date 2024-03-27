#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(Sting(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(Sting(60), ForeignKey('users.id'), nullable=False)
    name = Column(Sting(128), nullable=False)
    description = Column(Sting(1024), nullable=True)
    number_rooms = Column(Integer, Default=0, nullable=False)
    number_bathrooms = Column(Integer, Default=0, nullable=False)
    max_guest = Column(Integer, Default=0, nullable=False)
    price_by_night = Column(Integer, Default=0, nullable=False)
    latitude = Column(Float, Default=0, nullable=False)
    longitude = Column(Float,Default=0, nullable=False)
    amenity_ids = Column(Sting(60), ForeignKey('cities.id'), nullable=False)
