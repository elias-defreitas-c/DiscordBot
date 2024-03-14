from Response_funk.get_inventory import get_inventory
from Response_funk.adding_items import add_item
from Response_funk.deleting_items import del_item
from Response_funk.input_spliter import split_command
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
        return roll_dice(int(amount_dice), int(eye_dice))

    elif '?inventory' in lowered:
        return get_inventory(user_id)

    elif '?add_item' in lowered:
        item, amount = split_command(user_input, "?add_item")
        return add_item(user_id, item, amount)

    elif '?remove_item' in lowered:
        item, amount = split_command(user_input, "?remove_item")
        return del_item(user_id, item, amount)
