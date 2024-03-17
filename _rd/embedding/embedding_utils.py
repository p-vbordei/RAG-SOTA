# RAG-SOTA/embedding/embedding_utils.py

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
