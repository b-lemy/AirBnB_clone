#!/usr/bin/python3

"""
City model
"""
from models.base_model import BaseModel


class City(BaseModel):
    """ City class """

    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        """
              Constructor
        """
        super().__init__(*args, **kwargs)
