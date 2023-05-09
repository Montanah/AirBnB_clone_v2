#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from os import getenv


class Review(BaseModel, Base):
    """ Review classto store review information """

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'reviews'
        user_id = Column(String(60),
                         ForeignKey('users.id', ondelete='cascade'),
                         nullable=False)
        place_id = Column(String(60),
                          ForeignKey('places.id', ondelete='cascade'),
                          nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
