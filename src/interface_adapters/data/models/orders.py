# pylint: disable=R0801,R0902
from __future__ import annotations

from sqlalchemy import Column, Date, Integer, Time

from interface_adapters.data.models.base import Model


class OdersModel(Model):
    """Database representation for table orders"""

    order_id = Column(Integer, primary_key=True, index=True)
    date = Column(Date(timezone=True))
    time = Column(Time(timezone=True))
