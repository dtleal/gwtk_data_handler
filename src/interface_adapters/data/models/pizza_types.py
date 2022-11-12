# pylint: disable=R0801,R0902
from __future__ import annotations

import enum

from sqlalchemy import Column, Enum, String

from interface_adapters.data.models.base import Model


class PizzaTypesEnum(enum.Enum):
    CHICKEN = "Chicken"
    CLASSIC = "Classic"
    SUPREME = "Supreme"
    VEGGIE = "Veggie"


class PizzaTypesModel(Model):
    """Database representation for table pizza_types"""

    pizza_type_id = Column(String, index=True)
    name = Column(String)
    category = Column(Enum(PizzaTypesEnum))
    ingredients = Column(String)
