import pdfplumber
import re
from backend.config import PAGE_THRESHOLD


def load_pdf_text(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            if i >= PAGE_THRESHOLD:
                break  # stop reading more pages

            t = page.extract_text()
            if t:
                t = re.sub(r"\s+", " ", t)
                text += t + "\n"

    return text
