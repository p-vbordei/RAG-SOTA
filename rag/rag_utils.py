# RAG-SOTA/rag/rag_utils.py
"""
Provides utility functions supporting RAG operations, such as document scoring and preprocessing.

Functions:
calculate_document_scores(documents: List[Document], query: str) -> Dict[Document, float]

Purpose: Calculate relevance scores for each document relative to the query.
Module Dependencies: May use embedding/embedding_utils.py for document and query embeddings.
preprocess_documents(documents: List[Document]) -> List[Document]

Purpose: Preprocess documents to optimize them for the RAG model.
Description: Similar to query preprocessing but applied to document text.

"""





### end ###
