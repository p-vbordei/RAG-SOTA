# RAG-SOTA/db/documents_db.py
from datetime import datetime

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

### end ###
    
