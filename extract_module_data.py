import xml.etree.ElementTree as ET
import json
import re
import sys
import os

def parse_boe_xml(filepath):
    modules = {}
    current_module = None
    current_ra = None
    current_section = None # 'RA_CE' (Resultados/Criterios), 'CB' (Contenidos), 'PARAMS' (Duración/ECTS)

    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return {}

    try:
        tree = ET.parse(filepath)
        root = tree.getroot()

        texto_node = root.find('texto')
        if texto_node is None:
            # Fallback if no 'texto' tag at root level (some XMLs differ)
            paragraphs = root.findall('.//p')
        else:
            paragraphs = texto_node.findall('.//p')

        for p in paragraphs:
            text = p.text
            if not text:
                continue
            text = text.strip()

            # Detect Module Start
            if text.startswith("Módulo Profesional:"):
                # Save previous module
                if current_module:
                    modules[current_module['code']] = current_module

                module_name = text.replace("Módulo Profesional:", "").strip().rstrip('.')
                current_module = {
                    "name": module_name,
                    "code": "UNKNOWN",
                    "hours": "",
                    "ects": "",
                    "learning_results": [],
                    "contents": []
                }
                current_ra = None
                current_section = 'PARAMS'
                continue

            if current_module:
                # Detect Code
                if text.startswith("Código:"):
                    current_module['code'] = text.replace("Código:", "").strip().rstrip('.')
                    continue

                # Detect ECTS
                if "Equivalencia en créditos ECTS" in text:
                    parts = text.split(':')
                    if len(parts) > 1:
                        current_module['ects'] = parts[1].strip().rstrip('.')
                    continue

                # Detect Duration (sometimes at start, sometimes at end)
                if text.startswith("Duración:"):
                    parts = text.split(':')
                    if len(parts) > 1:
                        current_module['hours'] = parts[1].strip().replace(" horas", "").rstrip('.')
                    continue

                # Detect Section Headers
                if "Resultados de aprendizaje y criterios de evaluación" in text or "Resultados de aprendizaje y Criterios de evaluación" in text:
                    current_section = 'RA_CE'
                    continue

                if "Contenidos básicos" in text or "Contenidos básicos:" in text:
                    current_section = 'CB'
                    continue

                if "Orientaciones pedagógicas" in text:
                    current_section = 'OP' # We stop capturing contents here
                    continue

                # Parse RA and CE
                if current_section == 'RA_CE':
                    # Detect Result of Learning (starts with number and dot, e.g., "1. Evalúa...")
                    # Regex for "1. Text" or "1.Text"
                    ra_match = re.match(r'^(\d+)\.\s*(.+)', text)
                    if ra_match:
                        current_ra = {
                            "id": ra_match.group(1),
                            "description": ra_match.group(2),
                            "evaluation_criteria": []
                        }
                        current_module['learning_results'].append(current_ra)

                    # Detect Criteria (starts with letter and paren, e.g., "a) Se han...")
                    elif re.match(r'^[a-z]\)\s+', text) and current_ra:
                        current_ra['evaluation_criteria'].append(text)

                    # Sometimes "Criterios de evaluación:" appears as a header, ignore it
                    elif "Criterios de evaluación" in text:
                        continue

                # Parse Contents
                elif current_section == 'CB':
                    # Just add the lines for now, we can format later or keep as list
                    if text:
                        current_module['contents'].append(text)

        # Add the last module
        if current_module and current_module['code'] != "UNKNOWN":
             modules[current_module['code']] = current_module

    except Exception as e:
        print(f"Error parsing {filepath}: {e}")
        import traceback
        traceback.print_exc()

    return modules

def main():
    all_modules = {}

    # Parse RD 450/2010 (Technical Modules)
    print("Parsing RD 450/2010...")
    dam_modules = parse_boe_xml('data/rd_450_2010.xml')
    all_modules.update(dam_modules)
    print(f"Found {len(dam_modules)} modules in RD 450/2010.")

    # Parse RD 659/2023 (New Modules)
    print("Parsing RD 659/2023...")
    new_modules = parse_boe_xml('data/rd_659_2023.xml')
    all_modules.update(new_modules)
    print(f"Found {len(new_modules)} modules in RD 659/2023.")

    # Save to JSON
    with open('module_data.json', 'w', encoding='utf-8') as f:
        json.dump(all_modules, f, indent=4, ensure_ascii=False)

    print("Saved module_data.json")

if __name__ == "__main__":
    main()
