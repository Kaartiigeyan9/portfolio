import re
from pathlib import Path
p = Path(r"E:/portfolio/Kaartiigeyan_resume.pdf")
out = Path(r"E:/portfolio/resume_text.txt")
raw = p.read_bytes()
# Find runs of printable ascii (including common punctuation)
parts = re.findall(rb'[\x20-\x7E]{4,}', raw)
# Decode and join, attempt to insert newlines at common keywords
decoded = "\n\n".join(part.decode('latin-1', errors='replace') for part in parts)
# Try to normalize sequences like ") (" where words are separate
decoded = decoded.replace(')(', ') (')
# Write out
out.write_text(decoded, encoding='utf-8')
print(f'WROTE {out}')
print(decoded[:4000])
