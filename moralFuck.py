#!/usr/bin/python

  # -*- coding: utf8 -*-



from telebot import types

import telebot
import time

banword = ['nigger', 'nigga', 'naga', '������', '����', '����', 'faggot', '�����', '�������', '�����', '�����', '�����']

# ��������� ����� ������ ����
TOKEN = '6734713504:AAH1v07_y86elzFk0Y6rL-QsRYOi_FUmjQ4'

# ������� ��������� ����
bot = telebot.TeleBot(TOKEN)

# ���������� ������� /start
@bot.message_handler(commands=['start'])

def handle_start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('5 ������ ����� �� ������ ARUKU')
    markup.add(button1)
    bot.send_message(message.chat.id, "�� ������� ", reply_markup=markup)


@bot.message_handler(commands=['coinflip'])
def send_coinflip(message):

    img = open('media/coinflip.gif', 'rb')
    bot.send_animation(message.chat.id, img)

# ���������� ������� /help
@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.chat.id, "� ������� ���. ���� ������ �������� �� ���������.")

# ���������� ���� ��������� ��������� � ������
@bot.message_handler(content_types=['text'])
#def handle_message(message):
#    bot.send_message(message.chat.id, message.text)


def check_word(message):
    # if message.text.lower() == '��' or message.text.lower() == '��' :
    #     bot.send_message(message.chat.id,'� �� �� ��������� �������')
    if (message.text == '5 ������ ����� �� ������ ARUKU'):
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('������ � MoralFuck')
        button2 = types.KeyboardButton('�� � MoralFuck')
        button3 = types.KeyboardButton('�������� � MoralFuck')
        button4 = types.KeyboardButton('MoralFuck')
        button5 = types.KeyboardButton('MoralFuck � 115-�')
        markup2.add(button1,button2, button3, button4, button5)
        bot.send_message(message.chat.id, '������ �������', reply_markup=markup2)


    elif message.text == '������ � MoralFuck':
        bot.send_message(message.chat.id,'�� ��� ������')
    elif message.text == '�� � MoralFuck':
        bot.send_message(message.chat.id,'��� ���� ������')
    elif message.text == 'MoralFuck':
        bot.send_message(message.chat.id,'5/5')

    elif message.text == 'MoralFuck � 115-�':
        bot.send_message(message.chat.id,'??')

    elif message.text == '�������� � MoralFuck':
        bot.send_message(message.chat.id,'��?')




    if message.text.lower() in banword:
        bot.ban_chat_member(message.chat.id, message.from_user.id)
        bot.send_message(message.chat.id, '��� �����')




# ��������� ����
bot.polling()


