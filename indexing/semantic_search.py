# RAG-SOTA/indexing/semantic_search.py
import numpy as np
from typing import List
from db.documents_db import fetch_all_document_embeddings
from embedding.embedding_utils import calculate_similarity
from pymongo import MongoClient

def search_documents(query_embedding: np.array, top_k: int = 5) -> List[dict]:
    """
    Perform a semantic search to retrieve the top k relevant documents based on a query embedding.
    
    :param query_embedding: Embedding of the user's query as a numpy array.
    :param top_k: The number of top relevant documents to retrieve.
    :return: A list of dictionaries, each representing a document and its relevance score.
    """
    # Fetch embeddings for all documents in the database
    document_embeddings = fetch_all_document_embeddings()
    
    # Calculate similarity scores between the query embedding and each document embedding
    similarities = []
    for doc_id, doc_embedding in document_embeddings.items():
        similarity = calculate_similarity(query_embedding, doc_embedding)
        similarities.append({'document_id': doc_id, 'similarity': similarity})
    
    # Sort documents based on their similarity scores in descending order
    sorted_docs = sorted(similarities, key=lambda x: x['similarity'], reverse=True)
    
    # Retrieve the top k documents
    top_documents = sorted_docs[:top_k]
    
    # Optionally, fetch more details for the top documents from the database
    top_documents_details = [fetch_document_details(doc['document_id']) for doc in top_documents]
    
    return top_documents_details



def fetch_document_details(document_id: str) -> dict:
    """
    Fetch and return detailed information about a document given its ID.
    """
    client = MongoClient('mongodb://localhost:27017/')
    db = client['ocr_documents_db']
    document = db.documents.find_one({"_id": document_id})
    
    if not document:
        return {"error": "Document not found."}
    
    # Optionally, enrich document details with annotations or additional metadata
    annotations = db.annotations.find_one({"documentId": document_id})
    if annotations:
        document['annotations'] = annotations['annotations']
    
    return document

### end ###
