from .data_storage import get_storage


storage = get_storage()


def __get_data():
    return storage.knowledge_base.find_one({'name': 'lectures'})


def get_topics():
    data = __get_data()
    return list(data['data'].keys())


def get_lectures(topic: str):
    data = __get_data()
    lectures = data['data'][topic]
    return lectures
