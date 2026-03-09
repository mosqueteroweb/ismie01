import os
import glob
from bs4 import BeautifulSoup
from crew import AsirCurriculumCrew

def extract_module_acronym(filename):
    """Extrae las siglas del módulo desde el nombre del archivo (ej. asir_iso.html -> ISO)"""
    base_name = os.path.basename(filename)
    name_without_ext = os.path.splitext(base_name)[0]
    parts = name_without_ext.split('_')
    if len(parts) > 1:
        return parts[1].upper()
    return "UNKNOWN"

def process_html_file(filepath):
    """Procesa un archivo HTML, extrae RA y contenidos y ejecuta la Crew."""
    print(f"\\n--- Procesando archivo: {filepath} ---")

    with open(filepath, 'r', encoding='utf-8') as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    # Nombre del módulo
    title_tag = soup.find('h2')
    module_name = title_tag.text.strip() if title_tag else os.path.basename(filepath)
    module_acronym = extract_module_acronym(filepath)

    # Crear carpeta principal ASIR si no existe
    base_output_dir = "documentacionASIR"
    os.makedirs(base_output_dir, exist_ok=True)

    # Crear carpeta específica del módulo (ej. documentacion_ISO)
    module_output_dir = os.path.join(base_output_dir, f"documentacion_{module_acronym}")
    os.makedirs(module_output_dir, exist_ok=True)

    print(f"Módulo: {module_name} ({module_acronym})")
    print(f"Directorio de salida: {module_output_dir}")

    # Extraer Contenidos Básicos completos (section id="contenidos")
    contenidos_section = soup.find('section', id='contenidos')
    contenidos_html = str(contenidos_section) if contenidos_section else "No se encontraron Contenidos Básicos."

    # Extraer Resultados de Aprendizaje
    resultados_section = soup.find('section', id='resultados')
    if not resultados_section:
        print("No se encontraron Resultados de Aprendizaje en el archivo.")
        return

    ra_details = resultados_section.find_all('details')

    for i, detail in enumerate(ra_details, start=1):
        ra_number = f"RA{i}"

        # Opcional: Extraer título específico del RA si es necesario
        ra_title_span = detail.find('span', string=lambda text: text and text.startswith('RA'))
        ra_text = ""
        if ra_title_span:
            # Siguiente sibling span suele ser el texto del RA
            text_span = ra_title_span.find_next_sibling('span')
            if text_span:
                ra_text = text_span.text.strip()

        print(f"  > Preparando {ra_number} - {ra_text}")

        # Componer el contexto a enviar al LLM
        # Enviamos el HTML específico del RA actual + los contenidos globales para que el agente extraiga lo relevante
        contexto_archivo = f"<h1>{ra_number}: {ra_text}</h1>\\n"
        contexto_archivo += str(detail) + "\\n"
        contexto_archivo += "<h1>Contenidos Básicos del Módulo</h1>\\n"
        contexto_archivo += contenidos_html

        inputs = {
            'modulo': module_name,
            'ra_number': ra_number,
            'contexto_archivo': contexto_archivo
        }

        # Inicializar y ejecutar la Crew para este RA
        try:
            print(f"  > Ejecutando CrewAI para {module_acronym} - {ra_number}...")
            # Pasamos el output_dir y el ra_number a la Crew para que sepa dónde guardar los archivos
            crew_instance = AsirCurriculumCrew(
                output_dir=module_output_dir,
                ra_number=ra_number
            ).crew()

            # CrewAI permite pasar inputs a todas las tareas
            result = crew_instance.kickoff(inputs=inputs)
            print(f"  > ¡Completado {ra_number} para {module_acronym}!")
        except Exception as e:
            print(f"  > Error ejecutando CrewAI para {ra_number}: {e}")

def main():
    # Buscar todos los archivos HTML del directorio ASIR que tengan el formato asir_*.html
    # Asumiendo que se ejecuta desde la raíz o dentro de asir/
    target_files = []
    if os.path.exists("asir"):
        target_files = glob.glob("asir/asir_*.html")
    else:
        target_files = glob.glob("asir_*.html")

    # Filtrar el index general
    target_files = [f for f in target_files if not f.endswith("asir.html")]

    if not target_files:
        print("No se encontraron archivos asir_*.html para procesar.")
        return

    print(f"Archivos encontrados: {len(target_files)}")

    # Procesar archivo a archivo para no saturar contexto
    for filepath in target_files:
        process_html_file(filepath)
        print("-" * 50)

if __name__ == "__main__":
    main()
