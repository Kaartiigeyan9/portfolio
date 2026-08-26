import re
from pathlib import Path
p = Path('E:/portfolio/resume_text.txt')
text = p.read_text(encoding='utf-8')
# Find emails and urls
emails = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', text)
urls = re.findall(r'https?://[\w./%\-?=&@#]+', text)
# Filter common social links
linkedin = next((u for u in urls if 'linkedin' in u.lower()), None)
github = next((u for u in urls if 'github' in u.lower()), None)
# Build candidate summary lines: take lines with letters and length>30
lines = [ln.strip() for ln in text.splitlines() if len(ln.strip())>30 and re.search('[A-Za-z]', ln)]
summary = '\n'.join(lines[:6])
print('EMAILS:', emails)
print('LINKEDIN:', linkedin)
print('GITHUB:', github)
print('SUMMARY_PREVIEW:')
print(summary)
