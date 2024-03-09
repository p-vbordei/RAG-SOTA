# RAG-SOTA/indexing/vector_store.py
"""

Manages the vector store index, where document embeddings are stored and queried for semantic search.

Functions:
add_document_embedding(document_id: str, embedding: np.array)

Purpose: Add a document's embedding to the vector store.
Description: Stores the embedding vector associated with a document ID in the vector store for later retrieval.
Module Dependencies: May use an in-house implementation or external libraries designed for efficient vector search, such as FAISS or Annoy.
query_embeddings(query_embedding: np.array, top_k: int = 5) -> List[str]

Purpose: Query the vector store with a query embedding to find the most similar document embeddings.
Description: Returns the IDs of the top k most similar documents based on their embeddings.
Module Dependencies: Similar to add_document_embedding, relies on vector search technologies.

"""


import numpy as np
from pymongo import MongoClient
import os

# Assuming an external vector database or library, e.g., FAISS or Annoy, for the vector store.
# For simplicity, let's consider a FAISS Index as an example. Ensure you have FAISS installed.
import faiss

# Connect to MongoDB
def get_db():
    client = MongoClient(os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/'))
    return client.ocr_documents_db

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
