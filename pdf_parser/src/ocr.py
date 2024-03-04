### src/ocr.py 
from PIL import Image
import pytesseract
import fitz  # PyMuPDF

def apply_ocr_to_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    for page_num, page in enumerate(doc):
        for img_index, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image = Image.open(BytesIO(image_bytes))
            text = pytesseract.image_to_string(image)
            print(f"OCR Text for image {img_index} on page {page_num}: {text}")
    doc.close()
### end ###