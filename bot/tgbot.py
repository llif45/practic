import telebot
from telebot import types
from telebot.types import ReplyKeyboardMarkup

bot = telebot.TeleBot("7584058639:AAFFFVngdNtF6DFpaBInQmUykBCZNVVkr6s")
# Импорт библиотеки Бота для телеграмма и его токен

@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id, 'Что умеет этот бот?\n\nЭтот бот умеет складывать "статьи" которые нарушил тот или иной член экипажа в игре Space Station 14 (За основу взят сервер Space Stories) ')
# После команды /info бот выдаёт краткую информацию о себе
@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, <b>{message.from_user.first_name}</b>. думаю описание ты прочитал, приступим!\nЯ нахожусь в разработке, потому - могу выдавать сбои.\nВыбери статью которую нарушил член экипажа.', parse_mode='html')
# После команды /start бот отправляет приветственное сообщение с именем пользователя
    markup = ReplyKeyboardMarkup()
    bt1 = types.KeyboardButton('Лёгкие нарушения (1xx)')
    bt2 = types.KeyboardButton('Средние нарушения (2xx)')
    bt3 = types.KeyboardButton('Тяжкие нарушения (3xx)')
    bt4 = types.KeyboardButton('Особо тяжкие нарушения (4xx)')
    bt5 = types.KeyboardButton('Критические нарушения (5xx)')
    btend = types.KeyboardButton('Итоговый срок')
    markup.row(bt1,bt2)
    markup.row(bt3,bt4)
    markup.add(bt5)
    markup.add(btend)
    # Кнопки выбора "Тяжести" преступления
    bot.send_message(message.chat.id, "Выбери тяжесть преступления", reply_markup=markup)
    bot.register_next_step_handler(message, choice)
def choice(message):
    markup = ReplyKeyboardMarkup()
    if message.text == 'Лёгкие нарушения (1xx)':
        bt100 = types.KeyboardButton('100')
        bt101 = types.KeyboardButton('101')
        bt102 = types.KeyboardButton('102')
        bt103 = types.KeyboardButton('103')
        bt104 = types.KeyboardButton('104')
        bt105 = types.KeyboardButton('105')
        bt106 = types.KeyboardButton('106')
        bt107 = types.KeyboardButton('107')
        bt109 = types.KeyboardButton('109')
        markup.row(bt100,bt101,bt102,bt103,bt104,bt105,bt106)
        markup.add(bt107,bt109)
    elif message.text == 'Средние нарушения (2xx)':
        bot.send_message(message.chat.id, "Проверка на жизнь 2")
    elif message.text == 'Тяжкие нарушения (3xx)':
        bot.send_message(message.chat.id, "Проверка на жизнь 3")
    elif message.text == 'Особо тяжкие нарушения (4xx)':
        bot.send_message(message.chat.id, "Проверка на жизнь 4")
    elif message.text == 'Критические нарушения (5xx)':
        bot.send_message(message.chat.id, "Проверка на жизнь 5")
    elif message.text == 'Итоговый срок':
        bot.send_message(message.chat.id, "Итоговая проверка")
    else:
        bot.send_message(message.chat.id, "Выбери статью, дурында!")
        return
bot.polling(non_stop=True)