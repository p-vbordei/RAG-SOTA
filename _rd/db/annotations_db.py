# RAG-SOTA/db/annotations_db.py
from pymongo import MongoClient

def get_db():
    client = MongoClient("mongodb://localhost:27017/")  # Adjust the connection string as per your MongoDB setup
    db = client["ocr_documents_db"]  
    return db


def save_annotations(document_id, annotations):
    db = get_db()
    annotations_collection = db.annotations
    annotations_id = annotations_collection.insert_one({
        "documentId": document_id,
        "annotations": annotations
    }).inserted_id
    return annotations_id

def get_annotations(document_id):
    db = get_db()
    annotations_collection = db.annotations
    return annotations_collection.find_one({"documentId": document_id})

def update_annotations(annotation_id, annotations):
    db = get_db()
    annotations_collection = db.annotations
    result = annotations_collection.update_one(
        {"_id": annotation_id},
        {"$set": {"annotations": annotations}}
    )
    return result.modified_count

def delete_annotations(annotation_id):
    db = get_db()
    annotations_collection = db.annotations
    result = annotations_collection.delete_one({"_id": annotation_id})
    return result.deleted_count

### end ###
