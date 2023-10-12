#!/usr/bin/python3

import models
import uuid
from datetime import datetime

time = "%Y-%m-%dT%H:%M:%S.%f"
class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        self.updated_at = datetime.now

    def to_dict(self):
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = new_dict["created_at"].strftime(time)
        new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        return new_dict

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)
