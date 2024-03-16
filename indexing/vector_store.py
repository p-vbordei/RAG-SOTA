# RAG-SOTA/indexing/vector_store.py
import numpy as np
from pymongo import MongoClient
import os

# Assuming an external vector database or library, e.g., FAISS or Annoy, for the vector store.
# For simplicity, let's consider a FAISS Index as an example. Ensure you have FAISS installed.
import faiss

def get_db():
    client = MongoClient("mongodb://localhost:27017/")  # Adjust the connection string as per your MongoDB setup
    db = client["ocr_documents_db"]  
    return db

# Placeholder for the FAISS index. In a real application, this should be loaded from persistent storage or initialized properly.
dimension = 768  # Example dimension, adjust based on your actual embeddings
faiss_index = faiss.IndexFlatL2(dimension)

def add_document_embedding(document_id: str, embedding: np.array):
    """
    Add a document's embedding to the vector store.
    """
    # Convert numpy array to FAISS's format if necessary
    embedding_faiss = np.ascontiguousarray(embedding.reshape(1, -1))
    faiss_index.add(embedding_faiss)
    
    # Save document_id mapping in MongoDB for retrieval later
    db = get_db()
    db.vector_mappings.insert_one({"document_id": document_id, "index_position": faiss_index.ntotal - 1})

def query_embeddings(query_embedding: np.array, top_k: int = 5) -> list:
    """
    Query the vector store with a query embedding to find the most similar document embeddings.
    """
    query_embedding_faiss = np.ascontiguousarray(query_embedding.reshape(1, -1))
    distances, indices = faiss_index.search(query_embedding_faiss, top_k)
    
    # Retrieve document_ids from MongoDB using indices
    db = get_db()
    document_ids = []
    for index in indices[0]:
        mapping = db.vector_mappings.find_one({"index_position": int(index)})
        if mapping:
            document_ids.append(mapping['document_id'])
    
    return document_ids



### end ###
