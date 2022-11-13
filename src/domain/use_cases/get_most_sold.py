from domain.interfaces.use_case import UseCase
from domain.ports.get_most_sold_port import GetMostSoldOutputPort
from interface_adapters.data.repositories.get_most_sold import GetMostSoldRepository


class GetMostSoldUseCase(UseCase):
    """Get most sold use case"""

    def __init__(self, get_most_sold_repository: GetMostSoldRepository) -> None:
        self._get_most_sold_repository = get_most_sold_repository

    async def __call__(self) -> GetMostSoldOutputPort:
        return await self._get_most_sold_repository.get_most_sold()
