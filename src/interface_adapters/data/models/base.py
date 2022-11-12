# pylint: disable=E0213
from datetime import datetime, timezone
from typing import Any

from sqlalchemy import Column, DateTime
from sqlalchemy.ext.declarative import declarative_base, declared_attr

from utils import algorithms

_Base: Any = declarative_base()


class Model(_Base):
    """Provide a pattern for tablename and common attributes
    such as _created_at and _updated_at"""

    __abstract__ = True
    __name__: str

    _created_at = Column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
    _updated_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )

    @declared_attr
    def __tablename__(cls) -> str:
        """Patternize the tablename based on the name of the model class"""
        tablename_camel_case = cls.__name__.replace("Model", "")
        return algorithms.to_snake_case(tablename_camel_case)
