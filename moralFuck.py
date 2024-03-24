#!/usr/bin/python

  # -*- coding: utf8 -*-



from telebot import types

import telebot
import time

banword = ['nigger', 'nigga', 'naga', 'ниггер', 'нига', 'нага', 'faggot', 'пидор', 'пидорас', 'педик', 'гомик', 'петух']

# Указываем токен вашего бота
TOKEN = '6734713504:AAH1v07_y86elzFk0Y6rL-QsRYOi_FUmjQ4'

# Создаем экземпляр бота
bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])

def handle_start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('5 причин зайти на сервер ARUKU')
    markup.add(button1)
    bot.send_message(message.chat.id, "ну поехали ", reply_markup=markup)


@bot.message_handler(commands=['coinflip'])
def send_coinflip(message):

    img = open('media/coinflip.gif', 'rb')
    bot.send_animation(message.chat.id, img)

# Обработчик команды /help
@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.chat.id, "Я простой бот. Могу только отвечать на сообщения.")

# Обработчик всех текстовых сообщений в беседе
@bot.message_handler(content_types=['text'])
#def handle_message(message):
#    bot.send_message(message.chat.id, message.text)


def check_word(message):
    # if message.text.lower() == 'че' or message.text.lower() == 'чё' :
    #     bot.send_message(message.chat.id,'а ни че нормально общайся')
    if (message.text == '5 причин зайти на сервер ARUKU'):
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Тетрис с MoralFuck')
        button2 = types.KeyboardButton('Кс с MoralFuck')
        button3 = types.KeyboardButton('Приватка с MoralFuck')
        button4 = types.KeyboardButton('MoralFuck')
        button5 = types.KeyboardButton('MoralFuck в 115-й')
        markup2.add(button1,button2, button3, button4, button5)
        bot.send_message(message.chat.id, 'Выбери причину', reply_markup=markup2)


    elif message.text == 'Тетрис с MoralFuck':
        bot.send_message(message.chat.id,'он тут лучший')
    elif message.text == 'Кс с MoralFuck':
        bot.send_message(message.chat.id,'тут тоже лучший')
    elif message.text == 'MoralFuck':
        bot.send_message(message.chat.id,'5/5')

    elif message.text == 'MoralFuck в 115-й':
        bot.send_message(message.chat.id,'??')

    elif message.text == 'Приватка с MoralFuck':
        bot.send_message(message.chat.id,'да?')




    if message.text.lower() in banword:
        bot.ban_chat_member(message.chat.id, message.from_user.id)
        bot.send_message(message.chat.id, 'Идёт нахуй')




# Запускаем бота
bot.polling()


