from .data_storage import get_storage


storage = get_storage()
data = storage.knowledge_base.find_one({'name': 'practice_platforms'})


def get_topics():
    return data['topics'] + ['All']


def get_platforms(topic: str):
    platforms = None
    topics = get_topics()
    if topic in topics:
        if topic == 'All':
            platforms = []
            for topic in topics[:-1]:
                platforms.extend(data['platforms'][topic])
        else:
            platforms = data['platforms'][topic]
    return platforms
