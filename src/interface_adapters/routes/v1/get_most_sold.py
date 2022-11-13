from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from frameworks.container import FrameworkContainer
from domain.use_cases.get_most_sold import GetMostSoldUseCase
from interface_adapters.dtos.get_most_sold import GetMostSoldOutputDTO

most_sold_route = APIRouter()


@most_sold_route.get(
    "/most/popular/", response_model=GetMostSoldOutputDTO
)
@inject
async def get_most_sold(
    get_most_sold_use_case: GetMostSoldUseCase = Depends(
        Provide[FrameworkContainer.get_most_sold_use_case]
    ),
) -> GetMostSoldOutputDTO:
    """Route to get the most popular selled pizza"""
    try:
        output_use_case = await get_most_sold_use_case()
        print(output_use_case)

        return GetMostSoldOutputDTO(
            pizza_id=output_use_case.pizza_id,
            pizza_sold=output_use_case.pizza_sold,
            price=output_use_case.price,
            name=output_use_case.name,
            category=output_use_case.category
        )
    except Exception as error:
        return {"error": f"{error}"}
