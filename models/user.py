#!/usr/bin/python3
"""This module defines a class User"""
from models import hbnb_type_storage
from models.base_model import BaseModel, Base
from models.place import Place
from models.review import Review
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    if hbnb_type_storage == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        places = relationship('Place', order_by=Place.id,
                              back_populates='user')
        reviews = relationship('Review', order_by=Review.id,
                               back_populates='user')
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """ Instantiation"""
        super().__init__(*args, **kwargs)
