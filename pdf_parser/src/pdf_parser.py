# src/pdf_parser.py
import pdfplumber

def parse_pdf(pdf_path):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            full_text = ''
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:  # Check if page_text is not None
                    full_text += page_text + "\n"
            return full_text
    except Exception as e:
        print(f"Error processing {pdf_path}: {e}")
        return None


#### end ####