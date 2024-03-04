### src/ocr.py 

from PIL import Image
import pytesseract
import fitz  # PyMuPDF
from io import BytesIO

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'
  # Update this path (brew --prefix tesseract)

def apply_ocr_to_pdf(pdf_path, lang='eng+ron')):
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
# python src/main.py data/input/manual_utilizare_portal_onrc_recom.pdf
# python src/main.py data/input/Fascinant.pdf
### end ###