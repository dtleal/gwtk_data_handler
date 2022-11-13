from pydantic import BaseModel  # pylint: disable=E0611
from pydantic import Field  # pylint: disable=E0611


class GetMostSoldOutputDTO(BaseModel):
    """GetMostSold DTO"""

    pizza_id: str = Field(default=None)
    pizza_sold: int = Field(default=None)
    price: float = Field(default=None)
    name: str = Field(default=None)
    category: str = Field(default=None)


class GetMostSoldPerDayOutputDTO(BaseModel):
    """GetMostSoldPerDay DTO"""

    result: list = Field(default=None)
