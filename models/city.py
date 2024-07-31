#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from models import hbnb_type_storage
#from models.state import State
from models.place import Place
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
    if hbnb_type_storage == 'db':
        state = relationship('State', back_populates='cities')
    places = relationship('Place', order_by=Place.id, back_populates='city')


#State.cities = relationship('City', order_by=City.id, back_populates='state')
#City.places = relationship('Place', order_by=Place.id, back_populates='city')
