def split_command(user_input: str, command: str) -> (str, str, int):
    """
    Splits the user input to extract the item name and amount from a command.
    :param user_input: The user input string.
    :param command: The command to split on.
    :return: A tuple containing the item name, amount, and the index of the amount in the input.
    """
    parts = user_input.split()
    command_index = parts.index(command) + 1  # Index after the command
    amount_index = next((i for i, part in enumerate(parts) if part.isdigit()), None)
    item = ' '.join(parts[command_index:amount_index]) if amount_index is not None else ' '.join(parts[command_index:])
    amount = int(parts[amount_index]) if amount_index is not None else 1
    return item, amount, amount_index