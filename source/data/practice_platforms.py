from .data_storage import get_storage


storage = get_storage()


def __get_data():
    return storage.knowledge_base.find_one({'name': 'practice_platforms'})


def get_topics():
    data = __get_data()
    return list(data['data'].keys()) + ['All']


def get_platforms(topic: str):
    data = __get_data()
    platforms = None
    topics = get_topics()
    if topic in topics:
        if topic == 'All':
            platforms = []
            for topic in topics[:-1]:
                platforms.extend(data['data'][topic])
        else:
            platforms = data['data'][topic]
    return platforms
