import logging

import settings
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


logging.basicConfig(filename="bot.log", level=logging.INFO)


def greeting_user(update, context):
    update.message.reply_text(f'Привет, {update.message.from_user.first_name}! Ты вызвал команду '
                              f'{update.message.text}')


def send_echo_message(update, context):
    message = update.message.text
    update.message.reply_text(message)


def adding_bot_handlers(dispatcher):
    dispatcher.add_handler(CommandHandler('start', greeting_user))
    dispatcher.add_handler(MessageHandler(Filters.text, send_echo_message))


def start_echobot():
    echobot = Updater(settings.TG_BOT_API_KEY, use_context=True)

    adding_bot_handlers(echobot.dispatcher)

    logging.info('Бот приступил к работе')
    echobot.start_polling()
    echobot.idle()


if __name__ == '__main__':
    start_echobot()
