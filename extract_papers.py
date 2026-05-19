import pdfplumber
import os
import glob
import re

papers_dir = "papers/9702"
qp_out = "BaofojiaoGuide/data/extracted/papers"
ms_out = "BaofojiaoGuide/data/extracted/ms"
os.makedirs(qp_out, exist_ok=True)
os.makedirs(ms_out, exist_ok=True)

# Extract syllabus first
syllabus_pdf = "data/syllabuses/9702_syllabus_2025_2027.pdf"
if os.path.exists(syllabus_pdf):
    syllabus_out = "BaofojiaoGuide/data/extracted/9702_syllabus.txt"
    print(f"Extracting syllabus: {syllabus_pdf}")
    with pdfplumber.open(syllabus_pdf) as pdf:
        text = ""
        for i, page in enumerate(pdf.pages):
            t = page.extract_text() or ""
            text += f"\n=== PAGE {i+1} ===\n{t}"
    with open(syllabus_out, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"  -> {syllabus_out} ({len(text)} chars)")

# Extract all Paper 4 QP PDFs
qp_pattern = os.path.join(papers_dir, "**/*_qp_4?.pdf")
qp_files = sorted(glob.glob(qp_pattern, recursive=True))
print(f"\nFound {len(qp_files)} QP files for Paper 4")

for pdf_path in qp_files:
    basename = os.path.basename(pdf_path)
    txt_name = basename.replace(".pdf", ".txt")
    out_path = os.path.join(qp_out, txt_name)
    if os.path.exists(out_path):
        print(f"  SKIP {basename} (already extracted)")
        continue
    print(f"  Extracting {basename}...")
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = ""
            for i, page in enumerate(pdf.pages):
                t = page.extract_text() or ""
                text += f"\n=== PAGE {i+1} ===\n{t}"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"    -> {out_path} ({len(text)} chars)")
    except Exception as e:
        print(f"    ERROR: {e}")

# Extract all Paper 4 MS PDFs
ms_pattern = os.path.join(papers_dir, "**/*_ms_4?.pdf")
ms_files = sorted(glob.glob(ms_pattern, recursive=True))
print(f"\nFound {len(ms_files)} MS files for Paper 4")

for pdf_path in ms_files:
    basename = os.path.basename(pdf_path)
    txt_name = basename.replace(".pdf", ".txt")
    out_path = os.path.join(ms_out, txt_name)
    if os.path.exists(out_path):
        print(f"  SKIP {basename} (already extracted)")
        continue
    print(f"  Extracting {basename}...")
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = ""
            for i, page in enumerate(pdf.pages):
                t = page.extract_text() or ""
                text += f"\n=== PAGE {i+1} ===\n{t}"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"    -> {out_path} ({len(text)} chars)")
    except Exception as e:
        print(f"    ERROR: {e}")

print("\nDone!")
