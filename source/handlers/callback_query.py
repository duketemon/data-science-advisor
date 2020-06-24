import telegram
from data.online_courses import get_courses
from view.online_courses import create_online_courses_view


def callback_query_handler(update, context):
    request = update.callback_query.data
    if request.startswith('online_courses'):
        topic = ' '.join(request.split(' ')[1:])
        courses = get_courses(topic)
        view = create_online_courses_view(topic, courses)
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=view,
            parse_mode=telegram.ParseMode.MARKDOWN
        )
