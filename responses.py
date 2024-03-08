from random import choice, randint


def roll_dice(number, dice):
    term = ''
    total = 0
    init_number=number
    while number >= 1:
        roll = randint(1, dice)
        term += f'{roll} + '
        total += roll
        number -= 1

    return f'```You rolled {init_number}d{dice} and got: {term[:-3]} = {total}```'


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    d_index = user_input.find('d')
    questionmark_index = user_input.find('?')
    amount_dice = user_input[questionmark_index + 1:d_index]
    eye_dice = user_input[d_index + 1:]

    if lowered == '?help':
        return 'What do you want?!'
    elif '?hello' in lowered:
        return 'Bye retard'
    elif f'?{amount_dice}d{eye_dice}' in lowered:
        if int(amount_dice) > 9:
            return 'You can only roll 9 dice at one time. You IDIOT SANDWICH!'
        elif int(eye_dice) > 999:
            return 'The eyes are only allowed to be max 999. Why would you ever need more?'
        else:
            return f'{roll_dice(int(amount_dice), int(eye_dice))}'
    else:
        return choice(['Bro what are you talking about?',
                       'Shut the fuck up you retard!',
                       'I dont get what you\'re trying to say.'])
