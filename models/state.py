#!/usr/bin/python3
""" State Module for HBNB project """
from models import hbnb_type_storage, storage
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if hbnb_type_storage == 'db':
        cities = relationship('City', order_by=City.id, back_populates='state')
    else:
        @property
        def cities(self):
            """ Get list of cities in given state.
            """
            current_stateId = self.id
            tmp = storage.all(City)
            cities_list = []
            for k, v in tmp.items():
                if v.state_id == current_stateId:
                    cities_list.append(v)
            return cities_list
