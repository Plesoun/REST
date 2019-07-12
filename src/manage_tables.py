import sqlite3


class ManageTables:
    def __init__(self):
        self.connection = sqlite3.connect(
            "C:\\Users\\jakub\\OneDrive\\Documents\\github\\REST\\database.db"
        )

    cur = con.cursor()

    create_items = "CREATE TABLE items_of_interest (id int, buy_price_max int, buy_price_min int, city text, item_id text, quality int, sell_price_max int, sell_price_max_date text, sell_price_min int, sell_price_min_date text)"

    create_users = "CREATE TABLE users (id INTEGER PRIMARY KEY, username text, password text)"

    sel_q = "SELECT * FROM mytable"

    drop = "DROP TABLE users"

    cur.execute(create_users)
    con.commit()
    con.close()
