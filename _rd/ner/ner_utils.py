# RAG-SOTA/ner/ner_utils.py

import re

def preprocess_text(text):
    """
    Preprocess the text before it is fed into the NER model.
    This could include steps like removing special characters, lowercasing, etc.
    """
    # Example: Remove special characters and multiple spaces
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def postprocess_entities(entities):
    """
    Postprocess the entities returned by the NER model.
    This could include filtering low-confidence entities, merging entities, etc.
    """
    # Example: Filter out entities with a confidence score below a threshold
    threshold = 0.75
    filtered_entities = [entity for entity in entities if entity['score'] >= threshold]
    return filtered_entities

def format_entities_for_storage(entities):
    """
    Format the entities in a way that is suitable for storage in the database.
    """
    # Example: Convert entities to a dictionary format, removing unwanted information
    formatted_entities = [{
        'text': entity['span'],
        'type': entity['label'],
        'start': entity['char_start_index'],
        'end': entity['char_end_index']
    } for entity in entities]
    return formatted_entities

### end ###
