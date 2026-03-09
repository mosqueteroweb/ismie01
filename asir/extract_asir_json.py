import pypdf
import re
import os
import json

def extract_boe_data(filepath):
    reader = pypdf.PdfReader(filepath)
    text = ''
    for p in reader.pages:
        text += p.extract_text() + '\n'

    # Split text by "Módulo Profesional:" to avoid regex matching across different modules
    module_blocks = text.split("Módulo Profesional:")

    boe_data = {}
    for block in module_blocks[1:]: # Skip the first element which is text before the first module
        # Basic extractions within the block
        name_match = re.search(r'^\s*(.*?)\s*\n', block)
        if not name_match:
            continue
        mod_name = name_match.group(1).strip()

        code_match = re.search(r'Código:\s*(\w+)', block, re.IGNORECASE)
        if not code_match:
            continue
        mod_code = code_match.group(1).strip()

        ects_match = re.search(r'Equivalencia en créditos ECTS:\s*(\d+)', block, re.IGNORECASE)
        mod_ects = ects_match.group(1) if ects_match else ""

        hours_match = re.search(r'Duración:\s*(\d+)\s*horas', block, re.IGNORECASE)
        mod_hours = hours_match.group(1) if hours_match else ""

        # We only want "Resultados de aprendizaje y criterios de evaluación." until "Duración:" or "Contenidos básicos:"
        ra_start = block.find('Resultados de aprendizaje y criterios de evaluación.')
        if ra_start == -1:
            ra_start = block.find('Resultados de aprendizaje y Criterios de evaluación.')
        if ra_start == -1:
            ra_start = block.find('Resultados de aprendizaje')

        if ra_start != -1:
            ra_text = block[ra_start:]
        else:
            ra_text = block

        # Cut off at Duración or Contenidos básicos
        end_cut = ra_text.find('Duración:')
        if end_cut == -1:
            end_cut = ra_text.find('Contenidos básicos:')

        if end_cut != -1:
            ra_text = ra_text[:end_cut]

        # Parse RAs and CEs
        learning_results = []
        current_ra = None

        # Split by lines or paragraphs
        lines = ra_text.split('\n')
        for line in lines:
            line = line.strip()
            if not line:
                continue

            # Regex for "1. Text" or "1.Text"
            ra_match = re.match(r'^(\d+)\.\s*(.+)', line)
            if ra_match:
                if current_ra:
                    learning_results.append(current_ra)
                current_ra = {
                    "id": ra_match.group(1),
                    "description": ra_match.group(2),
                    "evaluation_criteria": []
                }
            # Regex for criteria "a) Text"
            elif re.match(r'^[a-z]\)\s+', line) and current_ra:
                current_ra['evaluation_criteria'].append(line)
            # Append continuation of criteria or RA description
            elif current_ra and not line.startswith("Resultados") and not line.startswith("Criterios"):
                if len(current_ra['evaluation_criteria']) > 0:
                    # Continuation of a criteria
                    current_ra['evaluation_criteria'][-1] += " " + line
                else:
                    # Continuation of RA description
                    current_ra['description'] += " " + line

        if current_ra:
            learning_results.append(current_ra)

        boe_data[mod_code] = {
            'name': mod_name,
            'code': mod_code,
            'hours': mod_hours,
            'ects': mod_ects,
            'learning_results': learning_results
        }

    return boe_data

def extract_cm_data(filepath):
    reader = pypdf.PdfReader(filepath)
    text = ''
    for p in reader.pages:
        text += p.extract_text() + '\n'

    # Similar block-splitting approach for CM to avoid regex jumping
    # Looking for something like "Módulo Profesional: ... (CÓDIGO: 0369)"
    # We will just split by "Módulo Profesional" and then look for code
    module_blocks = text.split("Módulo Profesional")

    cm_data = {}
    for block in module_blocks[1:]:
        code_match = re.search(r'C[ÓO]DIGO\s*:\s*(\w+)\s*\)', block, re.IGNORECASE)
        if not code_match:
            continue
        mod_code = code_match.group(1).strip()

        clean_lines = []
        for line in block.split('\n'):
            line = line.strip()
            if 'B.O.C.M.' in line or 'BOCM' in line or 'BOLETÍN OFICIAL' in line or 'Pág.' in line or 'JUEVES' in line:
                continue
            if not line:
                continue
            clean_lines.append(line)

        # Basic filtering to capture only contents
        # We start looking after "Contenidos" or assume the whole block is contents minus the header
        contents = []
        capture = False
        for line in clean_lines:
            if "Contenidos" in line and not capture:
                capture = True
                continue

            # Stop condition if it hits something else, but CM PDFs usually just list contents
            if "Orientaciones pedagógicas" in line:
                break

            if capture:
                contents.append(line)

        # If we didn't explicitly find "Contenidos", let's just use all clean lines (minus the first few header lines)
        if not contents:
            # Skip first couple of lines which are usually the title/code
            contents = clean_lines[2:] if len(clean_lines) > 2 else clean_lines

        cm_data[mod_code] = {
            'contents': contents
        }

    return cm_data

def update_module_data(boe_data, cm_data, json_filepath='module_data.json'):
    # Load existing data
    if os.path.exists(json_filepath):
        with open(json_filepath, 'r', encoding='utf-8') as f:
            all_data = json.load(f)
    else:
        all_data = {}

    for code, b_data in boe_data.items():
        # Merge with CM data
        if code in cm_data:
            c_data = cm_data[code]
            b_data['contents'] = c_data['contents']
        else:
            b_data['contents'] = []

        # Update json data. Always overwrite for ASIR to ensure we fix the bad data
        all_data[code] = b_data
        print(f"Added/Updated ASIR module {code} - {b_data['name']}")

    with open(json_filepath, 'w', encoding='utf-8') as f:
        json.dump(all_data, f, indent=4, ensure_ascii=False)
    print(f"Saved {json_filepath}")

if __name__ == "__main__":
    boe = extract_boe_data('asir/BOE_ASIR.pdf')
    cm = extract_cm_data('asir/contenidos_basicos_CM_ASIR.pdf')
    update_module_data(boe, cm)
