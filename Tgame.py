import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

from random import *


Players: list=[]
delete = ReplyKeyboardRemove()
bullet = randint(1,7)



question: dict = {}                             #BOT'S MESSAGES
buttons: dict = {}                                                     #BUTTONS
                                                            #PLAYERS LIST



token = "6609681759:AAFyL-FOOHH4fmZrOXe_y482njhWGwgtFs4"
bot = telebot.TeleBot(token)


buttons01 ={
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

   

    elif message.text ==  question.get('rules'):
         bot.send_message(message.chat.id, question.get('rules2'))



    elif message.text == question.get('add'):
        x = bot.send_message(message.chat.id, question.get('add_player'))
        bot.register_next_step_handler(x, add_user)


    elif message.text == question.get('start_game'):
        
        bot.send_message(message.chat.id, question.get('blabla'), reply_markup=delete)
        game_process(message, Players)

    else: 
        bot.send_message(message.chat.id, "Please choose the given option...", reply_markup=btn)
        btn1 = ReplyKeyboardMarkup(resize_keyboard=True)
        btn1.add(buttons.get('rules'),buttons.get('add'), buttons.get('start_game'))
        bot.send_message(message.chat.id, question.get('start'),reply_markup=btn1)
       
    
        


    question.update(question1)
    buttons.update(buttons2)
    bot.send_message(message.chat.id, question.get('Nickname'),reply_markup=delete)



    btn1 = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1.add(buttons.get('rules'),buttons.get('add'), buttons.get('start_game'))
    bot.send_message(message.chat.id, question.get('start'),reply_markup=btn1)
    









def game_process(message, list1):
    btn = ReplyKeyboardMarkup(resize_keyboard=True)
    btn.add(buttons.get('start'))
    btn1 = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1.add(buttons.get('shoot'))
    




    # list_line = sample(range(1,7), len(list1))






    for i, element in enumerate(list1, start=1):
        # random_num = list_line[i-1]
        bot.send_message(message.chat.id, f"{question.get('player')} : {i} - {element} ",reply_markup=btn)

            
        if len(list1) in range(3, 7):
            x = 6 - len(list1)
            add = list1[:x]
            list1.extend(add)
        elif len(list1) == 2:
            x = 2
            add = list1[:x]
            list1.extend(add)
            list1.extend(add)
        elif len(list1) <= 1 :
            bot.send_message(message.chat.id, question.get('not_enough'), func(message))
        
        else:
            pass


        if message.text == question.get('start2'): #___________________________________


            for y in list1:
                s= bot.send_message(message.chat.id, f"{question.get('player')} : {i} - {element}\n", f" {question.get('01')} {y} {question.get('02')} ", reply_markup=btn1 )
                bot.register_next_step_handler(s, shoot)
                def shoot(message):
                    if message.text == question.get('shoot') :   
                        kill = roulette(i, bullet, list1 )
                        bot.send_message(message.chat.id, kill)
                    else:
                        bot.send_message(message.chat.id, question.get('oops'), reply_markup=btn1)

                        






def roulette(player, bullet1, list ):
    if player == bullet1:
        return list.pop([player])
    else:
        pass




    


















def add_user(message):



    Players.append(message.text)
    


    bot.send_message(message.chat.id, question['added'])
    btn1 = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1.add(buttons.get('add'),buttons.get('rules'),buttons.get('start_game'))

    

    bot.send_message(message.chat.id, reply_markup=btn1)













# def  game_process(message):
#     if len(Players) <= 1:
#         bot.send_message(message.chat.id, question.get('not_enough'))
#     else:
         





    
         

        









   
    
    
    






bot.infinity_polling()
