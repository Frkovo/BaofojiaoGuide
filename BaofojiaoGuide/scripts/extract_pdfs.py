import os
import pdfplumber
import re

PAPERS_DIR = "E:/Dev/BaofojiaoGuide/papers/9231"
OUT_PAPERS = "E:/Dev/BaofojiaoGuide/BaofojiaoGuide/data/extracted/papers"
OUT_MS = "E:/Dev/BaofojiaoGuide/BaofojiaoGuide/data/extracted/ms"

def extract_text(pdf_path):
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                t = page.extract_text()
                if t:
                    text += t + "\n"
        return text
    except Exception as e:
        return f"[ERROR: {e}]"

def process_pdfs():
    for root, dirs, files in os.walk(PAPERS_DIR):
        for fname in files:
            if not fname.endswith(".pdf"):
                continue
            path = os.path.join(root, fname)
            # Determine if QP or MS
            if "_ms_" in fname:
                out_dir = OUT_MS
            else:
                out_dir = OUT_PAPERS
            out_name = fname.replace(".pdf", ".txt")
            out_path = os.path.join(out_dir, out_name)
            if os.path.exists(out_path):
                print(f"SKIP {fname}")
                continue
            text = extract_text(path)
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(text)
            size = len(text)
            print(f"OK   {fname} ({size} chars)")

if __name__ == "__main__":
    process_pdfs()
