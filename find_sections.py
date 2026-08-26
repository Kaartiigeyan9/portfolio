from pathlib import Path
import re
p = Path('E:/portfolio/resume_text.txt')
text = p.read_text(encoding='utf-8')
keys = ['education','projects','skills','experience','objective','summary','contact','certifications','achievements','leadership']
lines = text.splitlines()
found = {}
for i,l in enumerate(lines):
    for k in keys:
        if k.lower() in l.lower():
            found.setdefault(k,[]).append((i+1,l.strip()))
for k in keys:
    print('==',k.upper(),'==')
    for occ in found.get(k,[])[:10]:
        print(occ)
    print()
