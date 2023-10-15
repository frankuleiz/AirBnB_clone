#!/usr/bin/python3
"""defines the class review module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Representation of class Review
    It inherits from the BaseClass
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initializes the class instance"""
        super().__init__(*args, **kwargs)
