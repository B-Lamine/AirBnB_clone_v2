#!/usr/bin/python3
""" State Module for HBNB project """
from models import hbnb_type_storage
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """ Amenities class.
    """
    if hbnb_type_storage == 'db':
        from models.place import place_amenity
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        place_amenities = relationship('Place', back_populates='amenities',
                                       viewonly=False, secondary=place_amenity)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """ Instantiation"""
        super().__init__(*args, **kwargs)

