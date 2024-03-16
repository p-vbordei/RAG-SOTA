# RAG-SOTA/db/mongo_client.py
from pymongo import MongoClient
import os

def get_db():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['ocr_documents_db']
    return db

### end ###
