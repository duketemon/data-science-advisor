from view.help import get_help_view


def help_handler(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=get_help_view()
    )
