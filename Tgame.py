import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

from random import *

Players: list = []  # PLAYERS LIST
delete = ReplyKeyboardRemove()
bullet = randint(1, 7)

question: dict = {}  # BOT'S MESSAGES
buttons: dict = {}  # BUTTONS


token = "6242109060:AAGwaucxbFeEpiN2jU9Sw-GLTsEOme0LpZc"
bot = telebot.TeleBot(token)

buttons01 = {
    'btn1': KeyboardButton(text='English 🇬🇧'),
    'btn2': KeyboardButton(text='Русский 🇷🇺'),

}


@bot.message_handler(commands=["start"])
def entrance(message):
    btn = ReplyKeyboardMarkup(resize_keyboard=True)
    btn.add(buttons01.get('btn1'), buttons01.get('btn2'))

    bot.send_message(message.chat.id, "Hello, and wellcome to Russian roulette ... \n"
                                      "The first we need to do is to choose the language 🙃", reply_markup=btn)


@bot.message_handler(content_types=["text"])
def func(message):
    btn = ReplyKeyboardMarkup(resize_keyboard=True)
    btn.add(buttons01.get('btn1'), buttons01.get('btn2'))
    global question, buttons

    if message.text == "English 🇬🇧":
        from text_en import question1
        from text_en import buttons2

    elif message.text == "Русский 🇷🇺":
        from text_ru import question1
        from text_ru import buttons2

    elif message.text == question.get('rules'):
        bot.send_message(message.chat.id, question.get('rules2'))

    elif message.text == question.get('add'):
        x = bot.send_message(message.chat.id, question.get('add_player'))
        bot.register_next_step_handler(x, add_user)

    elif message.text == question.get('start_game'):
        bot.send_message(message.chat.id, question.get('blabla'), reply_markup=delete)
        game_process(message)

    else:
        bot.send_message(message.chat.id, "Please choose the given option...", reply_markup=btn)
        btn1 = ReplyKeyboardMarkup(resize_keyboard=True)
        btn1.add(buttons.get('rules'), buttons.get('add'), buttons.get('start_game'))
        bot.send_message(message.chat.id, question.get('start'), reply_markup=btn1)

    question.update(question1)
    buttons.update(buttons2)
    bot.send_message(message.chat.id, question.get('Nickname'), reply_markup=delete)

    btn1 = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1.add(buttons.get('rules'), buttons.get('add'), buttons.get('start_game'))
    bot.send_message(message.chat.id, question.get('start'), reply_markup=btn1)


""" начало игры -> """

def game_process(message):
    if len(Players) < 3:
        bot.send_message(message.chat.id, "людей недостаточно")
    else:
        pass




def add_user(message):
    if len(Players) == 6:
        btn1 = ReplyKeyboardMarkup(resize_keyboard=True)
        btn1.add(buttons.get('add'), buttons.get('rules'), buttons.get('start_game'))
        bot.send_message(message.chat.id, "людей уже 6", reply_markup=btn1)
    elif len(Players) < 6:
        Players.append(message.text)

        bot.send_message(message.chat.id, question['added'])
        btn1 = ReplyKeyboardMarkup(resize_keyboard=True)
        btn1.add(buttons.get('add'), buttons.get('rules'), buttons.get('start_game'))

        bot.send_message(message.chat.id, "Поставьте здесь что нибудь Юсуф (132 строка)", reply_markup=btn1)




bot.infinity_polling()
