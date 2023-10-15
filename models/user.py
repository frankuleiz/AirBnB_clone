#!/usr/bin/python3
"""defines the class user module"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Representation of class user 
    It inherits from the BaseClass
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initializes the class instance"""
        super().__init__(*args, **kwargs)
