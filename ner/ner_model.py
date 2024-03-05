# RAG-SOTA/ner/ner_model.py

from span_marker import SpanMarkerModel
from db.annotations_db import save_annotations

# Load the SpanMarker NER model
model = SpanMarkerModel.from_pretrained("tomaarsen/span-marker-mbert-base-multinerd")

def predict_entities(text):
    """
    Uses the loaded NER model to predict entities within the provided text.
    """
    return model.predict(text)

def extract_and_save_entities(document_id, text):
    """
    Extracts entities from the provided text using the NER model and saves them to the database.
    """
    # Extract entities
    predictions = predict_entities(text)
    
    # Save entities to the database
    annotations_id = save_annotations(document_id, predictions)
    
    return annotations_id

### end ###

# Example usage
# This is for demonstration purposes and would normally be invoked within an application flow
"""
if __name__ == "__main__":
    text_to_analyze = "Amelia Earhart flew her single engine Lockheed Vega 5B across the Atlantic to Paris."
    document_id = "some_unique_identifier_for_the_document"
    
    # Extract and save entities to the database
    annotations_id = extract_and_save_entities(document_id, text_to_analyze)
    print(f"Entities have been extracted and saved with annotation ID: {annotations_id}")
"""
