import sqlite3

from sqlite.database_name import DATABASE_NAME


def create_tables() -> None:
    con = sqlite3.connect(DATABASE_NAME)
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS inventory (user_id TEXT, item TEXT, amount NUMBER)")
    con.commit()
    con.close()