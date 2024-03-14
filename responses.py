from Response_funk.get_inventory import get_inventory
from Response_funk.adding_items import add_item
from Response_funk.deleting_items import del_item
from Response_funk.rolling_dice import roll_dice

def get_response(user_input: str, user_id: str) -> str:
    lowered: str = user_input.lower()
    d_index = user_input.find('d')
    questionmark_index = user_input.find('?')
    amount_dice = user_input[questionmark_index + 1:d_index]
    eye_dice = user_input[d_index + 1:]

    if lowered == '?help':
        return 'Here is every command: *Not implemented yet*'

    elif f'?{amount_dice}d{eye_dice}' in lowered:
        if int(amount_dice) > 9:
            return 'You can only roll 9 dice at one time. You IDIOT SANDWICH!'
        elif int(eye_dice) > 999:
            return 'The eyes are only allowed to be max 999. Why would you ever need more?'
        else:
            try:
                return f'{roll_dice(int(amount_dice), int(eye_dice))}'
            except Exception as ex:
                return f"An error occurred: {ex}"

    elif '?add_item' in lowered:
        parts = user_input.split()
        item_index = parts.index("?add_item") + 1  # Index after the "?add_item" command
        amount_index = next((i for i, part in enumerate(parts) if part.isdigit()), None)
        print(parts)
        item = ' '.join(parts[item_index:amount_index]) if amount_index is not None else ' '.join(parts[item_index:])
        if amount_index is not None:
            amount = int(parts[amount_index])
        else:
            amount = 1
        return add_item(user_id, item, amount)


    elif '?remove_item' in lowered:
        parts = user_input.split()
        amount_index = next((i for i, part in enumerate(parts) if part.isdigit()), None)
        item = ' '.join(parts[1:amount_index])
        print(parts)
        if amount_index is not None:
            amount = int(parts[amount_index])
            return del_item(user_id, item, amount)
        else:
            return del_item(user_id, item, 1)


    elif '?inventory' in lowered:
        inventory = get_inventory(user_id)
        if inventory:
            return f"Your inventory: {' '.join(inventory)}"
        else:
            return "Your inventory is empty."


