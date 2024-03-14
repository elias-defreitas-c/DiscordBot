import sqlite3

from sqlite.database_name import DATABASE_NAME


def search_entry(entry) -> [str]:
    con = sqlite3.connect(DATABASE_NAME)
    cur = con.cursor()
    cur.execute("SELECT * FROM inventory WHERE item = ?", (entry,))
    rows = cur.fetchall()
    result = [row[1] for row in rows]
    con.close()
    return result


def search_entry_amount(user_id, entry) -> int:
    con = sqlite3.connect(DATABASE_NAME)
    cur = con.cursor()
    cur.execute("SELECT amount FROM inventory WHERE user_id = ? AND item = ?", (user_id, entry))
    result = cur.fetchone()
    con.close()
    return result[0] if result is not None else 0