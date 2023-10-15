#!/usr/bin/python3
"""defines the class City module"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Representation of city user
    It inherits from the BaseClass
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes the class instance"""
        super().__init__(*args, **kwargs)
