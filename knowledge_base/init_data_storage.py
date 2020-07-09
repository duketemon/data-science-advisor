import os
import json
from pymongo import MongoClient


def insert_data(db, filename):
    collection = db.knowledge_base
    with open(filename) as f:
        data = json.load(f)
    collection.insert_one(data)


client = MongoClient(
    os.getenv('DATA_STORAGE_URL'), 
    username=os.getenv('DATA_STORAGE_USERNAME'),
    password=os.getenv('DATA_STORAGE_PASSWORD')
)
db = client[os.getenv('DATA_STORAGE_DB_NAME')]

filenames = os.listdir('data')
for filename in filenames:
    insert_data(db, f'data/{filename}')
