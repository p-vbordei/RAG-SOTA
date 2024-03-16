# RAG-SOTA/rag/document_retriever.py


from typing import List
from indexing.semantic_search import fetch_document_details
from embedding.embedding_utils import generate_embeddings, calculate_similarity
from indexing.semantic_search import search_documents

def preprocess_query(query: str) -> str:
    """
    Preprocess the query for semantic search.
    This may include lowercasing, removing punctuation, and other text normalization steps.
    """
    # Example preprocessing steps
    query = query.lower().strip()
    # Add more preprocessing steps as needed
    return query

def retrieve_documents(query: str, top_k: int = 5) -> List[dict]:
    """
    Retrieve the top k documents relevant to the given query.
    """
    preprocessed_query = preprocess_query(query)
    query_embedding = generate_embeddings(preprocessed_query)
    document_ids = search_documents(query_embedding, top_k)
    documents = [fetch_document_details(doc_id) for doc_id in document_ids]
    return rank_documents(documents, query_embedding)

def rank_documents(documents: List[dict], query_embedding: np.array) -> List[dict]:
    """
    Rank the retrieved documents based on relevance to the query.
    """
    for doc in documents:
        doc_embedding = generate_embeddings(doc['text'])
        doc['similarity'] = calculate_similarity(query_embedding, doc_embedding)
    ranked_documents = sorted(documents, key=lambda x: x['similarity'], reverse=True)
    return ranked_documents




### end ###
