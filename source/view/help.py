from ._ui_symbols import get_new_line_point_symbol


def get_help_view():
    return '\n'.join([
        "Hey! I'm a Data Science Advisor. I can",
        f"{get_new_line_point_symbol()} Recommend online courses - /online_courses",
        "If you have any ideas, please visit the repository of the project."
    ])
