#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.place import place_amenity, Place
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """ Amenities class.
    """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship('Place', back_populates='amenities',
                                   viewonly=False, secondary=place_amenity)


#Amenity.places = relationship('Place', order_by=Place.id,
#                              back_populates='amenities',
#                              viewonly=False, secondary=place_amenity)
