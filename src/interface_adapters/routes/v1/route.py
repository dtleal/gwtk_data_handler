from fastapi import APIRouter,Depends
from dependency_injector.wiring import Provide, inject

"""
from interface_adapters.api.v1.controllers.first_controller_example import FirstrExampleController
from interface_adapters.api.v1.dtos.first_example_dto import (
    FirstExampleInputDTO, FirstExampleOutputDTO
)
from domain.use_case.first_example.first_example import FirstExampleUseCase
"""
from frameworks.database.postgres_manager import PostgresqlManager
from frameworks.container import FrameworkContainer

router = APIRouter()


@router.post(
    "/first-example",
    response_model=dict
)
@inject
async def first_example_route(
    input_dto: dict,
    database_service: PostgresqlManager = Depends(Provide[FrameworkContainer.database_manager])
) -> dict:
    """"""
    #montar o use case como dependencia - instanciar com o servico database la no container
    #desenvolver o repository - passndo o db que ta aqui injetado
    #passar pro use case uma instancia do repository
    #executar o usecase
    #retornar
    return await {}
