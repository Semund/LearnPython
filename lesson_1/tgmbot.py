import logging

from telegram.ext import Updater, CommandHandler
from settings import TG_BOT_API_KEY

logging.basicConfig(filename="bot.log", level=logging.INFO)


def greeting_user(update, contact):
    update.message.reply_text(f'Привет, {update["message"].from_user.first_name}! Ты вызвал команду '
                              f'{update["message"].text}')


def start_echobot():
    echobot = Updater(TG_BOT_API_KEY, use_context=True)

    dp = echobot.dispatcher
    dp.add_handler(CommandHandler('start', greeting_user))

    logging.info('Бот приступил к работе')
    echobot.start_polling()
    echobot.idle()


if __name__ == '__main__':
    start_echobot()
