# pylint: disable=R0801,R0902
from typing import Any

from pydantic.dataclasses import dataclass

from domain.interfaces.input_port import InputPort


@dataclass
class CreateTableFromCSVPort(InputPort):
    """Object to describe a csv file."""

    csv_filename: str
    data_frame: Any


@dataclass
class CreateTableFromCSVOutputPort(InputPort):
    """Object to describe a csv file."""

    operation: str
    result: Any
