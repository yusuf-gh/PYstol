

from telebot.types import  KeyboardButton

question1: dict = {
    'Nickname': "Phewhh, now we have a common language😅",
    'start':"Let's start...",
    'add_player': 'Enter player name',
    "players": 'Players',
    "player": 'Player',
    'add': 'Add player 👥',
    'rules':'Game rules 📃',
    'rules2':"Welcome to Russian Roulette...\n"
            "Rules: Players shoot in turn at which they were added ...\n"
            "Max. amount of players is 6\n"
            "So... that's all. Good luck...(you'll need it😉)",
    'oops':"Oops, some thing went wrong\n"
            "Please choose the given option delow...",
    'start_game': "Start the game",
    'start2': 'Start...',
    'no_players': "Not enough players to start the game...",
    'added': "Player has been added",
    'not_enough': "Not enough players",
    "too_much": 'Too much players (max6)',
    '01':"Player",
    '02':"shoot...",
    'blabla':"Let's go...",
    'shoot': 'Shoot💥🔫',
    "enter": "Welcome to Russian Roulette...",
    "add_player1": "Enter the amount of players (no less than 2 players can play)",
    
}

buttons2: dict={
    'add': KeyboardButton(text='Add player 👥'),
    'rules': KeyboardButton(text='Game rules 📃'),
    'start_game': KeyboardButton(text='Start the game'),
    'shoot': KeyboardButton(text='Shoot💥🔫'),
    'start': KeyboardButton(text='Start...'),
}