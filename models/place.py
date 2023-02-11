#!/usr/bin/python3

"""
place model
"""
from models.base_model import BaseModel


class Place(BaseModel):
     """ Place class """

     name = ""
     city_id = ""
     user_id = ""
     description = ""
      

     def __init__(self, *args, **kwargs):
         """
              Constructor
         """
         super().__init__(*args, **kwargs)
