#!/usr/bin/python3
"""defines the Amenity user module"""
from models.base_model import BaseModeli


class Amenity(BaseModel):
    """
    Representation of amenity
    It inherits from the BaseClass
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes the class instance"""
        super().__init__(*args, **kwargs)
