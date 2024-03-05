# RAG-SOTA/db/save_to_db.py
from .mongo_client import get_db
from .annotations_db import save_annotations
from .documents_db import save_document

def save_ocr_results_to_db(filename, text, annotations):
    """
    Save OCR results and annotations to the database.
    
    :param filename: The name of the file that was processed.
    :param text: The extracted text from the OCR process.
    :param annotations: The extracted annotations from the NER process.
    :return: None
    """
    db = get_db()
    # Save the document data first
    document_id = save_document(db, filename, text)
    if document_id:
        # If the document was saved successfully, save the annotations
        annotations_id = save_annotations(db, document_id, annotations)
        if annotations_id:
            print(f"Saved document and annotations for {filename} to the database.")
        else:
            print(f"Failed to save annotations for {filename}.")
    else:
        print(f"Failed to save document {filename} to the database.")

### end ###
