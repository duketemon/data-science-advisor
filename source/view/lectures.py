from ._ui_symbols import *


def create_lectures_view(topic, courses):
    text = f'Here is the list of {topic} lectures:\n'

    for course in courses:
        provider_info = [
            f"[{provider['name']}]({provider['url']}) "
            for provider in course['providers']
        ]
        text += f"{get_new_line_point_symbol()} [{course['title']}]({course['url']}) by " +\
                " ".join(provider_info) + f"{generate_flag_symbol(course['language'])}\n"
    return text
