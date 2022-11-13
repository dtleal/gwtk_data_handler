# pylint: disable=R0801,R0902
from __future__ import annotations

from typing import Optional

from sqlalchemy import Column, ForeignKey, Integer, String, select, text
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.expression import Select

from domain.ports.get_most_sold_port import (
    GetMostSoldOutputPort,
    GetMostSoldPerDayOutputPort,
)
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

    @classmethod
    async def get_most_sold(
        cls,
        session: AsyncSession,
    ) -> GetMostSoldOutputPort:
        """Get most selled piza."""
        try:
            query = text(
                "SELECT od.pizza_id, COUNT(od.pizza_id) as pizza_sold, p.price, \
            pt.name, pt.category FROM order_details od join pizzas p on od.pizza_id = p.pizza_id \
            join pizza_types pt on pt.pizza_type_id = p.pizza_type_id group by od.pizza_id, p.size, \
            p.price, pt.name, pt.category order by pizza_sold DESC limit 1;"
            )
            resultset: Result = await session.execute(query)
            result = resultset.fetchall()
            return GetMostSoldOutputPort(
                pizza_id=result[0][0],
                pizza_sold=result[0][1],
                price=result[0][2],
                name=result[0][3],
                category=result[0][4],
            )

        except Exception as e:
            print("Error: ", e)

    @classmethod
    async def get_most_sold_per_day(
        cls,
        session: AsyncSession,
    ) -> GetMostSoldPerDayOutputPort:
        """Get most selled piza."""
        try:
            query = text(
                "SELECT o.date, COUNT(o.date) as pizzas_sold, od.pizza_id,	p.price, \
            pt.name, pt.category FROM orders o join order_details od on \
            o.order_id = od.order_id join pizzas p on od.pizza_id = p.pizza_id \
            join pizza_types pt on pt.pizza_type_id = p.pizza_type_id group by o.date, \
            od.pizza_id, p.price, pt.name, pt.category order by pizzas_sold DESC limit 5;"
            )
            resultset: Result = await session.execute(query)
            result = resultset.fetchall()
            return GetMostSoldPerDayOutputPort(result=result)
        except Exception as e:
            print("Error: ", e)
