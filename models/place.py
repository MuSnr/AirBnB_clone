#!/usr/bin/python3
"""Defines the Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represents a place.

    Attributes:
        place_city_id (str): The City id.
        place_user_id (str): The User id.
        place_name (str): The name of the place.
        place_description (str): The description of the place.
        place_number_rooms (int): The number of rooms of the place.
        place_number_bathrooms (int): The number of bathrooms of the place.
        place_max_guest (int): The maximum number of guests of the place.
        place_price_by_night (int): The price by night of the place.
        place_latitude (float): The latitude of the place.
        place_longitude (float): The longitude of the place.
        place_amenity_ids (list): A list of Amenity ids.
    """

    place_city_id = ""
    place_user_id = ""
    place_name = ""
    place_description = ""
    place_number_rooms = 0
    place_number_bathrooms = 0
    place_max_guest = 0
    place_price_by_night = 0
    place_latitude = 0.0
    place_longitude = 0.0
    place_amenity_ids = []

