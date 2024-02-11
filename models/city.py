#!/usr/bin/python3
"""Contains the City class(Custom)."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents a city.

    Attributes:
        city_state_id (str): The state id.
        city_name (str): The name of the city.
    """

    state_id = ""
    name = ""

