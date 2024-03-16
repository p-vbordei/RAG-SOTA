# RAG-SOTA/interface/streamlit_app.py
import sys


import sys
from pathlib import Path

# Get the absolute path of the project root (RAG-SOTA directory)
project_root = Path(__file__).parent.parent.absolute()
print(sys.path)
# Add the project root to the Python path
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

print("after append")
print(sys.path)
print(project_root)
# Now you can import your local modules
from db.mongo_client import get_db

import streamlit as st
from db.save_to_db import save_ocr_results_to_db
from rag.document_retriever import retrieve_documents
from rag.answer_generator import generate_answer
from pdf_parser.pdf_parser_main import parse_pdf
from pdf_parser.ocr import apply_ocr_to_pdf


from typing import List
from indexing.semantic_search import fetch_document_details
from rag.document_retriever import retrieve_documents
from rag.answer_generator import generate_answer


# Placeholder functions for OCR and PDF parsing, ensure to replace with your actual implementations
def parse_pdf_and_ocr(file_path):
    text = parse_pdf(file_path)  # Assume this function returns text from PDF
    annotations = apply_ocr_to_pdf(file_path)  # Assume this function returns annotations from OCR
    return text, annotations

def upload_documents():
    uploaded_files = st.file_uploader("Choose PDF or Word documents", accept_multiple_files=True, type=['pdf', 'docx'])
    if uploaded_files is not None:
        for uploaded_file in uploaded_files:
            # Assume a temporary file path or handle the file in memory
            file_path = f"/path/to/uploaded/files/{uploaded_file.name}"
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            text, annotations = parse_pdf_and_ocr(file_path)
            save_ocr_results_to_db(uploaded_file.name, text, annotations)

def enter_query():
    query = st.text_input("Enter your query here:")
    return query

def process_query(query: str) -> str:
    """
    Processes a query against the document base and generates a response.
    
    :param query: The user's query as a string.
    :return: A string containing the generated answer.
    """
    # Retrieve relevant documents based on the query
    document_ids = retrieve_documents(query, top_k=5)  # Assume this function returns a list of document IDs
    
    # Fetch document details for the retrieved document IDs
    documents = [fetch_document_details(doc_id) for doc_id in document_ids]
    
    # Generate an answer based on the retrieved documents
    answer = generate_answer(documents, query)
    
    return answer


def display_response(response):
    st.write(response)

def main():
    st.title("RAG-SOTA Document Query Application")
    upload_documents()
    query = enter_query()
    if query:
        response = process_query(query)
        display_response(response)

if __name__ == "__main__":
    main()



### end ###
