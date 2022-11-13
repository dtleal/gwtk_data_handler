from dependency_injector import containers, providers

from domain.use_cases.create_table_from_csv import CreateTableFromCSVUseCase
from domain.use_cases.get_order_details import GetOrderDetailsByIdUseCase
from frameworks.database.postgres_manager import PostgresqlManager
from interface_adapters.data.repositories.order_details import OrderDetailsRepository


class FrameworkContainer(containers.DeclarativeContainer):
    """Framework container"""

    wiring_config = containers.WiringConfiguration(
        modules=[
            "interface_adapters.routes.v1.upload_csv",
            "interface_adapters.routes.health_check",
            "interface_adapters.routes.v1.get_order_details",
        ],
    )

    database_manager: PostgresqlManager = providers.Factory(PostgresqlManager)

    create_table_from_csv_use_case: CreateTableFromCSVUseCase = providers.Factory(
        CreateTableFromCSVUseCase, db_service=database_manager
    )

    # Repositories
    order_details_repository: OrderDetailsRepository = providers.Factory(
        OrderDetailsRepository, database_service=database_manager
    )

    # Use cases
    get_order_details_use_case: GetOrderDetailsByIdUseCase = providers.Factory(
        GetOrderDetailsByIdUseCase, order_details_repository=order_details_repository
    )
