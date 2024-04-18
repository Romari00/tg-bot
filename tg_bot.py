import random
import re
import time
from datetime import datetime, timedelta

from sqlalchemy import insert, select, exists, update
from telebot.apihelper import ApiException

from connection.db import Session
from telebot import types
import telebot
from models.user import User, Eco, UserLogi, UserWho

banword = ['nigger', 'крутой', 'прошмандовка Aruku', 'nigga', 'сучка', 'naga', 'cын булочника','приёмыш', 'подвальный ребёнок', 'ниггер', 'бездарь', 'нига', 'ушлёпок', 'уебан', 'тварь', 'нага', 'гомодрил', 'сын миража', 'faggot', 'шлюха', 'пидор', 'пидорас', 'педик', 'гомик', 'петух']
special_for_Remedyv = ['прошмандовка Aruku', 'сучка', 'шлюха', 'тварь', 'лучшая']
# Указываем токен вашего бота
TOKEN = '6734713504:AAH1v07_y86elzFk0Y6rL-QsRYOi_FUmjQ4'


# Создаем экземпляр бота
bot = telebot.TeleBot(TOKEN)
none = {6311509652:'Стася'}
# Обработчик команды /start

moralfuck = ['моралфак', 'moralfuck', 'моралфаки', 'моралфака', 'моралкек']
stupid=open('media/stupid.MOV', 'rb')

@bot.message_handler(commands=['secret'])
def test(message):
    bot.delete_messages(message.chat.id,message_ids=[message.message_id, message.message_id-1, message.message_id-2])


@bot.message_handler(commands=['who'])
def who(message):
    # Генерируем случайное слово из списка banword
    random_word = random.choice(banword)

    # Записываем информацию о пользователе в базу данных
    new_who_entry = UserWho(user_id=message.from_user.id, message_id=message.message_id, chat_id=message.chat.id, result=random_word)
    with Session.begin() as session:
        session.add(new_who_entry)
        session.commit()

    # Создаем кнопку для отправки пользователю
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton(f'кто?', callback_data=f'who_result_{message.from_user.id}')
    markup.add(btn1, row_width=8)
    bot.send_message(message.chat.id, 'тык', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data.startswith('who_result_'))
def handle_who_result(call):
    chat_id = call.message.chat.id  # Получаем chat_id
    message_id = call.message.message_id - 1  # Получаем message_id
    # Получаем информацию о пользователе из базы данных
    with Session() as session:
        user_info = session.query(UserWho).filter_by(chat_id=chat_id, message_id=message_id).first()
        username = session.query(User).filter_by(id=user_info.user_id).first()
        if username:
            if username.username != None:
                if user_info:
                    result = user_info.result
                    bot.answer_callback_query(call.id, f'{username.username},  сегодня {result} ❤️', show_alert=True)
                else:
                    bot.send_message(chat_id, "извините")
            else:
                bot.send_message(chat_id, "извините")
        else:
            bot.send_message(chat_id, "извините")


@bot.message_handler(commands=['hug'])
def pat(message):
    hug = open('media/hug.gif', 'rb')
    user_active = message.from_user.username
    if message.reply_to_message:
        user_passive = message.reply_to_message.from_user.username
        if user_active == 'Remedyv':
            bot.reply_to(message, f'{user_active} обнялa {user_passive}')
            bot.send_animation(message.chat.id, hug)

        else:
            bot.reply_to(message, f'{user_active} обнял {user_passive}')
            bot.send_animation(message.chat.id, hug)

@bot.message_handler(commands=['kiss'])
def pat(message):
    kiss = open('media/kiss.gif', 'rb')
    user_active = message.from_user.username
    if message.reply_to_message:
        user_passive = message.reply_to_message.from_user.username
        if user_active == 'Remedyv':
            bot.reply_to(message, f'{user_active} поцеловалa {user_passive}')
            bot.send_animation(message.chat.id, kiss)
        else:
            bot.reply_to(message, f'{user_active} поцеловал {user_passive}')
            bot.send_animation(message.chat.id, kiss)

@bot.message_handler(commands=['hm'])
def pat(message):
    fuck = open('media/fuck.gif', 'rb')
    user_active = message.from_user.username
    if message.reply_to_message:
        user_passive = message.reply_to_message.from_user.username
        bot.reply_to(message, f'{user_active} *кхм* {user_passive}')
        bot.send_animation(message.chat.id, fuck)
@bot.message_handler(commands=['f_ck'])
def pat(message):
    nahui = open('media/nahui.gif', 'rb')
    user_active = message.from_user.username
    if message.reply_to_message:
        user_passive = message.reply_to_message.from_user.username
        if user_active == 'Remedyv':
            bot.reply_to(message, f'{user_active} послала нахуй {user_passive}')
            bot.send_animation(message.chat.id, nahui)
        else:
            bot.reply_to(message, f'{user_active} послал нахуй {user_passive}')
            bot.send_animation(message.chat.id, nahui)

@bot.message_handler(commands=['hit'])
def pat(message):
    kick = open('media/kill.gif', 'rb')
    user_active = message.from_user.username
    if message.reply_to_message:
        user_passive = message.reply_to_message.from_user.username
        if user_active == 'Remedyv':
            bot.reply_to(message, f'{user_active} ударила {user_passive}')
            bot.send_animation(message.chat.id, kick)
        else:
            bot.reply_to(message, f'{user_active} ударил {user_passive}')
            bot.send_animation(message.chat.id, kick)

@bot.message_handler(commands=['nip'])
def pat(message):
    nip = open('media/nip.gif.mp4', 'rb')
    nip_rem = open('media/nip_rem.mp4', 'rb')
    user_active = message.from_user.username
    if message.reply_to_message:
        user_passive = message.reply_to_message.from_user.username
        if user_active == 'Remedyv':
            bot.reply_to(message, f'{user_active} укусила {user_passive}')
            bot.send_animation(message.chat.id, nip_rem)
        else:
            bot.reply_to(message, f'{user_active} укусил {user_passive}')
            bot.send_animation(message.chat.id, nip)

@bot.message_handler(commands=['pat'])
def pat(message):
    hug = open('media/hug_women.mp4', 'rb')
    hug_rem = open('media/hug_rem.gif', 'rb')
    user_active = message.from_user.username
    if message.reply_to_message:
        user_passive = message.reply_to_message.from_user.username
        if user_active == 'Remedyv':
            bot.reply_to(message, f'{user_active} погладила {user_passive}')
            bot.send_animation(message.chat.id, hug)
        else:
            bot.reply_to(message, f'{user_active} погладил {user_passive}')
            bot.send_animation(message.chat.id, hug)


@bot.message_handler(commands=['invite'])
def pat(message):
    hug = open('media/taringa-anime.gif', 'rb')
    user_active = message.from_user.username
    if message.reply_to_message:
        user_passive = message.reply_to_message.from_user.username
        # if not user_passive:
        #     user_passive = 'haku'

        bot.reply_to(message, f'{user_active} зовет {user_passive} играть в гусей')
        bot.send_animation(message.chat.id, hug)
@bot.message_handler(commands=['wait'])
def pat(message):
    hug = open('media/cs.gif', 'rb')
    hug_remi = open('media/wait_rem.gif', 'rb')
    user_active = message.from_user.username
    if message.reply_to_message:

        user_passive = message.reply_to_message.from_user.username
        if user_active == 'Remedyv':

            bot.reply_to(message, f'{user_active} ждёт {user_passive} в Counter-Strike')
            bot.send_animation(message.chat.id, hug_remi)
        else:
            bot.reply_to(message, f'{user_active} ждёт {user_passive} в Counter-Strike')
            bot.send_animation(message.chat.id, hug)

@bot.message_handler(commands=['start'])

def entered_users(message):

    if message.from_user.username== None:
        bot.send_message(message.chat.id, 'Введите свой username')
    else:
        with Session.begin() as session:
            user_have = session.query(exists().where(User.id == message.from_user.id)).scalar()
            if not user_have:
                users_dict = dict(id = message.from_user.id, name = message.from_user.first_name, username = message.from_user.username)
                query = insert(User).values(users_dict)
                balance_dict = dict(id = message.from_user.id, balance = 100)
                query1 = insert(Eco).values(balance_dict)
                session.execute(query)
                session.execute(query1)
                session.commit()
                bot.send_message(message.chat.id, 'Вы зарегистрировались✅')

            else:
                bot.send_message(message.chat.id, 'Вы уже зарегались✅')

@bot.message_handler(commands=['coinflip'])

def bet(message):
    global user1
    user1 = message.from_user.id
    bot.reply_to(message, "Введите вашу ставку💰:")
    bot.register_next_step_handler(message, process_bet)

def process_bet(message):
    global user1
    if message.from_user.id != user1:
        bot.register_next_step_handler(message, process_bet)


    else:
        global bet_amount, new_balance
        bet_amount = message.text
        try:
            bet_amount = int(bet_amount)
            if bet_amount <= 0:
                bot.reply_to(message, 'ИДИ НАХУЙ без негатива\nВведите ставку:')
                bot.register_next_step_handler(message, process_bet)
                return
        except ValueError:
            bot.reply_to(message, 'Введи число, а не текст!!!')
            bot.register_next_step_handler(message, process_bet)
            return

        user1 = message.from_user.id
        with Session.begin() as session:
            query_balance = select(Eco.balance).select_from(Eco).where(Eco.id == user1)
            result = session.execute(query_balance).fetchone()
            balance_amount = result[0]

        if balance_amount < bet_amount:
            bot.reply_to(message, "У вас недостаточно средств")
            return
        else:
            new_balance = balance_amount - bet_amount
            query_update_balance = update(Eco).values(balance = new_balance).where(Eco.id == user1)
            session.execute(query_update_balance)
            session.commit()

            markup = types.InlineKeyboardMarkup(row_width=2)
            btn1 = types.InlineKeyboardButton('Орёл', callback_data='орёл')
            btn2 = types.InlineKeyboardButton('Новосиб', callback_data='новосиб')
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, "Выберите орёл или новосиб:", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data in ['орёл', 'новосиб'])
def process_coin_choice(call):
    global new_balance, bet_amount
    if call.from_user.id != user1:
        bot.register_next_step_handler(call.message, process_coin_choice)
    else:
        choice = call.data.lower()
        if choice not in ['орёл', 'новосиб']:
            bot.send_message(call.message.chat.id, "Пожалуйста, выберите орёл или новосиб.")
            return

        bot.delete_message(call.message.chat.id, call.message.message_id)
        result = random.choice(['орёл', 'новосиб'])

        if result == 'орёл':
            #img = open('media/coinflip_orel.gif', 'rb')
            vidos = open('media/or.mp4', 'rb')
            #sent_message = bot.send_animation(call.message.chat.id, img)
            sent_message = bot.send_video(call.message.chat.id, vidos)

            time.sleep(6)
        elif result == 'новосиб':
            #img = open('media/coinflip_nov.gif', 'rb')
            vidos = open('media/novasib.MP4', 'rb')
            #sent_message = bot.send_animation(call.message.chat.id, img)
            sent_message = bot.send_video(call.message.chat.id, vidos)

            time.sleep(6)


        if choice == result:
            win = 2*bet_amount
            bot.send_message(call.message.chat.id, f'{call.from_user.username}, Вы получили: <b>{win}</b>💰\nВы выбрали <b><i>{choice}</i></b>, результат: <b>{result}</b>.', parse_mode='html')
            with Session.begin() as session:
                new_balance += win
                query_update_balance = update(Eco).values(balance=new_balance).where(Eco.id == call.from_user.id)
                session.execute(query_update_balance)
                session.commit()

        else:
            bot.send_message(call.message.chat.id, f'{call.from_user.username}, Вы проебали: <b>{bet_amount}</b>💰\nВы выбрали <s><b><i>{choice}</i></b></s>, результат: <b>{result}</b>.', parse_mode='html')

        bot.delete_message(call.message.chat.id, sent_message.message_id)

@bot.message_handler(commands=['give'])
def process_give_command(message):
    # Проверяем, содержит ли сообщение аргументы для команды /give
    match = re.match(r'/give (@?\w+) (\d+)', message.text)
    if match:
        username = match.group(1)  # Имя пользователя
        amount = int(match.group(2))  # Сумма для передачи

        if username.startswith('@'):
            username = username[1:]

        with Session.begin() as session:
            user = session.query(User).filter(User.username == username).first()
            if user:
                sender_balance = session.query(Eco).filter(Eco.id == message.from_user.id).first()
                if sender_balance.balance >= amount:
                    sender_balance.balance -= amount
                    user_balance = session.query(Eco).filter(Eco.id == user.id).first()
                    user_balance.balance += amount
                    session.commit()
                    bot.reply_to(message, f"Вы успешно передали {amount}💰 пользователю {username}")
                else:
                    bot.reply_to(message, "У вас недостаточно средств для этой операции ❗️")
            else:
                bot.reply_to(message, f"Пользователь {username} не найден ❗️")
    else:
        bot.reply_to(message, "Используйте команду следующим образом: /give <username> <amount> ️❗️")


@bot.message_handler(commands=['door'])
def show_doors(message):
    global user_door
    user_door = message.from_user.id
    is_on_cooldown, remaining_time = check_command_cooldown(message.from_user.id)
    if is_on_cooldown:
        hours = remaining_time.seconds // 3600
        minutes = (remaining_time.seconds % 3600) // 60
        seconds = remaining_time.seconds % 60
        time_left_str = f"{hours}:{minutes}:{seconds}"

        bot.reply_to(message,
                     f"Вы уже использовали команду /door в последние 3 часа. Осталось времени: {time_left_str}🕑")
        return

    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton("Дверь 1", callback_data="door_1")
    button2 = types.InlineKeyboardButton("Дверь 2", callback_data="door_2")
    button3 = types.InlineKeyboardButton("Дверь 3", callback_data="door_3")
    markup.add(button1, button2, button3)

    with open('media/door.png', 'rb') as door_image:
        bot.send_photo(message.chat.id, door_image, caption="Какую дверь закрыли Remedyv с MoralFuck🚪", reply_markup=markup)

    update_last_command_time(message.from_user.id)


def check_command_cooldown(user_id):
    session = Session()
    try:
        user_log = session.query(UserLogi).filter_by(user_id=user_id, command='/door').order_by(UserLogi.date_time.desc()).first()

        if user_log:
            last_command_time = datetime.strptime(user_log.date_time, '%Y-%m-%d %H:%M:%S')  # Измените формат здесь
            time_since_last_command = datetime.now() - last_command_time
            if time_since_last_command < timedelta(hours=3):
                remaining_time = timedelta(hours=3) - time_since_last_command
                return True, remaining_time
            else:
                return False, None
        else:
            return False, None
    finally:
        session.close()


def update_last_command_time(user_id):
    with Session.begin() as session:
        new_log_entry = UserLogi(user_id=user_id, date_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), command='/door')
        session.add(new_log_entry)
        session.commit()
@bot.callback_query_handler(func=lambda call: call.data.startswith('door_'))
def open_door(call):
    if call.from_user.id != user_door:
        return
    else:
        bot.delete_message(call.message.chat.id, call.message.id)
        door_number = int(call.data.split('_')[1])

        coins = random.choice([50, 100, 150])

        with Session.begin() as session:
            user_id = call.from_user.id
            user_balance = session.query(Eco).filter(Eco.id == user_id).first()
            user_balance.balance += coins
            session.commit()

        bot.send_message(call.message.chat.id, f"Вы открыли 🚪Дверь {door_number} и нашли MoralFuck с Remedyv\nОни дали тебе {coins}💰 монеток, чтоб ты уже отъебался, без негатива.")


@bot.message_handler(commands=['balance'])
def check_balance(message):
    if len(message.text.split()) > 1:
        username = message.text.split()[1]
    else:
        username = None

    if username:
        if username.startswith('@'):
            username = username[1:]

        with Session.begin() as session:
            user = session.query(User).filter(User.username == username).first()
            if user:
                balance = session.query(Eco.balance).filter(Eco.id == user.id).scalar()
                bot.reply_to(message, f"Баланс пользователя {username}: {balance}💰")
            else:
                bot.reply_to(message, f"Пользователь {username} не найден.")
    else:
        with Session.begin() as session:
            balance = session.query(Eco.balance).filter(Eco.id == message.from_user.id).scalar()
            bot.reply_to(message, f"Ваш баланс: {balance}💰")

# bot.set_my_commands(
#     commands=[telebot.types.BotCommand('start', 'я сказала стартуем!'),
#                 telebot.types.BotCommand('help', 'ЭЭ помогите'),
#                 telebot.types.BotCommand('balance', 'безупречный баланс'),
#               telebot.types.BotCommand('coinflip', 'брось меня'),
#               telebot.types.BotCommand('who', 'кто ты по жизни'),
#               telebot.types.BotCommand('love @', 'любовь'),
#               telebot.types.BotCommand('door', 'осторожно, двери закрываются'),
#
#                 telebot.types.BotCommand('give', 'дай мне деньги'),
#                 telebot.types.BotCommand('give', 'дай мне деньги'),
                    #telebot.types.BotCommand('balance', 'безупречный баланс'),
        #               telebot.types.BotCommand('coinflip', 'брось меня'),
        #               telebot.types.BotCommand('who', 'кто ты по жизни'),
        #               telebot.types.BotCommand('love @', 'любовь'),
        #               telebot.types.BotCommand('door', 'осторожно, двери закрываются'),
        #
        #                 telebot.types.BotCommand('give', 'дай мне деньги'),
        #                 telebot.types.BotCommand('give', 'дай мне деньги'),


#               ],
#               scope=telebot.types.BotCommandScopeChat(-1002035354644)
#
#
#
# )
# @bot.message_handler(commands=['гладить'])
# def gladit(message):
#     bot.reply_to(message, 'заебись работает')

@bot.message_handler(commands=['love'])
def love_is(message):
    if len(message.text.split()) > 1:
        username = message.text.split()[1]
    else:
        bot.reply_to(message, "Используйте команду следующим образом: /love @username")
        return

    if username.startswith('@'):
        username = username[1:]

    with Session.begin() as session:
        user = session.query(User).filter(User.username == username).first()
        if user:
            bot.reply_to(message, f"❤️ {message.from_user.username} признается в любви {username} ❤️")
        else:
            bot.reply_to(message, f"Пользователь {username} не найден.")


# Обработчик команды /help
@bot.message_handler(commands=['help'])
def handle_help(message):
    help_text = "Доступные команды:\n"
    help_text += "/start - начать взаимодействие с ботом\n"
    help_text += "/coinflip - подбросить монетку\n"
    help_text += "/who - узнать кто ты по жизни\n"
    bot.send_message(message.chat.id, help_text)

# @bot.message_handler(commands=['who'])
#
# def who_i_am(message):
#     if len(message.text.split()) > 1:
#         username = message.text.split()[1]
#     else:
#         username = None
#
#     if username:
#         if username == '@Remedyv':
#             username = 'Remedyv'
#             bot.reply_to(message, f"Сегодня {username} - {random.choice(special_for_Remedyv)}")
#             return
#         if username.startswith('@'):
#             username = username[1:]
#
#         with Session.begin() as session:
#             user = session.query(User).filter(User.username == username).first()
#             if user:
#                 bot.reply_to(message, f"Сегодня {username} - {random.choice(banword)}")
#             else:
#                 name = session.query(User).filter(User.name == username).first()
#                 if name:
#                     bot.reply_to(message, f"Сегодня {name} - {random.choice(banword)}")
#                 else:
#                     bot.reply_to(message, f"Пользователь {username} не найден.")
#     else:
#         if message.from_user.id == 979795224:
#             bot.reply_to(message, f"Сегодня {message.from_user.username} - {random.choice(special_for_Remedyv)}")
#         else:
#             with Session.begin() as session:
#                 user = session.query(User).filter(User.username == message.from_user.username).first()
#                 if user != None:
#                     bot.reply_to(message, f"Сегодня {message.from_user.username} - {random.choice(banword)}")
#                 else:
#                     name = session.query(User).filter(User.name == message.from_user.first_name).first()
#                     if name:
#                         bot.reply_to(message, f"Сегодня {name} - {random.choice(banword)}")
#                     else:
#                         bot.reply_to(message, f"Пользователь {username} не найден.")



        # else:
        #     if not message.from_user.username:
        #         bot.reply_to(message, f"Сегодня {message.from_user.first_name} - {random.choice(banword)}")
        #     else:
        #         bot.reply_to(message, f"Сегодня {message.from_user.username} - {random.choice(banword)}")

# Обработчик всех текстовых сообщений в беседе




# @bot.message_handler(content_types=['text'])
#
# def check_word(message):
#     # if message.text.lower() == 'че' or message.text.lower() == 'чё' :
#     #     bot.send_message(message.chat.id,'а ни че нормально общайся')
#     if (message.text == '5 причин зайти на сервер ARUKU'):
#         markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         button1 = types.KeyboardButton('Тетрис с MoralFuck')
#         button2 = types.KeyboardButton('/coinflip')
#         button3 = types.KeyboardButton('Приватка с MoralFuck')
#         button4 = types.KeyboardButton('MoralFuck')
#         button5 = types.KeyboardButton('MoralFuck в 115-й')
#         markup2.add(button1,button2, button3, button4, button5)
#         bot.send_message(message.chat.id, 'Выбери причину', reply_markup=markup2)







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













# @bot.message_handler(chat_id=[-1002094586262], commands=['update'])
# def update_command(message):
# bot.set_my_commands(
#     commands=[
#     telebot.types.BotCommand('start', 'я сказала стартуем!'),
#                 telebot.types.BotCommand('help', 'ЭЭ помогите'),
#               telebot.types.BotCommand('balance', 'безупречный баланс'),
#               telebot.types.BotCommand('coinflip', 'брось меня'),
#               telebot.types.BotCommand('who', 'кто ты по жизни'),
#               telebot.types.BotCommand('love ', 'я люблю'),
#               telebot.types.BotCommand('door', 'осторожно, двери закрываются'),
#
#               telebot.types.BotCommand('give', 'дай мне деньги'),
#
#               telebot.types.BotCommand('hm', 'хммм'),
#               telebot.types.BotCommand('hug', 'обнять'),
#               telebot.types.BotCommand('nip','укусить'),
#               telebot.types.BotCommand('hit','ударить'),
#               telebot.types.BotCommand('f_ck', 'послать'),
#               telebot.types.BotCommand('wait','ждать'),
#
#               telebot.types.BotCommand('invite','позвать'),
#               telebot.types.BotCommand('pat', 'гладить'),
#                 telebot.types.BotCommand('kiss', 'поцеловать'),
#                 telebot.types.BotCommand('test', 'test')
#
#               ],
#               scope=telebot.types.BotCommandScopeChat(-1002094586262)
# )

#


# @bot.message_handler(chat_id=[-1002094586262], commands=['update'])
# def update_command(message):
#     bot.set_my_commands(
#     commands=[telebot.types.BotCommand('door', 'осторожно, двери закрываются')
#
#               ],
#               scope=telebot.types.BotCommandScopeChat(message.chat.id)



# telebot.types.BotCommand('coinflip', 'брось меня'),



# @bot.message_handler(chat_id=[-1002035354644], commands=['update'])
# def update_command(message):
#
#     bot.set_my_commands(
#     commands=[telebot.types.BotCommand('start', 'я сказала стартуем!'),
#               telebot.types.BotCommand('help', 'ЭЭ помогите'),
#               telebot.types.BotCommand('balance', 'безупречный баланс'),
#               telebot.types.BotCommand('coinflip', 'брось меня'),
#               telebot.types.BotCommand('who', 'кто ты по жизни'),
#               telebot.types.BotCommand('love', 'я люблю тебя'),
#               telebot.types.BotCommand('door', 'осторожно, двери закрываются'),
#               telebot.types.BotCommand('give', 'дай мне деньги')
#               ],
#               scope=telebot.types.BotCommandScopeChat(message.chat.id)
#
#
#
# )


# Запускаем бота
bot.polling(non_stop=True)