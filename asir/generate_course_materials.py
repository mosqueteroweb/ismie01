import os
import re
import sys
import time
import argparse

try:
    import google.generativeai as genai
    HAS_GENAI = True
except ImportError:
    HAS_GENAI = False

def setup_gemini():
    if not HAS_GENAI:
        print("Error: The 'google-generativeai' package is not installed.")
        print("Please run: pip install google-generativeai")
        return False

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: The GEMINI_API_KEY environment variable is not set.")
        print("Please set it before running this script: export GEMINI_API_KEY='your_api_key'")
        return False

    genai.configure(api_key=api_key)
    return True

class LearningOutcome:
    def __init__(self, number, title, criteria, contents):
        self.number = number
        self.title = title
        self.criteria = criteria
        self.contents = contents

def parse_module_file(filepath):
    print(f"\nParsing {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    mod_match = re.search(r'# Módulo (\w+) - (.*?)\n', content)
    if not mod_match:
        print("Could not parse module code/name")
        return None, None

    mod_code = mod_match.group(1)
    mod_name = mod_match.group(2)

    ra_blocks = re.split(r'\n(?=## \d+\.\s)', '\n' + content)
    outcomes = []

    for block in ra_blocks:
        block = block.strip()
        if not re.match(r'^## \d+\.\s', block):
            continue

        ra_match = re.match(r'^## (\d+)\.\s+(.*)', block)
        if not ra_match:
            continue

        ra_num = int(ra_match.group(1))
        lines = block.split('\n')
        ra_title = lines[0].replace(f"## {ra_num}. ", "").strip()

        rest_of_block = '\n'.join(lines[1:]).strip()
        parts = rest_of_block.split("### Contenidos Básicos Relacionados (CM):")

        criteria = parts[0].strip()
        contents = parts[1].strip() if len(parts) > 1 else ""
        outcomes.append(LearningOutcome(ra_num, ra_title, criteria, contents))

    return mod_name, outcomes

def test_parsing():
    for f in os.listdir('asir'):
        if f.endswith('.md') and f != 'generate_course_materials.py' and f != 'extract_asir_curriculum.py' and f != 'update_asir_curriculum.py':
            mod_name, outcomes = parse_module_file(f'asir/{f}')
            if outcomes:
                print(f"[{mod_name}] Found {len(outcomes)} RAs.")

PROMPT_THEORY = """
Eres un profesor experto del ciclo formativo de grado superior ASIR (Administración de Sistemas Informáticos en Red).
Tu objetivo es escribir un temario teórico detallado y pedagógico para el siguiente módulo y Resultado de Aprendizaje (RA).

Módulo: {mod_name}
Resultado de Aprendizaje (RA): {ra_title}
Criterios de Evaluación que los alumnos deben cumplir:
{criteria}

Contenidos Básicos a explicar:
{contents}

INSTRUCCIONES:
1. Escribe un temario completo de aproximadamente 3-5 páginas.
2. Utiliza formato Markdown profesional, con títulos (##, ###), listas, negritas para conceptos clave y bloques de código si aplica.
3. El temario debe estar enfocado estrictamente en cubrir los Contenidos Básicos mencionados y capacitar al alumno para cumplir los Criterios de Evaluación.
4. Incluye ejemplos prácticos o casos de uso dentro de la explicación teórica.
5. No inventes contenidos que no estén relacionados con el temario oficial propuesto.
"""

PROMPT_PRACTICE = """
Eres un profesor experto del ciclo formativo de grado superior ASIR (Administración de Sistemas Informáticos en Red).
Basándote en el siguiente Resultado de Aprendizaje y sus Contenidos Básicos, debes crear un documento de prácticas guiadas y ejercicios resueltos.

Módulo: {mod_name}
Resultado de Aprendizaje (RA): {ra_title}
Criterios de Evaluación:
{criteria}

Contenidos Básicos:
{contents}

INSTRUCCIONES:
1. Crea al menos 3 ejercicios prácticos o casos de estudio reales.
2. Para cada ejercicio incluye:
   - Título del ejercicio.
   - Enunciado claro y contexto del problema.
   - Solución paso a paso detallada (incluyendo comandos, configuración o código si aplica).
3. Utiliza formato Markdown con bloques de código adecuados.
4. Los ejercicios deben evaluar directamente los Criterios de Evaluación listados.
"""

PROMPT_TEST = """
Eres un profesor experto del ciclo formativo de grado superior ASIR (Administración de Sistemas Informáticos en Red).
Tu tarea es generar un examen tipo test para evaluar los conocimientos del siguiente Resultado de Aprendizaje.

Módulo: {mod_name}
Resultado de Aprendizaje (RA): {ra_title}
Criterios de Evaluación:
{criteria}

Contenidos Básicos:
{contents}

INSTRUCCIONES:
1. Genera 10 preguntas de opción múltiple.
2. Cada pregunta debe tener 4 opciones de respuesta, donde solo UNA es correcta.
3. Las preguntas deben evaluar los Criterios de Evaluación y basarse en los Contenidos Básicos.
4. IMPORTANTE: El formato de salida DEBE SER EXCLUSIVAMENTE el formato GIFT de Moodle. No incluyas saludos ni explicaciones, solo el código GIFT.

Ejemplo de formato GIFT esperado:
::Título de la pregunta:: ¿Cuál es el puerto por defecto de HTTP? {{
    =80
    ~8080
    ~443
    ~21
}}
"""

def call_gemini(prompt, retries=3):
    if not HAS_GENAI:
        print("[DRY RUN] Would send to Gemini:", prompt[:100].replace('\n', ' '), "...")
        return "Contenido generado (Simulación)"

    model = genai.GenerativeModel('gemini-1.5-flash')

    for attempt in range(retries):
        try:
            response = model.generate_content(prompt)
            time.sleep(4)
            return response.text
        except Exception as e:
            print(f"  [ERROR] Gemini API Error: {e}")
            if attempt < retries - 1:
                print(f"  [WAITING] Retrying in 10 seconds...")
                time.sleep(10)
            else:
                return f"Error al generar contenido: {e}"

def generate_materials_for_module(filepath, output_dir='asir/materials'):
    mod_name, outcomes = parse_module_file(filepath)
    if not outcomes:
        return

    clean_mod_name = os.path.basename(filepath).replace('.md', '')
    mod_dir = os.path.join(output_dir, clean_mod_name)
    os.makedirs(mod_dir, exist_ok=True)

    print(f"\n--- Generating Materials for: {mod_name} ---")

    for ra in outcomes:
        print(f"Processing RA {ra.number}: {ra.title[:30]}...")

        theory_prompt = PROMPT_THEORY.format(mod_name=mod_name, ra_title=ra.title, criteria=ra.criteria, contents=ra.contents)
        theory_content = call_gemini(theory_prompt)
        with open(os.path.join(mod_dir, f"RA{ra.number}_teoria.md"), 'w', encoding='utf-8') as f:
            f.write(theory_content)

        practice_prompt = PROMPT_PRACTICE.format(mod_name=mod_name, ra_title=ra.title, criteria=ra.criteria, contents=ra.contents)
        practice_content = call_gemini(practice_prompt)
        with open(os.path.join(mod_dir, f"RA{ra.number}_practica.md"), 'w', encoding='utf-8') as f:
            f.write(practice_content)

        test_prompt = PROMPT_TEST.format(mod_name=mod_name, ra_title=ra.title, criteria=ra.criteria, contents=ra.contents)
        test_content = call_gemini(test_prompt)
        with open(os.path.join(mod_dir, f"RA{ra.number}_test.txt"), 'w', encoding='utf-8') as f:
            f.write(test_content)

        print(f"  -> Generated RA {ra.number} files in {mod_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate ASIR Course Materials using Google Gemini API')
    parser.add_argument('input_file', nargs='?', help='Path to the .md module file (e.g., asir/implantacion_de_sistemas_operativos.md)')
    parser.add_argument('--all', action='store_true', help='Process all .md files in the asir/ directory')
    parser.add_argument('--test-parse', action='store_true', help='Test parsing of .md files without generating content')
    parser.add_argument('--dry-run', action='store_true', help='Simulate API calls without requiring a Gemini key')

    args = parser.parse_args()

    if args.test_parse:
        test_parsing()
        sys.exit(0)

    if not args.dry_run:
        if not setup_gemini():
             print("Continuing in DRY RUN mode...")
             HAS_GENAI = False
             args.dry_run = True

    if args.dry_run:
        print("Running in DRY RUN mode (No API calls will be made)")
        HAS_GENAI = False

    if args.input_file:
        if os.path.exists(args.input_file):
            generate_materials_for_module(args.input_file)
        else:
            print(f"Error: File '{args.input_file}' not found.")
    elif args.all:
        for f in os.listdir('asir'):
            if f.endswith('.md') and f not in ['generate_course_materials.py', 'extract_asir_curriculum.py', 'update_asir_curriculum.py']:
                generate_materials_for_module(os.path.join('asir', f))
    else:
        parser.print_help()
