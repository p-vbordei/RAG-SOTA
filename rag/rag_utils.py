# RAG-SOTA/rag/rag_utils.py
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def preprocess_text(text: str) -> str:
    """
    Preprocesses text for NLP tasks by performing several normalization steps:
    - Lowercasing the text to ensure case consistency.
    - Removing punctuation to reduce noise in text analysis.
    - Stripping extra whitespace for uniformity.
    - Optionally, more preprocessing steps like stemming, lemmatization, or stopword removal can be added.

    :param text: The original text string.
    :return: The preprocessed text string.
    """
    # Lowercase the text
    text = text.lower()

    # Remove punctuation using a regular expression
    text = re.sub(r'[^\w\s]', '', text)

    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()

    return text

def calculate_cosine_similarity(vector_a: np.ndarray, vector_b: np.ndarray) -> float:
    """
    Calculates the cosine similarity between two vectors.
    :param vector_a: First vector.
    :param vector_b: Second vector.
    :return: Cosine similarity score.
    """
    return cosine_similarity(vector_a.reshape(1, -1), vector_b.reshape(1, -1))[0][0]

### end ###
