#!/usr/bin/python3
"""Defines the City class."""

from models.base_model import BaseModel


class City(BaseModel):
    """Represent a City.
    Attributes:
        state_id: (str): It will be the State.id
        name: (str): The name of the city.
    """

    state_id = ""
    name = ""
