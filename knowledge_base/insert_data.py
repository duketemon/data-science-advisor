import os
import json
from pymongo import MongoClient


def insert_data(db, filename):
    collection = db.knowledge_base
    with open(f'data/{filename}.json') as f:
        data = json.load(f)
    collection.insert_one(data)


url = 'localhost'
username = 'defUser'
password = 'defPass'
client = MongoClient(url, username=username, password=password)
db = client['ds_advisor']

filenames = ['interview', 'courses', 'lectures', 'practice_platforms', 'essential_skills']
for filename in filenames:
    insert_data(db, filename)
