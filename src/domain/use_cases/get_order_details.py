from domain.interfaces.use_case import UseCase
from domain.ports.get_order_details_port import (
    OrderDetailsInputPort,
    OrderDetailsOutputPort,
)
from interface_adapters.data.repositories.order_details import OrderDetailsRepository


class GetOrderDetailsByIdUseCase(UseCase):
    """Get order details by id"""

    def __init__(self, order_details_repository: OrderDetailsRepository) -> None:
        self._order_details_repository = order_details_repository

    async def __call__(
        self, input_port: OrderDetailsInputPort
    ) -> OrderDetailsOutputPort:
        return await self._order_details_repository.get_order_details_by_id(
            order_details_id=input_port.order_details_id
        )
