# RAG-SOTA/agents/top_level_agent.py
from typing import List
from agents.document_agent import process_query as document_query_processor
from indexing.semantic_search import search_documents

def orchestrate_query_processing(query: str) -> str:
    """
    Orchestrates the entire query processing pipeline, delegating tasks to document agents or directly handling
    queries for a comprehensive response.
    
    :param query: User's query as a string.
    :return: A comprehensive answer synthesized from relevant information sources.
    """
    # Determine the most relevant documents for the query
    document_ids = determine_relevant_documents(query)
    
    # Collect responses from the relevant document agents
    responses = [document_query_processor(doc_id, query) for doc_id in document_ids]
    
    # Combine the responses into a single, coherent answer
    answer = combine_responses(responses)
    
    return answer

def determine_relevant_documents(query: str) -> List[str]:
    """
    Analyzes a query to route it to the most relevant document agents, determining which documents should be consulted.
    
    :param query: The query to analyze.
    :return: A list of document IDs deemed most relevant to the query.
    """
    # Utilize semantic search to identify relevant document IDs
    document_ids = search_documents(query, top_k=5)
    
    return document_ids

def combine_responses(responses: List[str]) -> str:
    """
    Synthesizes a single, coherent answer from multiple responses.
    
    :param responses: List of responses from various document agents.
    :return: A synthesized, comprehensive answer.
    """
    # Placeholder for response synthesis logic
    if responses:
        return " ".join(responses)
    else:
        return "I'm sorry, I couldn't find information related to your question."


### end ###
