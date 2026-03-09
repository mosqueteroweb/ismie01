import re
import os

def test_split(filepath):
    print(f"\n--- {filepath} ---")
    with open(filepath, 'r') as f:
        content = f.read()

    parts = content.split("## Contenidos Básicos (Comunidad de Madrid)")
    if len(parts) < 2:
        return

    boe_text = parts[0]
    cm_text = parts[1]

    # Identify RAs. Sometimes they wrap lines before "Criterios de evaluación:"
    ras = list(re.finditer(r'(?m)^(\d+)\.\s+(.*?)\nCriterios de evaluación:', boe_text, re.DOTALL))
    if not ras:
        # Fallback if there are multiple newlines or spaces
        ras = list(re.finditer(r'(?m)^(\d+)\.\s+(.*?)Criterios de evaluación:', boe_text, re.DOTALL))

    print(f"Found {len(ras)} RAs.")

    cm_blocks = list(re.finditer(r'(?m)^([A-ZÁÉÍÓÚ][^\n\-\•]*?):\s*$', cm_text))
    print(f"Found {len(cm_blocks)} CM Blocks.")

    for i in range(min(len(ras), len(cm_blocks))):
        print(f"RA {i+1}: {ras[i].group(2).replace(chr(10), ' ').strip()[:50]}... <--> CM {i+1}: {cm_blocks[i].group(1)}")

for f in os.listdir('asir'):
    if f.endswith('.md'):
        test_split(f'asir/{f}')
