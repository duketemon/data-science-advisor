import telegram
from data.practice_platforms import get_platforms
from view.practice_platforms import create_practice_platforms_view


def practice_platforms_handler(update, context):
    platforms = get_platforms()
    view = create_practice_platforms_view(platforms)
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=view,
        parse_mode=telegram.ParseMode.MARKDOWN
    )
