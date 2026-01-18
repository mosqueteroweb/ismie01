from pypdf import PdfReader
import re

pdf_path = "modulos_por_ciclo/ifcs02_desarrollo_de_aplicaciones_multiplataforma.pdf"
reader = PdfReader(pdf_path)

full_text = ""
for page in reader.pages:
    full_text += page.extract_text() + "\n"

print("--- Table Extract ---")
# Let's try to print the lines that look like table rows (contain numbers)
lines = full_text.split('\n')
for line in lines:
    if re.search(r'\d+', line):
        print(line)
