import random
import time

from sqlalchemy import insert, select, exists
from connection.db import Session, engine
from telebot import types
import telebot
from models.user import User

banword = ['nigger', 'крутой', 'прошмандовка Aruku', 'nigga', 'сучка', 'naga', 'cын булочника','приёмыш', 'подвальный ребёнок', 'ниггер', 'бездарь', 'нига', 'ушлёпок', 'уебан', 'тварь уродливая', 'нага', 'гомодрил', 'сын миража', 'faggot', 'шлюха', 'пидор', 'пидорас', 'педик', 'гомик', 'петух']

# Указываем токен вашего бота
TOKEN = '6734713504:AAH1v07_y86elzFk0Y6rL-QsRYOi_FUmjQ4'

# Создаем экземпляр бота
bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])

def entered_users(message):

    with Session.begin() as session:
        user_have = session.query(exists().where(User.id == message.from_user.id)).scalar()
        if not user_have:
            users_dict = dict(id = message.from_user.id, name = message.from_user.first_name, username = message.from_user.username)
            query = insert(User).values(users_dict)
            session.execute(query)
            session.commit()
        else:
            bot.send_message(message.chat.id, 'Вы уже зарегались')



    # users_dict = dict(id = message.from_user.id+8, name = message.from_user.first_name, username = message.from_user.username)
    # query = select(User.username).select_from(User)
    # with Session.begin() as session:
    #     t=session.execute(query).all()
    # bot.send_message(message.chat.id,f'{t}')





# def handle_start(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     button1 = types.KeyboardButton('5 причин зайти на сервер ARUKU')
#     markup.add(button1)
#     bot.send_message(message.chat.id, "ну поехали ", reply_markup=markup)


@bot.message_handler(commands=['coinflip'])

def coin_choice(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(types.KeyboardButton('Орёл'), types.KeyboardButton('Новосиб'))
    bot.reply_to(message, "Выберите орёл или новосиб:", reply_markup=markup)
    bot.register_next_step_handler(message, process_coin_choice)

def process_coin_choice(message):
    choice = message.text.lower()
    if choice not in ['орёл', 'новосиб']:
        bot.reply_to(message, "Пожалуйста, выберите орёл или новосиб.")
        return

    result = random.choice(['орёл', 'новосиб'])
    img = open('media/coinflip.gif', 'rb')
    sent_message = bot.send_animation(message.chat.id, img)

    time.sleep(3)

    if choice == result:
        bot.reply_to(message, f'Победа! Вы выбрали {choice}, результат: {result}.')
    else:
        bot.reply_to(message, f'Проебал! Вы выбрали {choice}, результат: {result}.')

    bot.delete_message(message.chat.id, sent_message.message_id)



# Обработчик команды /help
@bot.message_handler(commands=['help'])
def handle_help(message):
    help_text = "Доступные команды:\n"
    help_text += "/start - начать взаимодействие с ботом\n"
    help_text += "/coinflip - подбросить монетку\n"
    help_text += "/who - узнать кто ты по жизни\n"
    bot.send_message(message.chat.id, help_text)

@bot.message_handler(commands=['who'])

def who_i_am(message):
    bot.reply_to(message, f'{message.from_user.username} сегодня - {random.choice(banword)}')

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
        button2 = types.KeyboardButton('/coinflip')
        button3 = types.KeyboardButton('Приватка с MoralFuck')
        button4 = types.KeyboardButton('MoralFuck')
        button5 = types.KeyboardButton('MoralFuck в 115-й')
        markup2.add(button1,button2, button3, button4, button5)
        bot.send_message(message.chat.id, 'Выбери причину', reply_markup=markup2)


    # elif message.text == 'Тетрис с MoralFuck':
    #     bot./(message.chat.id,'он тут лучший')
    # elif message.text == '/coinflip':
    #     bot.reply_to(message.chat.id,'тут тоже лучший')
    # elif message.text == 'MoralFuck':
    #     bot.reply_to(message.chat.id,'5/5')
    #
    # elif message.text == 'MoralFuck в 115-й':
    #     bot.reply_to(message.chat.id,'??')
    #
    # elif message.text == 'Приватка с MoralFuck':
    #     bot.reply_to(message.chat.id,'да?')




    # if message.text.lower() in banword:
    #     bot.ban_chat_member(message.chat.id, message.from_user.id)
    #     bot.send_message(message.chat.id, 'Идёт нахуй')




# Запускаем бота
bot.polling()