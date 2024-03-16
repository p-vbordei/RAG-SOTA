# RAG-SOTA/rag/answer_generator.py
from typing import List
import numpy as np
from sentence_transformers import SentenceTransformer

# Load a pre-trained model
model = SentenceTransformer('all-MiniLM-L6-v2')

def generate_document_embeddings(documents: List[str]) -> List[np.ndarray]:
    """
    Generates embeddings for a list of document texts.
    :param documents: List of document texts.
    :return: List of embeddings as numpy arrays.
    """
    # Generate embeddings for all documents
    embeddings = model.encode(documents, convert_to_numpy=True)
    return embeddings

def generate_query_embedding(query: str) -> np.ndarray:
    """
    Generates an embedding for the query text.
    :param query: Query text.
    :return: Query embedding as a numpy array.
    """
    # Generate embedding for the query
    query_embedding = model.encode(query, convert_to_numpy=True)
    return query_embedding


def find_relevant_documents(query_embedding: np.ndarray, document_embeddings: List[np.ndarray]) -> List[int]:
    """
    Finds document indices most relevant to the query based on cosine similarity.
    :param query_embedding: Embedding of the query.
    :param document_embeddings: List of document embeddings.
    :return: Indices of the top relevant documents.
    """
    similarities = [rag_utils.calculate_cosine_similarity(query_embedding, doc_emb) for doc_emb in document_embeddings]
    return sorted(range(len(similarities)), key=lambda i: similarities[i], reverse=True)[:5]

def generate_answer(documents: List[str], query: str) -> str:
    """
    Generates an answer from a list of documents based on a query.
    :param documents: List of document texts.
    :param query: Query text.
    :return: Generated answer.
    """
    document_embeddings = generate_document_embeddings(documents)
    query_embedding = generate_query_embedding(query)
    relevant_doc_indices = find_relevant_documents(query_embedding, document_embeddings)
    
    # Simplified answer generation by aggregating relevant document texts
    answer = ' '.join([documents[i] for i in relevant_doc_indices])
    return answer

### end ###
