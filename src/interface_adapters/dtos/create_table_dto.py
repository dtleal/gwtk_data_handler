from pydantic import BaseModel  # pylint: disable=E0611
from pydantic import Field  # pylint: disable=E0611


class CreateTableOutputDTO(BaseModel):
    """CreateTable DTO"""

    operation: str = Field(default=None)
    result: str = Field(default=None)
