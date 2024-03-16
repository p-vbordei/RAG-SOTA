# RAG-SOTA/pdf_parser/src/pdf_parser.py
import argparse
import os
from PIL import Image
import pytesseract
import fitz  # PyMuPDF
from io import BytesIO
# https://docs.llamaindex.ai/en/stable/module_guides/loading/simpledirectoryreader.html

# RAG-SOTA/ppdf_parser/src/pdf_parser.py
import pdfplumber
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)  # Set logging level to INFO




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
                try:a
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

    

def main():
    parser = argparse.ArgumentParser(description='PDF Parser')
    parser.add_argument('path', help='Path to the PDF file or directory to parse')
    args = parser.parse_args()

    if os.path.isdir(args.path):
        # If input is a directory, parse each PDF in it
        for filename in os.listdir(args.path):
            if filename.endswith('.pdf'):
                pdf_path = os.path.join(args.path, filename)
                print(f"Parsing {pdf_path}...")
                parse_pdf(pdf_path)
                # Optionally apply OCR
                apply_ocr_to_pdf(pdf_path)
    elif os.path.isfile(args.path) and args.path.endswith('.pdf'):
        # Single PDF file
        print(f"Parsing {args.path}...")
        parse_pdf(args.path)
        # Optionally apply OCR
        apply_ocr_to_pdf(args.path)
    else:
        print("Invalid path or file format. Please provide a PDF file or directory containing PDFs.")

if __name__ == "__main__":
    main()


#### end ####
