#!/usr/bin/python3
"""Contains the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review.

    Attributes:
        review_place_id (str): The Place id.
        review_user_id (str): The User id.
        review_text (str): The text of the review.
    """

    review_place_id = ""
    review_user_id = ""
    review_text = ""

