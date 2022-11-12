import pandas
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, File, UploadFile

from domain.ports.create_table_port import CreateTableFromCSVPort
from domain.use_cases.create_table_from_csv import CreateTableFromCSVUseCase
from frameworks.container import FrameworkContainer
from interface_adapters.dtos.create_table_dto import CreateTableOutputDTO

csv_route = APIRouter()


@csv_route.post("/create/table", response_model=dict)
@inject
async def create_upload_file(
    csv_file: UploadFile = File(description="A file read as UploadFile"),
    create_table_from_csv_use_case: CreateTableFromCSVUseCase = Depends(
        Provide[FrameworkContainer.create_table_from_csv_use_case]
    ),
) -> CreateTableOutputDTO:
    """Route to create a new table into postgres from a csv file"""
    try:
        contents = pandas.read_csv(csv_file.file, encoding="UTF-8")
        input_port = CreateTableFromCSVPort(
            csv_filename=csv_file.filename, data_frame=contents
        )
        output_use_case = await create_table_from_csv_use_case(input_port=input_port)
        return CreateTableOutputDTO(
            operation=output_use_case.operation, result=output_use_case.result
        )
    except Exception as error:
        return CreateTableOutputDTO(
            operation="Create new table from csv file", result=f"{error}"
        )
