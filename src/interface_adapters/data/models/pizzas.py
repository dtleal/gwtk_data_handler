# pylint: disable=R0801,R0902
from __future__ import annotations

from sqlalchemy import DECIMAL, Column, ForeignKey, String

from interface_adapters.data.models.base import Model


class PizzasModel(Model):
    """Database representation for table pizzas"""

    pizza_id = Column(String, primary_key=True, index=True)
    pizza_type_id = Column(
        String,
        ForeignKey("pizza_types.pizza_type_id", ondelete="CASCADE"),
        index=True,
    )
    size = Column(String(length=3))
    price = Column(DECIMAL(7, 1))
