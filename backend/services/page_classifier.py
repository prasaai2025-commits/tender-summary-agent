from PyPDF2 import PdfReader
from backend.config import PAGE_THRESHOLD


def classify_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    pages = len(reader.pages)
    return {
        "pages": pages,
        "mode": "NORMAL" if pages < PAGE_THRESHOLD else "HEAVY"
    }

