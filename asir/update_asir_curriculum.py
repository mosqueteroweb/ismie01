import os
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_ras(boe_text):
    ras = []
    parts = re.split(r'\n(?=\d+\.\s+)', '\n' + boe_text)
    parts = [p.strip() for p in parts if p.strip()]

    for p in parts:
        if re.match(r'^\d+\.\s+', p):
            ras.append(p)

    return ras

def extract_cm_blocks(cm_text):
    # Regex for lines that are uppercase starts, end with colon, not preceded by dash
    pattern = r'(?m)^([A-ZÁÉÍÓÚ][^\n\-\•]*?):\s*$'
    matches = list(re.finditer(pattern, cm_text))

    blocks = []
    if not matches:
        blocks.append(("General", cm_text))
        return blocks

    # Check if there is preamble text before the first match
    if matches and matches[0].start() > 0:
        preamble = cm_text[:matches[0].start()].strip()
        if preamble:
            blocks.append(("Introducción", preamble))

    for i in range(len(matches)):
        start = matches[i].start()
        end = matches[i+1].start() if i + 1 < len(matches) else len(cm_text)

        title = matches[i].group(1).strip()
        content = cm_text[start:end].strip()
        blocks.append((title, content))

    return blocks

def process_file(filepath):
    print(f"\nProcessing {filepath}...")
    with open(filepath, 'r') as f:
        content = f.read()

    if "## Contenidos Básicos (Comunidad de Madrid)" not in content:
        print("Could not find ## Contenidos Básicos")
        return

    # Get Module Name
    mod_match = re.search(r'# Módulo (\w+) - (.*?)\n', content)
    if not mod_match:
        print("Could not parse module code/name")
        return
    mod_code = mod_match.group(1)
    mod_name = mod_match.group(2)

    parts = content.split("## Contenidos Básicos (Comunidad de Madrid)")
    header_boe = parts[0].split("Resultados de aprendizaje y criterios de evaluación.")

    if len(header_boe) < 2:
        print("Could not find Resultados de aprendizaje")
        return

    boe_text = header_boe[1].strip()
    cm_text = parts[1].strip()

    ras = extract_ras(boe_text)
    cm_blocks = extract_cm_blocks(cm_text)

    if not ras or not cm_blocks:
        print("RAs or CM blocks empty")
        return

    vectorizer = TfidfVectorizer(stop_words=None)
    ra_vectors = vectorizer.fit_transform(ras)

    ra_to_cm = {i: [] for i in range(len(ras))}

    for cm_title, cm_content in cm_blocks:
        cm_vec = vectorizer.transform([cm_content])
        sims = cosine_similarity(cm_vec, ra_vectors)[0]
        best_match_idx = sims.argmax()
        ra_to_cm[best_match_idx].append((cm_title, cm_content))

    # Reconstruct document
    new_content = f"# Módulo {mod_code} - {mod_name}\n\n"

    for i, ra_text in enumerate(ras):
        lines = ra_text.split('\n')
        ra_heading = lines[0].strip()
        ra_rest = '\n'.join(lines[1:]).strip()

        new_content += f"## {ra_heading}\n\n"
        if ra_rest:
            new_content += ra_rest + "\n\n"

        if ra_to_cm[i]:
            new_content += "### Contenidos Básicos Relacionados (CM):\n\n"
            for cm_title, cm_content in ra_to_cm[i]:
                new_content += cm_content + "\n\n"

    with open(filepath, 'w') as f:
        f.write(new_content)

for f in os.listdir('asir'):
    if f.endswith('.md'):
        process_file(f'asir/{f}')
