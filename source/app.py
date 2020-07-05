import os
import telegram
from telegram.ext import Updater, CommandHandler

from handlers import *


def run_bot():
    token = os.getenv("TELEGRAM_TOKEN")
    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start_handler))
    dispatcher.add_handler(CommandHandler("courses", courses_handler))
    dispatcher.add_handler(CommandHandler("practice_platforms", practice_platforms_handler))
    dispatcher.add_handler(CommandHandler("essential_skills", essential_skills_handler))
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
