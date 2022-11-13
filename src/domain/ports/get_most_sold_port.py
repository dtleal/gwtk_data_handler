# pylint: disable=R0801,R0902
from pydantic.dataclasses import dataclass

from domain.interfaces.input_port import InputPort


@dataclass
class GetMostSoldOutputPort(InputPort):
    """Object to describe a the result of most solded pizza."""

    pizza_id: str
    pizza_sold: int
    price: float
    name: str
    category: str


@dataclass
class GetMostSoldPerDayOutputPort(InputPort):
    """Object to describe a the result of most solded pizza."""

    result: list
