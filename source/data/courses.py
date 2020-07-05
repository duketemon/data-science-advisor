from .data_storage import get_storage


storage = get_storage()


def __get_data():
    return storage.knowledge_base.find_one({'name': 'courses'})


def get_topics():
    data = __get_data()
    return list(data['data'].keys())


def get_courses(topic: str):
    data = __get_data()
    courses = data['data'][topic]
    return courses
