import fitz  # PyMuPDF
from pathlib import Path

def parse_txt(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def parse_pdf(file_path: str) -> str:
    doc = fitz.open(file_path)
    text = []
    for page in doc:
        text.append(page.get_text())
    return "\n".join(text)

def extract_text(file_path: str) -> str:
    suffix = Path(file_path).suffix.lower()

    if suffix == ".txt":
        return parse_txt(file_path)
    if suffix == ".pdf":
        return parse_pdf(file_path)

    raise ValueError(f"Unsupported file format: {suffix}")