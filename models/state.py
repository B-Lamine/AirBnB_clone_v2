#!/usr/bin/python3
""" State Module for HBNB project """
from models import hbnb_type_storage
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    if hbnb_type_storage == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', order_by=City.id, back_populates='state')
    else:
        name = ""

        @property
        def cities(self):
            """ Get list of cities in given state.
            """
            from models import storage
            current_stateId = self.id
            tmp = storage.all(City)
            cities_list = []
            for k, v in tmp.items():
                if v.state_id == current_stateId:
                    cities_list.append(v)
            return cities_list
    
    def __init__(self, *args, **kwargs):
        """ Instantiation"""
        super().__init__(*args, **kwargs)
