# tests/test_pdf_parser.py

import unittest
from src.pdf_parser import parse_pdf

class TestPDFParser(unittest.TestCase):
    def test_parse_pdf(self):
        # Path to your test PDF
        test_pdf_path = 'tests/data/test_document.pdf'
        
        # Expected text in test_document.pdf
        expected_text = "This is a test document."
        
        # Use your parse_pdf function to extract text
        extracted_text = parse_pdf(test_pdf_path)
        
        # Remove any trailing whitespace for a fair comparison
        extracted_text = extracted_text.strip()
        
        # Assert that the extracted text matches the expected text
        self.assertEqual(extracted_text, expected_text)

if __name__ == '__main__':
    unittest.main()

#### end ####