from random import choice, randint

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Well, you\'re awefully silent...'
    elif 'hello' in lowered:
        return 'Hey there!'
    elif 'how are you' in lowered:
        return 'Good, thanks for asking'
    elif 'bye' in lowered:
        return 'See you!'
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1, 6)}'
    else:
        return choice(['Arigato gosai mastaka',
                       'Demo wakara nai, gomennasai',
                       'jaane matana Luffy!'])
    # raise NotImplementedError('Code is missing ..')