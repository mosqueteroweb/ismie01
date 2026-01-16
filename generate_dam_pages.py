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
    }
]

def load_module_data():
    if not os.path.exists("module_data.json"):
        print("Error: module_data.json not found.")
        return {}
    with open("module_data.json", "r", encoding="utf-8") as f:
        return json.load(f)

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
                            <span class="bg-blue-600 text-white text-xs px-2 py-1 rounded font-mono">RA {ra_id}</span>
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

    current_block_title = "Contenidos Generales"
    current_items = []
    blocks = []

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
        content = re.sub(r'<span class="bg-blue-600 text-white px-3 py-1 rounded-full text-sm font-semibold shadow-sm">.*?</span>',
                         f'<span class="bg-blue-600 text-white px-3 py-1 rounded-full text-sm font-semibold shadow-sm">{meta["course"]}</span>',
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

            # Find the closing div of space-y-4.
            # In the template (dam_di.html), it has nested details.
            # We assume the template structure is valid.
            # Find the last </div> before </section> is the CONTAINER closer.
            # The one before that is the space-y-4 closer.

            last_div = content.rfind('</div>', start_div_ra, end_sec_res)
            last_div_ra = content.rfind('</div>', start_div_ra, last_div)

            if start_div_ra != -1 and last_div_ra != -1:
                content = content[:start_div_ra] + ra_html + content[last_div_ra+6:]

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
