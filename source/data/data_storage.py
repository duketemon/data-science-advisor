import os
from pymongo import MongoClient


client = MongoClient(
    os.getenv('DATA_STORAGE_URL'),
    username=os.getenv('DATA_STORAGE_USERNAME'),
    password=os.getenv('DATA_STORAGE_PASSWORD')
)
storage = client[os.getenv('DATA_STORAGE_NAME')]


def get_storage():
    return storage
