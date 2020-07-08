from ._ui_symbols import *


def create_interview_view(topic, questions):
    text = f'Here is the list of questions for a {topic} interview:\n'
    return text + '\n'.join([
        f'{get_new_line_point_symbol()} {question["text"]}'
        for question in questions
    ])
