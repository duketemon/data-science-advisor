import telegram

from data.online_courses import get_courses
from view.online_courses import create_online_courses_view

from data.practice_platforms import get_platforms
from view.practice_platforms import create_practice_platforms_view

from data.essential_skills import get_essential_skills
from view.essential_skills import create_essential_skills_view


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
    elif request.startswith('practice_platforms'):
        topic = ' '.join(request.split(' ')[1:])
        platforms = get_platforms(topic)
        view = create_practice_platforms_view(topic, platforms)
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=view,
            parse_mode=telegram.ParseMode.MARKDOWN
        )
    elif request.startswith('essential_skills'):
        title = ' '.join(request.split(' ')[1:])
        essential_skills = get_essential_skills(title)
        view = create_essential_skills_view(title, essential_skills)
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=view,
            parse_mode=telegram.ParseMode.MARKDOWN
        )
