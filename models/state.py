#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class State(BaseModel, Base):
    """ State class """

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City',
                                cascade='delete', backref='state')
    else:
        name = ""

        @property
        def cities(self):
            my_cities = models.storage.all(City).values()
            return [city for city in my_cities if city.state_id == self.id]
