#!/usr/bin/python3
"""Defines the Review class."""

from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a Review.
    Attributes:
        place_id (str): It will be the Place.id.
        user_id (str): It will be the User.id.
        text (str): The text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""