from dependency_injector import containers, providers

from domain.use_cases.create_table_from_csv import CreateTableFromCSVUseCase
from domain.use_cases.get_order_details import GetOrderDetailsByIdUseCase
from frameworks.database.postgres_manager import PostgresqlManager


class FrameworkContainer(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(
        modules=[
            "interface_adapters.routes.v1.upload_csv",
            "interface_adapters.routes.health_check",
        ],
    )

    database_manager: PostgresqlManager = providers.Factory(PostgresqlManager)

    create_table_from_csv_use_case: CreateTableFromCSVUseCase = providers.Factory(
        CreateTableFromCSVUseCase, db_service=database_manager
    )

    get_order_details_use_case: GetOrderDetailsByIdUseCase = providers.Factory(
        GetOrderDetailsByIdUseCase, db_service=database_manager
    )
