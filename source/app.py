import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from handlers import *


def run_bot():
    token = '1099491551:AAGayElAv5o3i91P2D3tMPQC9sdJi37OEJM'
    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start_handler))
    dispatcher.add_handler(CommandHandler("online_courses", online_courses_handler))
    dispatcher.add_handler(CommandHandler("help", help_handler))
    dispatcher.add_handler(telegram.ext.CallbackQueryHandler(callback_query_handler))
    # dispatcher.add_handler(MessageHandler(Filters.text, next_move_handler))
    dispatcher.add_error_handler(error_handler)

    # Start the Bot
    updater.start_polling()

    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    print('Service started...')
    updater.idle()


run_bot()
