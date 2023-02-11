#!/usr/bin/python3

"""
state model
"""
from models.base_model import BaseModel


class State(BaseModel):
    """ Amenity class """

    name = ""

    def __init__(self, *args, **kwargs):
        """
              Constructor
        """
        super().__init__(*args, **kwargs)
