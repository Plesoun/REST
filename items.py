from datetime import datetime
from src.database import PostgreSQL


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


database = database = PostgreSQL(
    "postgres", "testtest", "localhost:5433/custom_projects", schema="albion"
)


def read_table():
    return database.get_table(table_to_get="market_data")


def read_column():
    pass
