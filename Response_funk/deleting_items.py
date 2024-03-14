import sqlite3

from Response_funk.searching import search_entry, search_entry_amount
from sqlite.database_name import DATABASE_NAME


def del_item(user_id: str, item: str, amount: int):
    con = sqlite3.connect(DATABASE_NAME)
    cur = con.cursor()
    if not search_entry(item):
        return f"{item} is not in your Inventory"
    else:
        current_amount = search_entry_amount(user_id, item)
        new_amount = current_amount - amount
        if new_amount <= 0:
            cur.execute("DELETE FROM inventory WHERE user_id = ? AND item = ?", (user_id, item))
            con.commit()
            con.close()
            return f"Removed '{item}' completely from your inventory."
        else:
            cur.execute("UPDATE inventory SET amount = ? WHERE user_id = ? AND item = ?", (new_amount, user_id, item))
            con.commit()
            con.close()
            return f"Removed {amount}x '{item}' from your inventory."