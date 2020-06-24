from .data_storage import get_storage


storage = get_storage()
data = storage.knowledge_base.find_one({'name': 'online_courses'})


def get_topics():
    return data['topics'] + ['All']


def get_courses(topic: str):
    courses = None
    topics = get_topics()
    if topic in topics:
        if topic == 'All':
            courses = []
            for topic in topics[:-1]:
                courses.extend(data['courses'][topic])
        else:
            courses = data['courses'][topic]
    return courses
