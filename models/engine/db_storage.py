#!/usr/bin/python3
""" Module to define class to manage database storage.
"""


import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """ database storage management class
    """
    __engine = None
    __session = None

    def __init__(self):
        """ instantiation method.
        """
        hbnb_mysql_user = os.getenv('HBNB_MYSQL_USER')
        hbnb_mysql_pwd = os.getenv('HBNB_MYSQL_PWD')
        hbnb_mysql_host = os.getenv('HBNB_MYSQL_HOST')
        hbnb_mysql_db = os.getenv('HBNB_MYSQL_DB')
        hbnb_env = os.getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                                      .format(hbnb_mysql_user, hbnb_mysql_pwd,
                                              hbnb_mysql_db),
                                      pool_pre_ping=True)
        if hbnb_env == 'test':
            Base.metadata.drop_all(engine)

    def all(self, cls=None):
        """ query all objects of cls, or all classes if cls is None.
        """
        classes = {
                   'User': User, 'Place': Place,
                   'State': State, 'City': City, 'Amenity': Amenity,
                   'Review': Review
                  }
        cls_name = str(cls).split('.')[-1].split("'")[0]
        tmp_dct = {}
        if cls is not None:
            for obj in self.__session.query(cls).all():
                tmp_dct.update({cls_name + '.' + obj.id: obj})
            return tmp_dct
        else:
            for cls_name, cls in classes.items():
                for obj in self.__session.query(cls).all():
                    tmp_dct.update({cls_name + '.' + obj.id: obj})
            return tmp_dct

    def new(self, obj):
        """ add a new record to the open session.
        """
        self.__session.add(obj)

    def save(self):
        """ save all changes to the database.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete object from the session.
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ create all tables.
        """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(Session)
        self.__session = Session

    def close(self):
        """ Close current session.
        """
        self.__session.remove()
