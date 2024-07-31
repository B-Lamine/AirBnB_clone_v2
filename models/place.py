#!/usr/bin/python3
""" Place Module for HBNB project """
from models import hbnb_type_storage
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, String, Integer
from sqlalchemy import Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship

if hbnb_type_storage == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 nullable=False, primary_key=True),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 nullable=False, primary_key=True))


class Place(BaseModel, Base):
    """ A place to stay """
    if hbnb_type_storage == 'db':
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        city = relationship('City', back_populates='places')
        user = relationship('User', back_populates='places')
        amenities = relationship('Amenity', back_populates='place_amenities',
                                 viewonly=False, secondary=place_amenity)
        reviews = relationship('Review', order_by=Review.id,
                               back_populates='place')
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = 0
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
