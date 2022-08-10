#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
import models

if getenv("HBNB_TYPE_STORAGE") == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
            Column('place_id', String(60),
                ForeignKey('places.id'),
                primary_key=True, nullable=False),
            Column('amenity_id', String(60),
                ForeignKey('amenities.id'),
                primary_key=True, nullable=False)
            )

class Place(BaseModel, Base):
    """ A place to stay """
    from models.city import City
    from models.user import User
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey(City.id), nullable=False)
        user_id = Column(String(60), ForeignKey(User.id), nullable=False)
        user = relationship('User', back_populates="places")
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", backref="place")
        amenities = relationship("Amenity", secondary="place_amenity",
                                 backref="place_amenities",viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
        
        @property
        def reviews(self):
            """Get reviews"""
            from models import storage
            arr = []
            for review in storage.all('Review').values():
                if self.id == review.place_id:
                    arr.append(review)
            return arr
        @property
        def amenities(self):
            """Get amenities"""
            return self.__class__.amenity_ids

        @amenities.setter
        def amenities(self, obj):
            if obj.__class__.__name__ == "Amenity":
                self.__class__.amenity_ids.append(obj.id)

    def __init__(self, *args, **kwargs):
        """Initialize model."""
        super().__init__(*args, **kwargs)
