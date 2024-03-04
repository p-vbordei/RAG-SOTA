# src/pdf_parser.py
import fitz  # PyMuPDF
import pdfplumber

def parse_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        full_text = ''
        for page in pdf.pages:
            full_text += page.extract_text() + "\n"
    print(full_text)

#### end ####