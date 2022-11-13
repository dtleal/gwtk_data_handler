from domain.ports.get_order_details_port import OrderDetailsOutputPort
from frameworks.database.postgres_manager import PostgresqlManager
from interface_adapters.data.models.order_details import OrderDetailsModel


class OrderDetailsRepository:
    """Repository to handle with order details."""

    def __init__(self, database_service: PostgresqlManager) -> None:
        self._db = database_service

    async def get_order_details_by_id(
        self, order_details_id: int
    ) -> OrderDetailsOutputPort:
        """Get an order details by id."""
        await self._db.connect()
        async with self._db.session() as session:
            if result := await OrderDetailsModel.find_by_id(session, order_details_id):
                return result
        return await OrderDetailsOutputPort(
            order_details_id=result.order_details_id,
            order_id=result.order_id,
            pizza_id=result.pizza_id,
            quantity=result.quantity,
        )
