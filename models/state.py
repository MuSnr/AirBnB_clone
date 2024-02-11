#!/usr/bin/python3
"""Contains the State class(Custom)."""
from models.base_model import BaseModel


class State(BaseModel):
    """Represents a state.

    Attributes:
        state_name (str): The name of the state.
    """

    state_name = ""

