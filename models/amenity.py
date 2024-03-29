#!/usr/bin/python3
"""Contains the Amenity class(custom)."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents an amenity.

    Attributes:
        amenity_name (str): The name of the amenity.
    """

    name = ""

