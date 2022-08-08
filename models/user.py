#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """ User class """

    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "users"
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        password = Column(String(128), nullable=False)
        places = relationship("Place", backref="user", cascade="delete")
        email = Column(String(128), nullable=False)
        reviews = relationship("Review", backref="user", cascade="delete")
    else:
        first_name = ""
        last_name = ""
        email = ""

    def __init__(self, *args, **kwargs):
        """Initialize model."""
        super().__init__(*args, **kwargs)
