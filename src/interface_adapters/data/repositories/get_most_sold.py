from domain.ports.get_most_sold_port import GetMostSoldOutputPort
from frameworks.database.postgres_manager import PostgresqlManager
from interface_adapters.data.models.order_details import OrderDetailsModel


class GetMostSoldRepository:
    """Repository to handle with order details."""

    def __init__(self, database_service: PostgresqlManager) -> None:
        self._db = database_service

    async def get_most_sold(self) -> GetMostSoldOutputPort:
        """Get most solded pizza."""
        await self._db.connect()
        async with self._db.session() as session:
            if result := await OrderDetailsModel.get_most_sold(session):
                return result
        return await result

