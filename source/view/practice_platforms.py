from ._ui_symbols import *


def create_practice_platforms_view(platforms: [str]):
    list_of_courses = '\n'.join([
        f"{get_new_line_point_symbol()} [{platform['title']}]({platform['url']}). "
        f"{platform['description']} "
        f"{'/'.join([generate_flag_symbol(lang) for lang in platform['languages']])}"
        for platform in platforms
    ])
    return f'Here is the list of platforms to practice your skills:\n' + list_of_courses
