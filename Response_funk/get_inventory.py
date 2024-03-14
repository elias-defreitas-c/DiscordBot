import sqlite3

from sqlite.database_name import DATABASE_NAME


def get_inventory(user_id: str) -> list[str]:
    con = sqlite3.connect(DATABASE_NAME)
    cur = con.cursor()
    cur.execute("SELECT item, amount FROM inventory WHERE user_id = ?", (user_id,))
    rows = cur.fetchall()
    con.close()
    inventory = [f"\n{amount}x {item}" for item, amount in rows]
    return inventory
