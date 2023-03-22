#!/usr/bin/python3
'''
Database storage class
'''

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import Base
from models.state import State
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage():
    '''
        Database storage class
    '''

    __engine = None
    __session = None

    def __init__(self):
        '''
            initializes db engine
        '''
        string = 'mysql+mysqldb://{}:{}@{}/{}'
        self.__engine = create_engine(string.format(getenv('HBNB_MYSQL_USER'),
                                                    getenv('HBNB_MYSQL_PWD'),
                                                    getenv('HBNB_MYSQL_HOST'),
                                                    getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') is 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''
            returns all of a class or a specific class
        '''
        if cls is None:
            objects = [obj for my_class in
                       [State, User, City, Place, Amenity, Review]
                       for obj in self.__session.query(my_class).all()]
        else:
            objects = self.__session.query(eval(cls)).all()
        return {'{}.{}'.format(obj.__class__.__name__, obj.id): obj for
                obj in objects}

    def new(self, obj):
        '''
            adds the object to the current database session
        '''
        self.__session.add(obj)

    def save(self):
        '''
            saves & commits all changes of the current database session
        '''
        self.__session.commit()

    def delete(self, obj=None):
        '''
            deletes an object on the current database session
        '''
        if obj is not None:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        '''
            create all tables in the database
        '''
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

    def close(self):
        '''
            calls remove() method
        '''
        self.__session.close()
