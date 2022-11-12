import sqlalchemy

from domain.interfaces.use_case import UseCase
from domain.ports.create_table_port import (
    CreateTableFromCSVOutputPort,
    CreateTableFromCSVPort,
)
from frameworks.database.postgres_manager import PostgresqlManager


class CreateTableFromCSVUseCase(UseCase):
    """Create table from CSV use case"""

    def __init__(self, db_service: PostgresqlManager) -> None:
        self._db_service = db_service

    async def __call__(
        self, input_port: CreateTableFromCSVPort
    ) -> CreateTableFromCSVOutputPort:
        """Business logic create a new table"""
        engine = sqlalchemy.create_engine(
            "postgresql://postgres:postgres@localhost:5435/db_pizza_place"
        )
        try:
            data = input_port.data_frame
            data.to_sql(
                input_port.csv_filename, engine, if_exists="append", index=False
            )
            return CreateTableFromCSVOutputPort(
                operation=f"Create new table from csv {input_port.csv_filename}",
                result="Success",
            )
        except Exception as error:
            return CreateTableFromCSVOutputPort(
                operation=f"Create new table from csv {input_port.csv_filename}",
                result=f"Error: {error}",
            )
