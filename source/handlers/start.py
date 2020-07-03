from view.help import get_help_view


def start_handler(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=get_help_view(),
        disable_web_page_preview=True
    )
