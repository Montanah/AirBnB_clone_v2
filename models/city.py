#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60),
                          ForeignKey('states.id', ondelete='cascade'),
                          nullable=False)
        places = relationship('Place',
                              cascade='delete', backref='cities')
    else:
        state_id = ""
        name = ""
