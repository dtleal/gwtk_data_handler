from domain.interfaces.use_case import UseCase
from domain.ports.get_order_details_port import (
    OrderDetailsInputPort,
    OrderDetailsOutputPort,
)
from frameworks.database.postgres_manager import PostgresqlManager
from interface_adapters.data.models.order_details import OrderDetailsModel


class GetOrderDetailsByIdUseCase(UseCase):
    """Get order details by id"""

    def __init__(
        self, db_service: PostgresqlManager, order_details_model: OrderDetailsModel
    ) -> None:
        self._db_service = db_service
        self._order_details_model = order_details_model

    async def __call__(
        self, input_port: OrderDetailsInputPort
    ) -> OrderDetailsOutputPort:
        await self._db_service.connect()
        async with self._db_service.session() as session:
            if result := await self._order_details_model.find_by_id(
                session, input_port.order_details_id
            ):
                return result
        return await OrderDetailsOutputPort(
            order_details_id=result.order_details_id,
            order_id=result.order_id,
            pizza_id=result.pizza_id,
            quantity=result.quantity,
        )
