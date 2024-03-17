# RAG-SOTA/pdf_parser/pdf_parser.py
import argparse
import os
from PIL import Image
import pytesseract
import fitz  # PyMuPDF
from io import BytesIO
# https://docs.llamaindex.ai/en/stable/module_guides/loading/simpledirectoryreader.html
# https://github.com/run-llama/llama_parse/blob/main/examples/demo_advanced.ipynb


# RAG-SOTA/ppdf_parser/src/pdf_parser.py
import pdfplumber
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)  # Set logging level to INFO


import os
from llama_index.core import SimpleDirectoryReader
import logging

def process_document(file_path):
    """
    Process a single document, applying OCR if it's a PDF that requires it.
    
    :param file_path: The path to the document.
    :return: The text content extracted from the document.
    """
    if file_path.endswith('.pdf'):
        if needs_ocr(file_path):
            apply_ocr_to_pdf(file_path)
        return parse_pdf(file_path)
    else:
        # Add your processing logic for other document types here
        pass  # Placeholder for other document processing



# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'
  # Update this path (brew --prefix tesseract)

def apply_ocr_to_pdf(pdf_path, lang='eng+ron'):
    doc = fitz.open(pdf_path)
    for page_num, page in enumerate(doc):
        for img_index, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image = Image.open(BytesIO(image_bytes))
            text = pytesseract.image_to_string(image, lang=lang)
            print(f"OCR Text for image {img_index} on page {page_num} [{lang}]: {text}")
    doc.close()



def needs_ocr(pdf_path):
    """
    Determine if OCR needs to be performed on the PDF file.

    :param pdf_path: The path to the PDF file.
    :return: True if OCR is needed, False otherwise.
    """
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages):
                try:
                    # Extract text from the page
                    page_text = page.extract_text()
                    # Check if page text is empty
                    if not page_text:
                        return True  # OCR is needed if page text is empty
                except Exception as page_error:
                    logging.warning(f"Error processing page {page_num + 1} of {pdf_path}: {page_error}")
        return False  # OCR is not needed if all pages have text
    except Exception as pdf_error:
        logging.error(f"Error processing {pdf_path}: {pdf_error}")
        return False  # Assume OCR is not needed in case of any error



def parse_pdf(pdf_path):
    """
    Parse the text content from a PDF file.

    :param pdf_path: The path to the PDF file.
    :return: The extracted text content as a string, or None if an error occurs.
    """
    try:
        with pdfplumber.open(pdf_path) as pdf:
            full_text = ''
            for page_num, page in enumerate(pdf.pages):
                try:
                    page_text = page.extract_text()
                    if page_text:
                        full_text += page_text + "\n"
                except Exception as page_error:
                    logging.warning(f"Error processing page {page_num + 1} of {pdf_path}: {page_error}")
            return full_text
    except Exception as pdf_error:
        logging.error(f"Error processing {pdf_path}: {pdf_error}")
        return None
    

def parse_documents_from_path_with_llama_index(path):
    """
    Parse documents from a given path using Llama Index's Simple Directory Reader. 
    Applies OCR to PDFs if necessary.
    
    :param path: The path to the directory containing documents or to a single document.
    :return: A list containing the extracted text content from each document, or None if an error occurs.
    """
    try:
        text_contents = []
        if os.path.isdir(path):
            # Use Simple Directory Reader to iterate through each file in the directory
            reader = SimpleDirectoryReader(path, recursive=True)
            for file_path in reader.file_paths:
                print(f"Processing {file_path}...")
                text_content = process_document(file_path)
                if text_content:
                    text_contents.append(text_content)
        elif os.path.isfile(path):
            # Single file processing
            print(f"Processing {path}...")
            text_content = process_document(path)
            if text_content:
                text_contents.append(text_content)
        else:
            print("Invalid path or file format. Please provide a valid file or directory path.")
            return None
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return None
    
    return text_contents

# python -m unittest tests/test_pdf_parser.py
# python src/main.py data/input/manual_utilizare_portal_onrc_recom.pdf


#### end ####
