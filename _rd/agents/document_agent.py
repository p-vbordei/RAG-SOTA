# RAG-SOTA/agents/document_agent.py
from typing import Dict, List
from rag.document_retriever import retrieve_documents
from rag.answer_generator import generate_answer
from db.documents_db import update_document

def process_query(document_ids: List[str], query: str) -> str:
    """
    Processes a query related to specific documents and generates a response.
    
    :param document_ids: List of IDs of documents to manage.
    :param query: The user's query as a string.
    :return: A response generated based on information from the assigned documents.
    """
    # Retrieve relevant documents
    documents = retrieve_documents(query, document_ids=document_ids)
    
    # Generate an answer based on the retrieved documents
    answer = generate_answer(documents, query)
    
    return answer

def update_document_knowledge(document_ids: List[str], document_updates: Dict[str, Dict]):
    """
    Updates the knowledge base with new or modified information related to specified documents.
    
    :param document_ids: List of document IDs that the updates apply to.
    :param document_updates: A dictionary with document IDs as keys and updated information as values.
    """
    for doc_id, updates in document_updates.items():
        if doc_id in document_ids:
            update_document(doc_id, updates)

### end ###
