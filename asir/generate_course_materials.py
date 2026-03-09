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
        if f.endswith('.md') and f not in ['generate_course_materials.py', 'extract_asir_curriculum.py', 'update_asir_curriculum.py']:
            mod_name, outcomes = parse_module_file(f'asir/{f}')
            if outcomes:
                print(f"[{mod_name}] Found {len(outcomes)} RAs.")

PROMPT_OUTLINE = """
Eres un profesor experto del ciclo formativo de grado superior ASIR (Administración de Sistemas Informáticos en Red).
Tu objetivo es diseñar un índice maestro sumamente detallado (outline) para crear el temario de un Resultado de Aprendizaje.

Módulo: {mod_name}
Resultado de Aprendizaje (RA): {ra_title}
Criterios de Evaluación a cubrir:
{criteria}

Contenidos Básicos obligatorios:
{contents}

INSTRUCCIONES:
1. Analiza los contenidos y los criterios, y divídelos en una lista de exactamente 4 a 6 secciones temáticas principales.
2. Cada sección debe tener un título claro y conciso.
3. Responde ÚNICAMENTE con la lista de títulos, uno por línea, numerados (ej. "1. Introducción a...", "2. Arquitectura de...").
4. No incluyas saludos ni explicaciones, solo la lista numerada.
"""

PROMPT_THEORY_SECTION = """
Eres un profesor experto del ciclo formativo ASIR escribiendo un manual técnico detallado de nivel universitario/técnico superior.
Estás escribiendo un capítulo específico para el siguiente Resultado de Aprendizaje: {ra_title}

Tu tarea actual es desarrollar EXCLUSIVAMENTE la siguiente sección del temario:
TÍTULO DE LA SECCIÓN: "{section_title}"

INSTRUCCIONES PARA LA REDACCIÓN:
1. Escribe al menos 600-800 palabras de teoría profunda, técnica y exhaustiva SOLO sobre este título.
2. Utiliza formato Markdown profesional: subtítulos (###, ####), listas, negritas para términos técnicos.
3. INCLUYE SIEMPRE EJEMPLOS TÉCNICOS: comandos de terminal, código de configuración, o ejemplos de topologías de red que apliquen.
4. DIAGRAMAS: Si aplica a la temática, debes incluir obligatoriamente al menos un bloque de código tipo `mermaid` para ilustrar arquitecturas, flujos de trabajo o diagramas de red.
5. No hagas introducciones generales al módulo entero, céntrate estrictamente y a fondo en "{section_title}".
"""

PROMPT_PRACTICE = """
Eres un profesor experto del ciclo formativo de grado superior ASIR.
Basándote en el siguiente Resultado de Aprendizaje, debes crear un documento de prácticas guiadas basadas en Aprendizaje Basado en Retos (Casos Reales).

Módulo: {mod_name}
Resultado de Aprendizaje (RA): {ra_title}
Criterios de Evaluación:
{criteria}

Contenidos Básicos:
{contents}

INSTRUCCIONES:
1. Diseña 3 prácticas. Cada práctica debe estar ambientada en una empresa ficticia con un problema informático realista y urgente.
2. Para cada práctica incluye en Markdown:
   - ## Práctica X: [Título atractivo]
   - ### 🏢 El Escenario: Contexto de la empresa, el problema exacto y por qué es crítico solucionarlo.
   - ### 🎯 Requisitos del Cliente: Qué se espera que haga el técnico (el alumno).
   - ### 🛠️ Solución Paso a Paso: Instrucciones detalladas de cómo resolverlo (comandos exactos, líneas de configuración de archivos, pasos en la interfaz gráfica, etc.).
3. Los ejercicios deben ser avanzados, técnicos y evaluar directamente los Criterios de Evaluación listados.
"""

PROMPT_TEST = """
Eres un profesor experto del ciclo formativo de grado superior ASIR.
Genera un examen tipo test para evaluar el siguiente Resultado de Aprendizaje.

Módulo: {mod_name}
Resultado de Aprendizaje (RA): {ra_title}
Criterios de Evaluación:
{criteria}

INSTRUCCIONES:
1. Genera 10 preguntas de opción múltiple muy técnicas (evita preguntas demasiado obvias).
2. Cada pregunta debe tener 4 opciones de respuesta, donde solo UNA es correcta.
3. IMPORTANTE: El formato de salida DEBE SER EXCLUSIVAMENTE el formato GIFT de Moodle. No incluyas saludos, explicaciones, ni bloques de código markdown, solo el texto GIFT puro.

Ejemplo estricto de formato GIFT esperado:
::Título corto:: Enunciado de la pregunta {{
    =Respuesta correcta
    ~Respuesta falsa 1
    ~Respuesta falsa 2
    ~Respuesta falsa 3
}}
"""

PROMPT_TEST_REVIEW = """
Eres un inspector educativo técnico y experto en ASIR.
Aquí tienes un examen tipo test generado en formato GIFT de Moodle para el RA: {ra_title}.

Examen Generado:
{test_content}

INSTRUCCIONES:
1. Revisa rigurosamente el examen. Comprueba que las respuestas marcadas con "=" son técnicamente 100% correctas y que las marcadas con "~" son innegablemente incorrectas.
2. Comprueba que no hay preguntas repetidas.
3. Corrige cualquier error, mejora la redacción si es ambigua, y asegúrate de que el formato GIFT es perfecto.
4. Devuelve ÚNICAMENTE el código GIFT corregido final. Sin preámbulos, sin bloques de código markdown, solo el texto plano.
"""

def call_gemini(prompt, retries=3):
    if not HAS_GENAI:
        print("[DRY RUN] Would send to Gemini:", prompt[:80].replace('\n', ' '), "...")
        return "Contenido generado (Simulación)\n"

    model_name = os.environ.get('GEMINI_MODEL', 'gemini-1.5-flash-8b')
    model = genai.GenerativeModel(model_name)

    for attempt in range(retries):
        try:
            response = model.generate_content(prompt)
            if 'flash' in model_name.lower():
                time.sleep(4)  # 15 RPM limit for Flash free tier
            else:
                time.sleep(13)  # 5 RPM limit for others
            return response.text
        except Exception as e:
            print(f"  [ERROR] Gemini API Error: {e}")
            if attempt < retries - 1:
                print(f"  [WAITING] Retrying in 65 seconds...")
                time.sleep(65) # Wait 1 minute for RPM reset
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
        print(f"\nProcessing RA {ra.number}: {ra.title[:50]}...")

        # 1. GENERATE THEORY (Multi-step)
        print(f"  [1/4] Generating Theory Outline...")
        outline_prompt = PROMPT_OUTLINE.format(
            mod_name=mod_name, ra_title=ra.title, criteria=ra.criteria, contents=ra.contents
        )
        outline = call_gemini(outline_prompt)

        # Parse outline lines (e.g. "1. Introducción a redes")
        sections = [line.strip() for line in outline.split('\n') if line.strip() and re.match(r'^\d+\.', line.strip())]
        if not sections:
            # Fallback if AI didn't format properly
            sections = ["Conceptos Generales", "Desarrollo de Criterios", "Aspectos Prácticos"]

        theory_content = f"# Temario: {ra.title}\n\n"

        for i, section_title in enumerate(sections):
            print(f"  [1/4] Generating Theory Section {i+1}/{len(sections)}: {section_title[:30]}...")
            section_prompt = PROMPT_THEORY_SECTION.format(
                ra_title=ra.title, section_title=section_title
            )
            section_text = call_gemini(section_prompt)
            theory_content += f"## {section_title}\n\n{section_text}\n\n"

        with open(os.path.join(mod_dir, f"RA{ra.number}_teoria.md"), 'w', encoding='utf-8') as f:
            f.write(theory_content)

        # 2. GENERATE PRACTICE (Role-play)
        print(f"  [2/4] Generating Role-play Practices...")
        practice_prompt = PROMPT_PRACTICE.format(
            mod_name=mod_name, ra_title=ra.title, criteria=ra.criteria, contents=ra.contents
        )
        practice_content = call_gemini(practice_prompt)
        with open(os.path.join(mod_dir, f"RA{ra.number}_practica.md"), 'w', encoding='utf-8') as f:
            f.write(practice_content)

        # 3. GENERATE TEST
        print(f"  [3/4] Generating GIFT Test...")
        test_prompt = PROMPT_TEST.format(
            mod_name=mod_name, ra_title=ra.title, criteria=ra.criteria
        )
        test_content_raw = call_gemini(test_prompt)

        # 4. REVIEW TEST
        print(f"  [4/4] Reviewing and correcting Test...")
        review_prompt = PROMPT_TEST_REVIEW.format(
            ra_title=ra.title, test_content=test_content_raw
        )
        test_content_final = call_gemini(review_prompt)

        # Strip potential markdown code blocks from the final GIFT output
        test_content_final = re.sub(r'```(?:gift|txt|text)?\n', '', test_content_final)
        test_content_final = test_content_final.replace('```', '')

        with open(os.path.join(mod_dir, f"RA{ra.number}_test.txt"), 'w', encoding='utf-8') as f:
            f.write(test_content_final.strip())

        print(f"  -> Finished RA {ra.number} files in {mod_dir}")

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
