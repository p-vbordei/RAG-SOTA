# RAG-SOTA/rag/document_retriever.py
"""
document_retriever.py Overview and Functions
The document_retriever.py module is essential for implementing the Retrieval-Augmented Generation (RAG) approach in your project. It interacts closely with both the indexing/ and db/ modules to retrieve relevant documents from your database based on user queries. Here's a detailed breakdown of its responsibilities and the functions it will contain:

1. retrieve_documents(query: str, top_k: int = 5) -> List[Document]
Purpose: To retrieve the top k documents relevant to the given query.
Description: This function will use semantic search techniques to find documents that are most semantically related to the user's query. It leverages embeddings stored in the indexing/ module to perform this search.
Parameters:
query: A string representing the user's query.
top_k: An integer specifying the number of top relevant documents to retrieve. Default is 5.
Returns: A list of Document objects, each containing information about the retrieved documents, such as their IDs, titles, text, and possibly scores indicating relevance to the query.
Module Dependencies: Depends on indexing/semantic_search.py for searching documents based on semantic similarity and db/documents_db.py for fetching document details from the database.

2. preprocess_query(query: str) -> str
Purpose: To preprocess the query for semantic search.
Description: Applies necessary preprocessing steps to the query text to improve the quality of the search. This may include lowercasing, removing punctuation, and other text normalization steps.
Parameters:
query: The raw query string from the user.
Returns: A preprocessed, clean version of the query string.
Module Dependencies: None directly, but follows best practices in text preprocessing for NLP tasks.

3. rank_documents(documents: List[Document], query: str) -> List[Document]
Purpose: To rank the retrieved documents based on relevance to the query.
Description: After retrieving a set of documents, this function ranks them based on their relevance to the query. This could involve computing similarity scores between the query embeddings and document embeddings, or using additional criteria like document freshness or authority.
Parameters:
documents: A list of Document objects retrieved based on semantic search.
query: The preprocessed query string.
Returns: A list of the same Document objects, but sorted based on their relevance to the query.
Module Dependencies: May depend on embedding/embedding_utils.py for generating or accessing embeddings and calculating similarity scores.

"""

from typing import List
from db.documents_db import fetch_document_details
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
