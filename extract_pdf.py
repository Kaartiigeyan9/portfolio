from pathlib import Path
p = Path(r"E:/portfolio/Kaartiigeyan_resume.pdf")
out = Path(r"E:/portfolio/resume_text.txt")
text = ""

# Try PyPDF2 first
try:
    import PyPDF2
    reader = PyPDF2.PdfReader(str(p))
    parts = []
    for page in reader.pages:
        parts.append(page.extract_text() or "")
    text = "\n\n".join(parts)
except Exception as e1:
    # Fallback to pdfminer
    try:
        from pdfminer.high_level import extract_text
        text = extract_text(str(p))
    except Exception as e2:
        text = f"ERROR_PARSING: PyPDF2_error={e1!r}; pdfminer_error={e2!r}"

out.write_text(text, encoding='utf-8')
print(f"WROTE {out}")
print("---BEGIN---")
print(text[:4000])
print("---END---")
