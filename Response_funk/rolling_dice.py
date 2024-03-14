from random import randint


def roll_dice(number, dice):
    term = ''
    total = 0
    init_number = number
    if int(number) > 9:
        return 'You can only roll 9 dice at one time. You IDIOT SANDWICH!'
    elif int(dice) > 999:
        return 'The eyes are only allowed to be max 999. Why would you ever need more?'
    else:
        while number >= 1:
            roll = randint(1, dice)
            term += f'{roll} + '
            total += roll
            number -= 1
        return f'```You rolled {init_number}d{dice} and got: {term[:-3]} = {total}```'



