# pylint: disable=R0801,R0902
from typing import Any

from pydantic.dataclasses import dataclass

from domain.interfaces.input_port import InputPort


@dataclass
class OrderDetailsInputPort(InputPort):
    """Object to describe a Address."""

    order_details_id: int


@dataclass
class OrderDetailsOutputPort(InputPort):
    """Object to describe a Address."""

    order_details_id: int
    order_id: int
    pizza_id: str
    quantity: int

