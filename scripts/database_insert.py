import pandas
import sqlalchemy

# Create the engine to connect to the PostgreSQL database
engine = sqlalchemy.create_engine('postgresql://postgres:postgres@localhost:5435/db_pizza_place')


def _insert_into_table_from_csv_file(table_name: str, csv_file: str) -> None:
    # Read data from CSV and load into a dataframe object
    data = pandas.read_csv(csv_file, encoding="UTF-8")

    # Write data into the table in PostgreSQL database
    data.to_sql(table_name, engine, if_exists='append', index=False)


def main() -> None:
    _insert_into_table_from_csv_file(table_name="orders", csv_file="./scripts/csv/orders.csv")
    _insert_into_table_from_csv_file(table_name="pizza_types", csv_file="./scripts/csv/pizza_types.csv")
    _insert_into_table_from_csv_file(table_name="pizzas", csv_file="./scripts/csv/pizzas.csv")
    _insert_into_table_from_csv_file(table_name="order_details", csv_file="./scripts/csv/order_details.csv")


if __name__ == "__main__":
    """A simple script to store data into table from a csv file"""
    main()
