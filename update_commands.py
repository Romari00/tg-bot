import telebot
from tg_bot import bot
hotelki=-1002094586262
durka=-1002035354644
@bot.message_handler(chat_id=[-1002094586262], commands=['update'])
def update_command(message):
    bot.set_my_commands(
    commands=[telebot.types.BotCommand('start', 'я сказала стартуем!'),
                telebot.types.BotCommand('help', 'ЭЭ помогите'),
                telebot.types.BotCommand('balance', 'безупречный баланс'),
              telebot.types.BotCommand('coinflip', 'брось меня'),
              telebot.types.BotCommand('who', 'кто ты по жизни'),
              telebot.types.BotCommand('love @', 'я люблю тебя'),
              telebot.types.BotCommand('door', 'осторожно, двери закрываются'),

                telebot.types.BotCommand('give', 'дай мне деньги'),
              telebot.types.BotCommand('целовать', '?'),
              telebot.types.BotCommand('эм', '?'),
              telebot.types.BotCommand('обнять', '?'),
              telebot.types.BotCommand('укусить', '?'),
              telebot.types.BotCommand('ударить', '?'),
              telebot.types.BotCommand('послать', '?'),
              telebot.types.BotCommand('ждать', '?'),

              telebot.types.BotCommand('позвать', '?'),
              telebot.types.BotCommand('гладить', '?')

              ],
              scope=telebot.types.BotCommandScopeChat(-1002035354644)
)