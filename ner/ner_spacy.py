# RAG-SOTA/ner/new_spacy.py
import spacy
from db.annotations_db import save_annotations

# Load SpaCy's NER model
nlp = spacy.load("en_core_web_sm")  # Consider using a model that best fits your data

def predict_entities_spacy(text):
    """
    Uses SpaCy's NER model to predict entities within the provided text.
    """
    doc = nlp(text)
    entities = [{'text': ent.text, 'type': ent.label_, 'start': ent.start_char, 'end': ent.end_char} for ent in doc.ents]
    return entities

def extract_and_save_entities_spacy(document_id, text):
    """
    Extracts entities from the provided text using SpaCy's NER model and saves them to the database.
    """
    # Extract entities
    predictions = predict_entities_spacy(text)
    
    # Save entities to the database
    annotations_id = save_annotations(document_id, predictions)
    
    return annotations_id

### end ###