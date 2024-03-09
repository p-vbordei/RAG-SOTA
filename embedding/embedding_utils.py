# RAG-SOTA/embedding/embedding_utils.py
"""
This module will provide functionalities related to handling document embeddings, crucial for the semantic search and retrieval processes.

Functions:
generate_embeddings(text: str) -> np.array

Purpose: Generate embeddings for a given piece of text, which could be a query or document content.
Description: Uses the chosen embedding model to convert text into a vector representation.
Module Dependencies: Might rely on external libraries or APIs like OpenAIEmbedding or similar services for embedding generation.
calculate_similarity(embedding1: np.array, embedding2: np.array) -> float

Purpose: Calculate the similarity between two embeddings.
Description: Computes the cosine similarity (or other relevant metric) between two embedding vectors.
Module Dependencies: Primarily mathematical operations, might use numpy or similar libraries for calculations.

"""

import numpy as np
# Assuming an external library for embeddings, e.g., Hugging Face's Transformers
from transformers import AutoModel, AutoTokenizer

model_name = "sentence-transformers/all-MiniLM-L6-v2"  # Example model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

def generate_embeddings(text: str) -> np.array:
    """
    Generate embeddings for a given piece of text.
    """
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
    outputs = model(**inputs)
    embeddings = outputs.last_hidden_state.mean(dim=1).detach().numpy()
    return embeddings

def calculate_similarity(embedding1: np.array, embedding2: np.array) -> float:
    """
    Calculate the cosine similarity between two embeddings.
    """
    similarity = np.dot(embedding1, embedding2) / (np.linalg.norm(embedding1) * np.linalg.norm(embedding2))
    return similarity




### end ###
