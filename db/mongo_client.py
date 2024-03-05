# RAG-SOTA/db/mongo_client.py
from pymongo import MongoClient
import os

def get_db():
    client = MongoClient(os.environ.get('MONGODB_URI'))
    db = client['ocr_documents_db']
    return db
### end ###