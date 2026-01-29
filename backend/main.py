from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os, shutil

# ✅ Services imports (ABSOLUTE – Render safe)
from backend.services.pdf_loader import load_pdf_text
from backend.services.llm_formatter import format_summary
from backend.services.pdf_generator import generate_pdf

from backend.services.identity import extract_identity
from backend.services.dates import extract_dates
from backend.services.technical import extract_technical
from backend.services.eligibility import extract_eligibility
from backend.services.finance import extract_finance
from backend.services.penalties import extract_penalties

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, "..", "frontend")
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

app.mount("/outputs", StaticFiles(directory=OUTPUT_DIR), name="outputs")


@app.get("/", response_class=HTMLResponse)
def home():
    with open(os.path.join(FRONTEND_DIR, "index.html"), "r", encoding="utf-8") as f:
        return f.read()


@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    path = os.path.join(UPLOAD_DIR, file.filename)
    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename}


@app.post("/generate-pdf")
def generate(filename: str):
    pdf_path = os.path.join(UPLOAD_DIR, filename)

    text = load_pdf_text(pdf_path)

    summary = format_summary(
        extract_identity(text),
        extract_dates(text),
        extract_technical(text),
        extract_eligibility(text),
        extract_finance(text),
        extract_penalties(text),
        filename
    )

    output_path = os.path.join(OUTPUT_DIR, "Tender_Summary.pdf")
    generate_pdf(summary, output_path)

    return {"download": "/outputs/Tender_Summary.pdf"}
