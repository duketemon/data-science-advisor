from ._ui_symbols import *


def create_essential_skills_view(title: str, skills: [str]):
    options_list = '\n'.join([
        f"{get_new_line_point_symbol()} {skill}"
        for skill in skills
    ])
    return f'Here is the list of essential skills for {title} position:\n' + options_list
