import sqlite3


def create_table(self, tablename, table_structure):
    connection = sqlite3.connect(
        "C:\\Users\\jakub\\OneDrive\\Documents\\github\\REST\\database.db",
        timeout=200,
    )
    cursor = connection.cursor()
    create = f"CREATE TABLE {tablename} {table_structure}"

    cursor.execute(create)
    connection.close()


def update_table(self, tablename, data):
    connection = sqlite3.connect(
        "C:\\Users\\jakub\\OneDrive\\Documents\\github\\REST\\database.db",
        timeout=200,
    )
    data.to_sql(tablename, connection, if_exists="append", index=False)
    connection.close()


def delete_table(self, tablename):
    connection = sqlite3.connect(
        "C:\\Users\\jakub\\OneDrive\\Documents\\github\\REST\\database.db",
        timeout=200,
    )
    cursor = connection.cursor()
    drop_table = f"DROP TABLE {tablename}"
    cursor.execute(drop_table)
    connection.close()


def get_item(item_name):
    connection = sqlite3.connect(
        "C:\\Users\\jakub\\OneDrive\\Documents\\github\\REST\\database.db",
        timeout=200,
    )
    cursor = connection.cursor()

    get = f"SELECT * FROM items_of_interest WHERE item_id='{item_name}'"

    cursor.execute(get)
    connection.close()
