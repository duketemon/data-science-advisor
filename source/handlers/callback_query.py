import telegram

from data.courses import get_courses
from view.courses import create_courses_view

from data.lectures import get_lectures
from view.lectures import create_lectures_view

from data.practice_platforms import get_platforms
from view.practice_platforms import create_practice_platforms_view

from data.essential_skills import get_essential_skills
from view.essential_skills import create_essential_skills_view


DEFAULT_SETTINGS = {
    'parse_mode': telegram.ParseMode.MARKDOWN,
    'disable_web_page_preview': True
}


def __send_view(update, context, view):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=view,
        **DEFAULT_SETTINGS
    )


def callback_query_handler(update, context):
    request = update.callback_query.data
    if request.startswith('courses'):
        topic = ' '.join(request.split(' ')[1:])
        courses = get_courses(topic)
        view = create_courses_view(topic, courses)
        __send_view(update, context, view)
    elif request.startswith('lectures'):
        topic = ' '.join(request.split(' ')[1:])
        lectures = get_lectures(topic)
        view = create_lectures_view(topic, lectures)
        __send_view(update, context, view)
    elif request.startswith('practice_platforms'):
        topic = ' '.join(request.split(' ')[1:])
        platforms = get_platforms(topic)
        view = create_practice_platforms_view(topic, platforms)
        __send_view(update, context, view)
    elif request.startswith('essential_skills'):
        title = ' '.join(request.split(' ')[1:])
        essential_skills = get_essential_skills(title)
        view = create_essential_skills_view(title, essential_skills)
        __send_view(update, context, view)
    else:
        print(f'"{request}" not implemented in the {__name__}.py file')
