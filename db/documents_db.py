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

def fetch_all_document_embeddings():
    """
    Fetch embeddings for all documents stored in the database.
    Returns a dictionary with document IDs as keys and embeddings as values.
    """
    db = get_db()  # Assuming get_db() is a function that returns a reference to the database
    documents = db.documents.find({})  # Assuming your documents are stored in a 'documents' collection
    
    embeddings = {}
    for doc in documents:
        # Assuming each document has an 'embedding' field with the embedding stored as a list
        # And an '_id' field used as the document ID
        embeddings[str(doc['_id'])] = np.array(doc['embedding'])
    return embeddings


### end ###
    
