from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os, shutil

import pdf_loader
import identity
import dates
import technical
import eligibility
import finance
import penalties
import llm_formatter
import pdf_generator

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, "..", "tender-summary-frontend")
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

    text = pdf_loader.load_pdf_text(pdf_path)

    summary = llm_formatter.format_summary(
        identity.extract_identity(text),
        dates.extract_dates(text),
        technical.extract_technical(text),
        eligibility.extract_eligibility(text),
        finance.extract_finance(text),
        penalties.extract_penalties(text),
        filename
    )

    out = os.path.join(OUTPUT_DIR, "Tender_Summary.pdf")
    pdf_generator.generate_pdf(summary, out)

    return {
        "download": "/outputs/Tender_Summary.pdf"
    }
