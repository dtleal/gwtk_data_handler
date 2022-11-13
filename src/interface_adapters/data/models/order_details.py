# pylint: disable=R0801,R0902
from __future__ import annotations

from typing import Optional

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.expression import Select, select

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

    @classmethod
    async def find_by_id(
        cls, session: AsyncSession, order_details_id: int
    ) -> Optional[OrderDetailsModel]:
        """Find by its id."""
        query: Select = select(cls).filter(cls.order_details_id == order_details_id)
        result: Result = await session.execute(query)
        return result.scalars().first()
