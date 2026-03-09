import os
import json
import re

TEMPLATE_FILE = "DAM/dam_di.html"

MODULES_METADATA = [
    {
        "filename": "asir_fh.html",
        "title": "Fundamentos de hardware",
        "code": "0371",
        "weekly": "3",
        "desc": "Configuración y ensamblaje de equipos informáticos, sistemas físicos y arquitectura de computadores.",
        "course": "1º Curso ASIR"
    },
    {
        "filename": "asir_gbd.html",
        "title": "Gestión de bases de datos",
        "code": "0372",
        "weekly": "6",
        "desc": "Diseño, consulta y manipulación de bases de datos relacionales y diseño lógico y conceptual.",
        "course": "1º Curso ASIR"
    },
    {
        "filename": "asir_iso.html",
        "title": "Implantación de sistemas operativos",
        "code": "0369",
        "weekly": "7",
        "desc": "Instalación, configuración y administración de sistemas operativos monousuario y en red.",
        "course": "1º Curso ASIR"
    },
    {
        "filename": "asir_lmsgi.html",
        "title": "Lenguajes de marcas y sistemas de gestión de información",
        "code": "0373",
        "weekly": "3",
        "desc": "Lenguajes de marcado (XML, HTML), hojas de estilo y sistemas de información empresarial.",
        "course": "1º Curso ASIR"
    },
    {
        "filename": "asir_par.html",
        "title": "Planificación y administración de redes",
        "code": "0370",
        "weekly": "6",
        "desc": "Diseño, configuración, interconexión y gestión de redes de área local y extensa.",
        "course": "1º Curso ASIR"
    },
    {
        "filename": "asir_ipe1.html",
        "title": "Itinerario personal para la empleabilidad I",
        "code": "1709",
        "weekly": "3",
        "desc": "Orientación laboral, derechos y deberes, y prevención de riesgos laborales.",
        "course": "1º Curso ASIR"
    },
    {
        "filename": "asir_asgbd.html",
        "title": "Administración de sistemas gestores de bases de datos",
        "code": "0375",
        "weekly": "3",
        "desc": "Administración, rendimiento y seguridad de sistemas gestores de bases de datos y bases de datos distribuidas.",
        "course": "2º Curso ASIR"
    },
    {
        "filename": "asir_aso.html",
        "title": "Administración de sistemas operativos",
        "code": "0374",
        "weekly": "5",
        "desc": "Administración avanzada de sistemas operativos de servidor, directorios activos y automatización.",
        "course": "2º Curso ASIR"
    },
    {
        "filename": "asir_iaw.html",
        "title": "Implantación de aplicaciones web",
        "code": "0377",
        "weekly": "3",
        "desc": "Instalación y configuración de servidores web, de aplicaciones y gestores de contenido.",
        "course": "2º Curso ASIR"
    },
    {
        "filename": "asir_sad.html",
        "title": "Seguridad y alta disponibilidad",
        "code": "0378",
        "weekly": "5",
        "desc": "Implementación de medidas de seguridad activa y pasiva, copias de seguridad y sistemas de alta disponibilidad.",
        "course": "2º Curso ASIR"
    },
    {
        "filename": "asir_sri.html",
        "title": "Servicios de red e internet",
        "code": "0376",
        "weekly": "5",
        "desc": "Instalación, configuración y administración de servicios de red e internet (DNS, DHCP, correo, web, FTP).",
        "course": "2º Curso ASIR"
    },
    {
        "filename": "asir_ip.html",
        "title": "Inglés profesional",
        "code": "0179",
        "weekly": "2",
        "desc": "Comunicación en lengua inglesa en el entorno profesional del sector informático.",
        "course": "2º Curso ASIR"
    },
    {
        "filename": "asir_ipe2.html",
        "title": "Itinerario personal para la empleabilidad II",
        "code": "1710",
        "weekly": "2",
        "desc": "Habilidades sociales, trabajo en equipo, liderazgo y emprendimiento.",
        "course": "2º Curso ASIR"
    },
    {
        "filename": "asir_sa.html",
        "title": "Sostenibilidad Aplicada",
        "code": "1708",
        "weekly": "1",
        "desc": "Criterios de sostenibilidad y protección ambiental en el sector productivo.",
        "course": "2º Curso ASIR"
    },
    {
        "filename": "asir_da.html",
        "title": "Digitalización Aplicada",
        "code": "1665",
        "weekly": "1",
        "desc": "Competencias digitales aplicadas a los sectores productivos y transformación digital.",
        "course": "2º Curso ASIR"
    },
    {
        "filename": "asir_proy.html",
        "title": "Proyecto intermodular de administración de sistemas informáticos en red",
        "code": "0379",
        "weekly": "0",
        "desc": "Proyecto final de ciclo de ASIR.",
        "course": "2º Curso ASIR"
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
    if not module_info or 'learning_results' not in module_info:
        return '<div class="space-y-4"><!-- No data available --></div>'

    html_parts = ['<div class="space-y-4">']

    for ra in module_info['learning_results']:
        ra_id = ra['id']
        ra_desc = ra['description']
        criteria_html = '\n'.join([
            f'<li class="flex items-start gap-2"><span class="text-blue-500 mt-1">•</span> {crit}</li>'
            for crit in ra['evaluation_criteria']
        ])

        html_parts.append(f"""
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
        """)
    html_parts.append('</div>')
    return ''.join(html_parts)

def generate_contents_html(module_info):
    if not module_info or 'contents' not in module_info:
        return '<div class="grid grid-cols-1 md:grid-cols-2 gap-6"><!-- No data available --></div>'

    blocks = parse_contents(module_info)
    colors = ["blue", "orange", "green", "purple"]
    html_parts = ['<div class="grid grid-cols-1 md:grid-cols-2 gap-6">']

    for i, block in enumerate(blocks):
        color = colors[i % len(colors)]
        items_html = "\n".join([f'<li>{item}</li>' for item in block['items']])

        html_parts.append(f"""
                <div class="card p-6 border-l-4 border-l-{color}-500">
                    <h4 class="text-lg font-bold text-slate-800 mb-3">{block['title']}</h4>
                    <ul class="text-sm text-slate-600 space-y-1 list-disc pl-4">
                        {items_html}
                    </ul>
                </div>
        """)

    html_parts.append('</div>')
    return "".join(html_parts)

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
        acronym = meta['filename'].replace('asir_', '').replace('.html', '')

        content = template_content

        # 1. Title
        start_title = content.find('<title>')
        end_title = content.find('</title>')
        if start_title != -1:
            content = content[:start_title+7] + f"{meta['title']} (ASIR) - Módulo {code}" + content[end_title:]

        content = re.sub(r'<h2 class="text-4xl md:text-5xl font-extrabold mb-4 leading-tight">.*?</h2>',
                         f'<h2 class="text-4xl md:text-5xl font-extrabold mb-4 leading-tight">{meta["title"]}</h2>',
                         content)

        # 2. Course Badge - Change color to blue for ASIR? The user likes blue for ASIR in index.
        content = re.sub(r'<div class="inline-block bg-orange-500 text-white text-xs font-bold px-3 py-1 rounded-full mb-4">.*?</div>',
                         f'<div class="inline-block bg-blue-900 text-white text-xs font-bold px-3 py-1 rounded-full mb-4">{meta["course"]}</div>',
                         content)

        # Update the main background class specifically for ASIR
        content = re.sub(r'from-slate-800 to-slate-900', 'from-blue-800 to-blue-900', content)
        content = re.sub(r'bg-orange-500', 'bg-blue-600', content) # replacing some orange accents
        content = re.sub(r'text-orange-400', 'text-blue-300', content) # replacing some orange text accents

        # Change the main FP DAM logo to FP ASIR
        content = content.replace('FP <span class="text-orange-500">DAM</span>', 'FP <span class="text-blue-900">ASIR</span>')


        # 3. Description
        content = re.sub(r'<p class="text-xl text-slate-300 max-w-2xl">.*?</p>',
                         f'<p class="text-xl text-slate-300 max-w-2xl">Módulo Profesional {code}. {meta["desc"]}</p>',
                         content, flags=re.DOTALL)

        # 4. Stats
        # ECTS
        content = re.sub(r'(<p class="text-3xl font-black text-white">).*?(</p>\s*<p class="text-xs text-slate-400 uppercase font-bold tracking-wider">ECTS</p>)',
                         f'\\g<1>{ects}\\g<2>', content)

        # Code
        content = re.sub(r'(<p class="text-3xl font-black text-blue-300">).*?(</p>\s*<p class="text-xs text-slate-400 uppercase font-bold tracking-wider">Código</p>)',
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

        # Handle Relations Page Generation and Link - Remove it for ASIR
        # Remove the link button if no content (or if we don't want to generate a blank page)
        # The template has: <div class="mt-4"><a href="dam_di_relaciones.html" ... </div>
        # We regex replace it to empty string.
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

        # Make sure the backlink points to asir.html
        content = content.replace('href="dam.html"', 'href="asir.html"')

        output_filename = f"asir/{meta['filename']}"
        with open(output_filename, "w", encoding="utf-8") as out:
            out.write(content)

        print(f"Generated {output_filename}")

if __name__ == "__main__":
    generate_pages()
