import sqlite3

from Response_funk.searching import search_entry, search_entry_amount
from sqlite.database_name import DATABASE_NAME


def add_item(user_id: str, item: str, amount: int):
    con = sqlite3.connect(DATABASE_NAME)
    cur = con.cursor()
    if not search_entry(item):
        cur.execute("INSERT INTO inventory (user_id, item, amount) VALUES (?, ?, ?)", (user_id, item, amount))
        con.commit()
        con.close()
        return f"Added {amount}x '{item}' to your inventory."
    else:
        current_amount = search_entry_amount(user_id, item)
        new_amount = current_amount + amount  # Add the new amount to the current amount
        cur.execute("UPDATE inventory SET amount = ? WHERE user_id = ? AND item = ?", (new_amount, user_id, item))
        con.commit()
        con.close()
        return f"Added {amount}x '{item}' to your inventory."
