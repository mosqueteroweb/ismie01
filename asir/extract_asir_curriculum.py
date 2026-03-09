import pypdf
import re
import os

def normalize_text(text):
    return text.replace('\n', ' ').replace('  ', ' ')

def to_filename(name):
    # Remove dots
    name = name.replace('.', '').strip()
    # Replace spaces with underscores
    name = re.sub(r'\s+', '_', name)
    # Convert to lowercase
    name = name.lower()
    # Remove accents
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        ("ñ", "n"),
    )
    for a, b in replacements:
        name = name.replace(a, b).replace(a.upper(), b.upper())
    return name + '.md'

print("Test:", to_filename("Implantación de Sistemas Operativos."))


def extract_boe_data(filepath):
    reader = pypdf.PdfReader(filepath)
    text = ''
    for p in reader.pages:
        text += p.extract_text() + '\n'

    # Find modules
    modules = list(re.finditer(r'Módulo\s+Profesional:\s*(.*?)\s*\n.*?(?:Equivalencia en créditos ECTS:.*?|Duración:.*?)\n*Código:\s*(\w+)', text, re.IGNORECASE))

    boe_data = {}
    for i in range(len(modules)):
        m = modules[i]
        mod_name = m.group(1).strip()
        mod_code = m.group(2).strip()

        start_idx = m.end()
        end_idx = modules[i+1].start() if i + 1 < len(modules) else len(text)

        mod_text = text[start_idx:end_idx]

        # We only want "Resultados de aprendizaje y criterios de evaluación." until "Duración:" or "Contenidos básicos:"
        # Let's find "Resultados de aprendizaje"
        ra_start = mod_text.find('Resultados de aprendizaje y criterios de evaluación.')
        if ra_start == -1:
            ra_start = mod_text.find('Resultados de aprendizaje')

        if ra_start != -1:
            ra_text = mod_text[ra_start:]
        else:
            ra_text = mod_text

        # Cut off at Duración or Contenidos básicos
        end_cut = ra_text.find('Duración:')
        if end_cut == -1:
            end_cut = ra_text.find('Contenidos básicos:')

        if end_cut != -1:
            ra_text = ra_text[:end_cut]

        boe_data[mod_code] = {
            'name': mod_name,
            'ra_text': ra_text.strip()
        }

    return boe_data

boe_data = extract_boe_data('asir/BOE_ASIR.pdf')
print(f"Extracted BOE modules: {len(boe_data)}")
for code, data in boe_data.items():
    print(f"[{code}] {data['name']}: {len(data['ra_text'])} chars")


def extract_cm_data(filepath):
    reader = pypdf.PdfReader(filepath)
    text = ''
    for p in reader.pages:
        text += p.extract_text() + '\n'

    # Find modules
    modules = list(re.finditer(r'Módulo Profesional[^\(]*\([^\)]*C[ÓO]DIGO\s*:\s*(\w+)\s*\)', text, re.IGNORECASE))

    cm_data = {}
    for i in range(len(modules)):
        m = modules[i]
        mod_code = m.group(1).strip()

        start_idx = m.end()
        end_idx = modules[i+1].start() if i + 1 < len(modules) else len(text)

        mod_text = text[start_idx:end_idx]

        # Remove header/footer noise and page numbers
        # E.g. "JUEVES 15 DE ABRIL DE 2010Pág. 124 B.O.C.M. Núm. 89"
        # "BOCM-20100415-5"
        # "BOLETÍN OFICIAL DE LA COMUNIDAD DE MADRIDBOCM"

        clean_lines = []
        for line in mod_text.split('\n'):
            if 'B.O.C.M.' in line or 'BOCM' in line or 'BOLETÍN OFICIAL' in line or 'Pág.' in line or 'JUEVES' in line:
                continue
            clean_lines.append(line)

        clean_text = '\n'.join(clean_lines).strip()

        cm_data[mod_code] = {
            'cm_text': clean_text
        }

    return cm_data

cm_data = extract_cm_data('asir/contenidos_basicos_CM_ASIR.pdf')
print(f"Extracted CM modules: {len(cm_data)}")
for code, data in cm_data.items():
    print(f"[{code}]: {len(data['cm_text'])} chars")


def generate_markdown(boe_data, cm_data, output_dir='asir'):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for code, b_data in boe_data.items():
        if code in cm_data:
            c_data = cm_data[code]

            filename = to_filename(b_data['name'])
            filepath = os.path.join(output_dir, filename)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(f"# Módulo {code} - {b_data['name']}\n\n")

                f.write("## Currículo BOE (Resultados de aprendizaje y Criterios de evaluación)\n\n")
                f.write(b_data['ra_text'])
                f.write("\n\n")

                f.write("## Contenidos Básicos (Comunidad de Madrid)\n\n")
                f.write(c_data['cm_text'])
                f.write("\n")

            print(f"Generated {filepath}")
        else:
            print(f"Warning: Module {code} not found in CM data.")

generate_markdown(boe_data, cm_data)
