from ._ui_symbols import *


def create_online_courses_view(topic, courses):
    list_of_courses = '\n'.join([
        f"{get_new_line_point_symbol()} [{course['title']}]({course['url']}) "
        f"by [{course['provider']}]({course['provider-url']}) "
        f"{generate_flag_symbol(course['language'])}"
        for course in courses
    ])
    return f'Here is the list of {topic} courses:\n' + list_of_courses
