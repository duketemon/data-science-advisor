from data.essential_skills import get_titles
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from utils.ui import build_menu


def essential_skills_handler(update, context):
    titles = get_titles()
    button_list = [
        InlineKeyboardButton(text=position, callback_data=f"essential_skills {position}")
        for position in titles
    ]
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Choose a job title: ',
        reply_markup=reply_markup,
        one_time_keyboard=True
    )
