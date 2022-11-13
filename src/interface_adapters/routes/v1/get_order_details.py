import pandas
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from domain.ports.get_order_details_port import (
    OrderDetailsInputPort,
    OrderDetailsOutputPort
)
from domain.use_cases.get_order_details import GetOrderDetailsByIdUseCase
from frameworks.container import FrameworkContainer
from interface_adapters.dtos.get_order_details_dto import GetOrderDetailsOutputDTO

order_details_route = APIRouter()


@order_details_route.get(
    "/order/details/{order_details_id}", 
    response_model=GetOrderDetailsOutputDTO
)
@inject
async def get_order_details(
    order_details_id: int,
    get_order_details_use_case: GetOrderDetailsByIdUseCase = Depends(
        Provide[FrameworkContainer.get_order_details_use_case]
    ),
) -> GetOrderDetailsOutputDTO:
    """Route to create a new table into postgres from a csv file"""
    try:
        input_port = OrderDetailsInputPort(order_details_id=order_details_id)

        output_use_case = await get_order_details_use_case(input_port=input_port)

        return GetOrderDetailsOutputDTO(
            order_details_id=output_use_case.order_details_id,
            order_id=output_use_case.order_id,
            pizza_id=output_use_case.pizza_id,
            quantity=output_use_case.quantity
        )
    except Exception as error:
        return {"error": f"{error}"}
