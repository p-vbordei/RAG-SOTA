# pdf_parser/src/pdf_parser.py
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

# python -m unittest tests/test_pdf_parser.py
# python src/main.py data/input/manual_utilizare_portal_onrc_recom.pdf

#### end ####