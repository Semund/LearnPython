"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import datetime
import logging
import ephem

import settings

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}


def greet_user(update, context):
    update.message.reply_text(f'Привет, {update.message.from_user.first_name}! Ты вызвал команду '
                              f'{update.message.text}')


def talk_to_me(update, context):
    message = update.message.text
    update.message.reply_text(message)


def get_planetary_position(update, context):
    planet_name = update.message.text.split()[-1].capitalize()

    if hasattr(ephem, planet_name):
        constellation = ephem.constellation(getattr(ephem, planet_name)(ephem.now()))[-1]
        message = f'{planet_name} находится в созвездии {constellation}'
    else:
        message = 'Я не знаю такого объекта'

    update.message.reply_text(message)


def adding_bot_handlers(dispatcher):
    dispatcher.add_handler(CommandHandler('start', greet_user))
    dispatcher.add_handler(CommandHandler('planet', get_planetary_position))
    dispatcher.add_handler(MessageHandler(Filters.text, talk_to_me))


def main():
    mybot = Updater(settings.TG_BOT_API_KEY, use_context=True)

    adding_bot_handlers(mybot.dispatcher)

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
