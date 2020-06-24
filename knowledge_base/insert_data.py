import os
import json
from pymongo import MongoClient



def insert_online_courses_data(db):
    collection = db.knowledge_base
    with open('online_courses.json') as f:
        data = json.load(f)
    collection.insert_one(data)


url = 'localhost'
username = 'defUser'
password = 'defPass'
client = MongoClient(url, username=username, password=password)

    # os.getenv('DATA_STORAGE_URL'), 
    # username=os.getenv('DATA_STORAGE_USERNAME'), 
    # password=os.getenv('DATA_STORAGE_PASSWORD')
# )
db = client['ds_advisor']
insert_online_courses_data(db)
