# RAG-SOTA/db/documents_db.py
from datetime import datetime
from pymongo import MongoClient
import numpy as np

def get_db():
    client = MongoClient("mongodb://localhost:27017/")  # Adjust the connection string as per your MongoDB setup
    db = client["ocr_documents_db"] 
    return db

def save_document(db, filename, text):
    """
    Save the document with the extracted text to the database.

    :param db: The database connection object.
    :param filename: The name of the file being saved.
    :param text: The OCR extracted text from the file.
    :return: The ID of the saved document or None if saving failed.
    """
    documents_collection = db.documents
    try:
        document_id = documents_collection.insert_one({
            "filename": filename,
            "uploadDate": datetime.utcnow(),
            "text": text
        }).inserted_id
        return document_id
    except Exception as e:
        print(f"An error occurred while saving the document: {e}")
        return None


def fetch_all_document_embeddings():
    """
    Fetch embeddings for all documents stored in the database.
    Returns a dictionary with document IDs as keys and embeddings as values.
    """
    try:
        db = get_db()
        documents = db.documents.find({})

        embeddings = {}
        for doc in documents:
            if 'embedding' in doc:
                embeddings[str(doc['_id'])] = np.array(doc['embedding'])
            else:
                print(f"Document {doc['_id']} does not have an embedding.")
        return embeddings
    except Exception as e:
        print(f"An error occurred while fetching document embeddings: {e}")
        return {}
### end ###
    
