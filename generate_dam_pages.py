import os
import json
import re

TEMPLATE_FILE = "dam_di.html"

MODULES_METADATA = [
    {
        "filename": "dam_si.html",
        "title": "Sistemas Informáticos",
        "code": "0483",
        "weekly": "6",
        "desc": "Configuración, administración y mantenimiento de sistemas informáticos, hardware, software y redes locales.",
        "course": "1º Curso DAM"
    },
    {
        "filename": "dam_bd.html",
        "title": "Bases de Datos",
        "code": "0484",
        "weekly": "6",
        "desc": "Diseño, gestión y manipulación de bases de datos relacionales y no relacionales.",
        "course": "1º Curso DAM"
    },
    {
        "filename": "dam_prog.html",
        "title": "Programación",
        "code": "0485",
        "weekly": "8",
        "desc": "Fundamentos de programación, estructuras de datos, programación orientada a objetos y buenas prácticas.",
        "course": "1º Curso DAM"
    },
    {
        "filename": "dam_ed.html",
        "title": "Entornos de Desarrollo",
        "code": "0487",
        "weekly": "3",
        "desc": "Uso de IDEs, control de versiones, optimización de código y pruebas unitarias.",
        "course": "1º Curso DAM"
    },
    {
        "filename": "dam_lm.html",
        "title": "Lenguajes de Marcas",
        "code": "0373",
        "weekly": "4",
        "desc": "Lenguajes de marcado (XML, HTML), hojas de estilo y sistemas de gestión de información empresarial.",
        "course": "1º Curso DAM"
    },
    {
        "filename": "dam_ipe1.html",
        "title": "Itinerario Personal para la Empleabilidad I",
        "code": "1709",
        "weekly": "3",
        "desc": "Orientación laboral, derechos y deberes, y prevención de riesgos laborales.",
        "course": "1º Curso DAM"
    },
    {
        "filename": "dam_da.html",
        "title": "Digitalización Aplicada",
        "code": "1665",
        "weekly": "2",
        "desc": "Competencias digitales aplicadas a los sectores productivos y transformación digital.",
        "course": "1º Curso DAM"
    },
    {
        "filename": "dam_ad.html",
        "title": "Acceso a Datos",
        "code": "0486",
        "weekly": "5",
        "desc": "Gestión de la persistencia de datos, mapeo objeto-relacional (ORM) y bases de datos nativas.",
        "course": "2º Curso DAM"
    },
    {
        "filename": "dam_pmdm.html",
        "title": "Prog. Multimedia y Disp. Móviles",
        "code": "0489",
        "weekly": "4",
        "desc": "Desarrollo de aplicaciones para dispositivos móviles, integración multimedia y librerías gráficas.",
        "course": "2º Curso DAM"
    },
    {
        "filename": "dam_psp.html",
        "title": "Prog. de Servicios y Procesos",
        "code": "0490",
        "weekly": "3",
        "desc": "Programación concurrente, programación de red y servicios telemáticos.",
        "course": "2º Curso DAM"
    },
    {
        "filename": "dam_sge.html",
        "title": "Sistemas de Gestión Empresarial",
        "code": "0491",
        "weekly": "3",
        "desc": "Implantación, adaptación y mantenimiento de sistemas de planificación de recursos empresariales (ERP).",
        "course": "2º Curso DAM"
    },
    {
        "filename": "dam_ip.html",
        "title": "Inglés Profesional",
        "code": "0179",
        "weekly": "2",
        "desc": "Comunicación en lengua inglesa en el entorno profesional del sector informático.",
        "course": "2º Curso DAM"
    },
    {
        "filename": "dam_ipe2.html",
        "title": "Itinerario Personal para la Empleabilidad II",
        "code": "1710",
        "weekly": "2",
        "desc": "Habilidades sociales, trabajo en equipo, liderazgo y emprendimiento.",
        "course": "2º Curso DAM"
    },
    {
        "filename": "dam_sa.html",
        "title": "Sostenibilidad Aplicada",
        "code": "1708",
        "weekly": "2",
        "desc": "Criterios de sostenibilidad y protección ambiental en el sector productivo.",
        "course": "2º Curso DAM"
    },
        {
        "filename": "dam_di.html",
        "title": "Desarrollo de Interfaces",
        "code": "0488",
        "weekly": "6",
        "desc": "Diseño y desarrollo de interfaces gráficas de usuario, usabilidad y experiencia de usuario.",
        "course": "2º Curso DAM"
    },
    {
        "filename": "dam_fct.html",
        "title": "Formación en Centros de Trabajo",
        "code": "0495",
        "weekly": "0",
        "desc": "Prácticas en empresa.",
        "course": "2º Curso DAM"
    },
    {
        "filename": "dam_proy.html",
        "title": "Proyecto de Desarrollo de Aplicaciones Multiplataforma",
        "code": "0492",
        "weekly": "0",
        "desc": "Proyecto final de ciclo.",
        "course": "2º Curso DAM"
    }
]

def load_module_data():
    if not os.path.exists("module_data.json"):
        print("Error: module_data.json not found.")
        return {}
    with open("module_data.json", "r", encoding="utf-8") as f:
        return json.load(f)

def parse_contents(module_info):
    current_block_title = "Contenidos Generales"
    current_items = []
    blocks = []

    if module_info and 'contents' in module_info:
        for line in module_info['contents']:
            line = line.strip()
            if not line: continue

            if line.endswith(":") and len(line) < 100:
                if current_items:
                    blocks.append({"title": current_block_title, "items": current_items})
                current_block_title = line.rstrip(':')
                current_items = []
            else:
                clean_line = line.lstrip('−').lstrip('-').lstrip('•').strip()
                if clean_line:
                    current_items.append(clean_line)

        if current_items:
            blocks.append({"title": current_block_title, "items": current_items})

        if not blocks and current_items:
            blocks.append({"title": "Contenidos", "items": current_items})
    return blocks

def generate_ra_html(module_info):
    html = '<div class="space-y-4">'

    if not module_info or 'learning_results' not in module_info:
        return html + "<!-- No data available --></div>"

    for ra in module_info['learning_results']:
        ra_id = ra['id']
        ra_desc = ra['description']
        criteria_html = ""
        for crit in ra['evaluation_criteria']:
            criteria_html += f'<li class="flex items-start gap-2"><span class="text-blue-500 mt-1">•</span> {crit}</li>\n'

        html += f"""
                <details class="group bg-white rounded-xl border border-slate-200 overflow-hidden transition-all duration-300 open:shadow-lg open:ring-1 open:ring-blue-500">
                    <summary class="flex justify-between items-center cursor-pointer p-5 bg-slate-50 hover:bg-slate-100 font-bold text-slate-800 select-none">
                        <div class="flex items-center gap-3">
                            <span class="bg-blue-600 text-white text-xs px-2 py-1 rounded font-mono whitespace-nowrap shrink-0">RA {ra_id}</span>
                            <span>{ra_desc}</span>
                        </div>
                        <span class="group-open:rotate-180 transition-transform text-slate-400">▼</span>
                    </summary>
                    <div class="p-6 border-t border-slate-200 bg-white">
                        <ul class="space-y-2 text-sm text-slate-700">
                            {criteria_html}
                        </ul>
                    </div>
                </details>
        """
    html += '</div>'
    return html

def generate_contents_html(module_info):
    html = '<div class="grid grid-cols-1 md:grid-cols-2 gap-6">'

    if not module_info or 'contents' not in module_info:
        return html + "<!-- No data available --></div>"

    blocks = parse_contents(module_info)
    colors = ["blue", "orange", "green", "purple"]

    for i, block in enumerate(blocks):
        color = colors[i % len(colors)]
        items_html = ""
        for item in block['items']:
            items_html += f'<li>{item}</li>\n'

        html += f"""
                <div class="card p-6 border-l-4 border-l-{color}-500">
                    <h4 class="text-lg font-bold text-slate-800 mb-3">{block['title']}</h4>
                    <ul class="text-sm text-slate-600 space-y-1 list-disc pl-4">
                        {items_html}
                    </ul>
                </div>
        """

    html += '</div>'
    return html

def generate_relations_page(module_info, meta, acronym):
    blocks = parse_contents(module_info)
    ras = module_info.get('learning_results', []) if module_info else []

    # Generate Rows HTML
    rows_html = ""
    for i, ra in enumerate(ras):
        ra_id = ra['id']
        ra_desc = ra['description']

        # Criteria
        criteria_html = '<ul class="space-y-2">'
        for crit in ra['evaluation_criteria']:
             criteria_html += f'<li class="flex gap-2"><span class="text-blue-400">•</span> <span>{crit}</span></li>'
        criteria_html += '</ul>'

        # Content Block
        content_html = ""
        if i < len(blocks):
            block = blocks[i]
            items_list = "".join([f'<li>{item}</li>' for item in block['items']])
            content_html = f"<div class='font-bold text-orange-600 mb-2'>{block['title']}</div><ul class=\"list-disc pl-4 space-y-1 text-xs\">{items_list}</ul>"
        else:
             content_html = "<span class='text-slate-400 italic'>No hay contenidos vinculados directamente.</span>"

        rows_html += f"""
                        <tr class="hover:bg-slate-50 transition-colors">
                            <td class="px-6 py-6 align-top bg-white"><span class='font-bold text-blue-600'>RA {ra_id}</span><br>{ra_desc}</td>
                            <td class="px-6 py-6 align-top">{criteria_html}</td>
                            <td class="px-6 py-6 align-top bg-orange-50/30">{content_html}</td>
                        </tr>
        """

    # Full Page Template
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Relaciones RA-Contenidos - {meta['title']}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700;900&display=swap" rel="stylesheet">
    <style>
        body {{ font-family: 'Roboto', sans-serif; background-color: #f8fafc; color: #1e293b; }}
        .back-btn {{ position: fixed; top: 20px; left: 20px; z-index: 100; }}
    </style>
</head>
<body class="pb-20">

    <!-- Back Button -->
    <a href="{meta['filename']}" class="back-btn bg-white p-3 rounded-full shadow-lg hover:bg-blue-50 text-blue-600 transition-all border border-blue-100 group">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 group-hover:-translate-x-1 transition-transform" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
        </svg>
    </a>

    <!-- Header -->
    <header class="bg-white shadow-sm border-b border-gray-100 mb-12">
        <div class="max-w-7xl mx-auto px-6 py-8 text-center">
            <div class="inline-block bg-orange-100 text-orange-600 text-xs font-bold px-3 py-1 rounded-full mb-3">Módulo {meta['code']}</div>
            <h1 class="text-3xl md:text-4xl font-extrabold text-slate-800 mb-2">Relación Resultados de Aprendizaje - Contenidos</h1>
            <p class="text-slate-500 text-lg">{meta['title']}</p>
        </div>
    </header>

    <main class="max-w-7xl mx-auto px-6 space-y-16">

        <!-- Detailed Table Section -->
        <section class="bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden">
            <div class="p-8 border-b border-slate-100">
                 <h2 class="text-2xl font-bold text-slate-800 border-l-4 border-orange-500 pl-4">Matriz de Detalle</h2>
            </div>
            <div class="overflow-x-auto">
                <table class="w-full text-left text-sm text-slate-600">
                    <thead class="bg-slate-50 text-slate-800 font-bold uppercase text-xs tracking-wider">
                        <tr>
                            <th class="px-6 py-4 w-1/4">Resultado de Aprendizaje</th>
                            <th class="px-6 py-4 w-1/3">Criterios de Evaluación</th>
                            <th class="px-6 py-4 w-1/3">Contenidos Básicos Asociados</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-100">
                        {rows_html}
                    </tbody>
                </table>
            </div>
        </section>

    </main>

    <footer class="bg-white border-t border-slate-200 mt-20 py-12">
        <div class="max-w-7xl mx-auto px-6 text-center text-slate-400 text-sm">
            <p>Autor © Pedro Salazar 2026</p>
        </div>
    </footer>

</body>
</html>"""

    rel_filename = f"dam_{acronym}_relaciones.html"
    with open(rel_filename, "w", encoding="utf-8") as out:
        out.write(html)
    print(f"Generated {rel_filename}")
    return rel_filename

def generate_pages():
    module_data_json = load_module_data()

    with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
        template_content = f.read()

    for meta in MODULES_METADATA:
        code = meta['code']
        print(f"Processing {meta['filename']} ({code})...")

        data = module_data_json.get(code)
        if not data:
            print(f"  Warning: No data found for code {code}")
            data = {"hours": meta.get("hours", "???"), "ects": meta.get("ects", "?"), "learning_results": [], "contents": []}

        hours = data.get('hours') or meta.get('hours', '???')
        ects = data.get('ects') or meta.get('ects', '???')
        acronym = meta['filename'].replace('dam_', '').replace('.html', '')

        content = template_content

        # 1. Title
        start_title = content.find('<title>')
        end_title = content.find('</title>')
        if start_title != -1:
            content = content[:start_title+7] + f"{meta['title']} (DAM) - Módulo {code}" + content[end_title:]

        content = re.sub(r'<h2 class="text-4xl md:text-5xl font-extrabold mb-4 leading-tight">.*?</h2>',
                         f'<h2 class="text-4xl md:text-5xl font-extrabold mb-4 leading-tight">{meta["title"]}</h2>',
                         content)

        # 2. Course Badge
        content = re.sub(r'<div class="inline-block bg-orange-500 text-white text-xs font-bold px-3 py-1 rounded-full mb-4">.*?</div>',
                         f'<div class="inline-block bg-orange-500 text-white text-xs font-bold px-3 py-1 rounded-full mb-4">{meta["course"]}</div>',
                         content)

        # 3. Description
        content = re.sub(r'<p class="text-xl text-slate-300 max-w-2xl">.*?</p>',
                         f'<p class="text-xl text-slate-300 max-w-2xl">Módulo Profesional {code}. {meta["desc"]}</p>',
                         content, flags=re.DOTALL)

        # 4. Stats
        # ECTS
        content = re.sub(r'(<p class="text-3xl font-black text-white">).*?(</p>\s*<p class="text-xs text-slate-400 uppercase font-bold tracking-wider">ECTS</p>)',
                         f'\\g<1>{ects}\\g<2>', content)

        # Code
        content = re.sub(r'(<p class="text-3xl font-black text-orange-400">).*?(</p>\s*<p class="text-xs text-slate-400 uppercase font-bold tracking-wider">Código</p>)',
                         f'\\g<1>{code}\\g<2>', content)

        # Hours
        content = re.sub(r'(<p class="text-3xl font-black text-white">).*?(</p>\s*<p class="text-xs text-slate-400 uppercase font-bold tracking-wider">Horas</p>)',
                         f'\\g<1>{hours}\\g<2>', content)

        # Weekly
        content = re.sub(r'(<p class="text-3xl font-black text-white">).*?(</p>\s*<p class="text-xs text-slate-400 uppercase font-bold tracking-wider">Semanales</p>)',
                         f'\\g<1>{meta["weekly"]}\\g<2>', content)

        # 5. Learning Results
        ra_html = generate_ra_html(data)
        start_sec_res = content.find('id="resultados"')
        if start_sec_res != -1:
            start_div_ra = content.find('<div class="space-y-4">', start_sec_res)
            end_sec_res = content.find('</section>', start_div_ra)

            last_div = content.rfind('</div>', start_div_ra, end_sec_res)
            last_div_ra = content.rfind('</div>', start_div_ra, last_div)

            if start_div_ra != -1 and last_div_ra != -1:
                content = content[:start_div_ra] + ra_html + content[last_div_ra+6:]

        # Handle Relations Page Generation and Link
        has_content = len(data.get('contents', [])) > 0
        if has_content:
            generate_relations_page(data, meta, acronym)
            # Replace the link in the template with the correct filename
            content = content.replace('dam_di_relaciones.html', f'dam_{acronym}_relaciones.html')
        else:
             # Remove the link button if no content (or if we don't want to generate a blank page)
             # The template has: <div class="mt-4"><a href="dam_di_relaciones.html" ... </div>
             # We can regex replace it to empty string.
             content = re.sub(r'<div class="mt-4"><a href="dam_di_relaciones\.html".*?</div>', '', content, flags=re.DOTALL)


        # 6. Contents
        con_html = generate_contents_html(data)
        start_sec_con = content.find('id="contenidos"')
        if start_sec_con != -1:
            start_div_con = content.find('<div class="grid grid-cols-1 md:grid-cols-2 gap-6">', start_sec_con)
            end_sec_con = content.find('</section>', start_div_con)

            last_div_container = content.rfind('</div>', start_div_con, end_sec_con)
            last_div_grid = content.rfind('</div>', start_div_con, last_div_container)

            if start_div_con != -1 and last_div_grid != -1:
                content = content[:start_div_con] + con_html + content[last_div_grid+6:]

        with open(meta['filename'], "w", encoding="utf-8") as out:
            out.write(content)

        print(f"Generated {meta['filename']}")

if __name__ == "__main__":
    generate_pages()
