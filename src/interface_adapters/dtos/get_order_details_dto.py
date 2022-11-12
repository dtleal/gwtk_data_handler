from pydantic import BaseModel  # pylint: disable=E0611
from pydantic import Field  # pylint: disable=E0611


class GetOrderDetailsOutputDTO(BaseModel):
    """GetOrderDetails DTO"""

    order_details_id: int = Field(default=None)
    order_id: int = Field(default=None)
    pizza_id: str = Field(default=None)
    quantity: int = Field(default=None)
