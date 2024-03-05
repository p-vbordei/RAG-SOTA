# RAG-SOTA/pdf_parser/src/main.py
import argparse
from pdf_parser import parse_pdf
from ocr import apply_ocr_to_pdf
import os

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