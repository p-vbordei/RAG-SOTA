# RAG-SOTA/ppdf_parser/src/pdf_parser.py
import pdfplumber
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)  # Set logging level to INFO

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

# python -m unittest tests/test_pdf_parser.py
# python src/main.py data/input/manual_utilizare_portal_onrc_recom.pdf

#### end ####
    