import telebot
from tg_bot import bot
hotelki=-1002094586262
durka=-1002035354644
@bot.message_handler(chat_id=[-1002094586262], commands=['update'])
def update_command(message):
    bot.set_my_commands(
    commands=[telebot.types.BotCommand('start', '� ������� ��������!'),
                telebot.types.BotCommand('help', '�� ��������'),
                telebot.types.BotCommand('balance', '����������� ������'),
              telebot.types.BotCommand('coinflip', '����� ����'),
              telebot.types.BotCommand('who', '��� �� �� �����'),
              telebot.types.BotCommand('love @', '� ����� ����'),
              telebot.types.BotCommand('door', '���������, ����� �����������'),

                telebot.types.BotCommand('give', '��� ��� ������'),
              telebot.types.BotCommand('��������', '?'),
              telebot.types.BotCommand('��', '?'),
              telebot.types.BotCommand('������', '?'),
              telebot.types.BotCommand('�������', '?'),
              telebot.types.BotCommand('�������', '?'),
              telebot.types.BotCommand('�������', '?'),
              telebot.types.BotCommand('�����', '?'),

              telebot.types.BotCommand('�������', '?'),
              telebot.types.BotCommand('�������', '?')

              ],
              scope=telebot.types.BotCommandScopeChat(-1002035354644)
)