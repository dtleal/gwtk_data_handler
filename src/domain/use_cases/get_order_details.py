import sqlalchemy

from domain.interfaces.use_case import UseCase
from domain.ports.get_order_details_port import (
    OrderDetailsInputPort,
    OrderDetailsOutputPort,
)
from frameworks.database.postgres_manager import PostgresqlManager
from interface_adapters.data.models.oder_details import OderDetailsModel


class GetOrderDetailsByIdUseCase(UseCase):
    """Create table from CSV use case"""

    def __init__(self, db_service: PostgresqlManager, order_details_model: OderDetailsModel) -> None:
        self._db_service = db_service
        self._order_details_model = order_details_model

    async def __call__(
        self, order_input_port: OrderDetailsInputPort
    ) -> OrderDetailsOutputPort:
        self._db_service.connect()
        async with self._db_service.session() as session:
            if order_details := await self._order_details_model.find_by_id(
                session, order_input_port.order_details_id
            ):
                return await order_details
        return None
