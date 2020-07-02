from data.practice_platforms import get_topics
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from utils.ui import build_menu


def practice_platforms_handler(update, context):
    topics = get_topics()
    button_list = [
        InlineKeyboardButton(text=topic, callback_data=f"practice_platforms {topic}")
        for topic in topics
    ]
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Choose a topic: ',
        reply_markup=reply_markup,
        one_time_keyboard=True
    )
