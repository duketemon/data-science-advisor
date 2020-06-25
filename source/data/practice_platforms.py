from .data_storage import get_storage


storage = get_storage()
data = storage.knowledge_base.find_one({'name': 'practice_platforms'})


def get_platforms():
    return data['platforms']
