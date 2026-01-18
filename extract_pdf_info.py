from pypdf import PdfReader
import re

pdf_path = "modulos_por_ciclo/ifcs02_desarrollo_de_aplicaciones_multiplataforma.pdf"
reader = PdfReader(pdf_path)

print(f"Total pages: {len(reader.pages)}")

# Extract text from all pages and search for the module code
full_text = ""
for page in reader.pages:
    full_text += page.extract_text() + "\n"

# Search for the module code 0492
# The pattern might vary, but typically lists code, name, hours, ects.
# Let's look for the occurrence of "0492" and surrounding text.

matches = re.finditer(r".{0,100}0492.{0,100}", full_text, re.DOTALL)

print("--- Matches for 0492 ---")
for match in matches:
    print(match.group(0))
    print("-" * 20)

# Also search for "Proyecto de desarrollo" to find the row in the hours table
matches_name = re.finditer(r".{0,100}Proyecto de desarrollo.{0,100}", full_text, re.DOTALL)
print("--- Matches for Module Name ---")
for match in matches_name:
    print(match.group(0))
    print("-" * 20)
