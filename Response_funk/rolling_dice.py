from random import randint


def roll_dice(number, dice):
    term = ''
    total = 0
    init_number = number
    while number >= 1:
        roll = randint(1, dice)
        term += f'{roll} + '
        total += roll
        number -= 1

    return f'```You rolled {init_number}d{dice} and got: {term[:-3]} = {total}```'