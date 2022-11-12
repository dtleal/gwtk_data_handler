from dependency_injector import containers, providers

from frameworks.database.postgres_manager import PostgresqlManager


class FrameworkContainer(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(
        modules=[
            "interface_adapters.routes.v1.route",
        ],
    )

    database_manager = providers.Factory(PostgresqlManager)
    # instanciar o use case e passar o db_manager
