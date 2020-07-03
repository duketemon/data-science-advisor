from .data_storage import get_storage


storage = get_storage()
data = storage.knowledge_base.find_one({'name': 'essential_skills'})


def get_titles():
    return data['titles']


def get_essential_skills(title: str):
    essential_skills = data['data'][title]['skills']
    return essential_skills
