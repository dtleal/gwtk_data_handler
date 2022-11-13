# pylint: disable=R0801,R0902
from __future__ import annotations

from sqlalchemy import Column, ForeignKey, Integer, String

from interface_adapters.data.models.base import Model


class OrderDetailsModel(Model):
    """Database representation for table orders"""

    order_details_id = Column(Integer, primary_key=True, index=True)
    order_id = Column(
        Integer,
        ForeignKey("orders.order_id", ondelete="CASCADE"),
        index=True,
    )
    pizza_id = Column(
        String,
        ForeignKey("pizzas.pizza_id", ondelete="CASCADE"),
        index=True,
    )
    quantity = Column(Integer)
