import os

# Base template from dam_di.html (simulated, I will read the actual file in the script)
TEMPLATE_FILE = "dam_di.html"

# Module Data
MODULES = [
    {
        "filename": "dam_si.html",
        "title": "Sistemas Informáticos",
        "code": "0483",
        "ects": "11",
        "hours": "205",
        "weekly": "6",
        "desc": "Módulo Profesional 0483. Configuración, administración y mantenimiento de sistemas informáticos, hardware, software y redes locales.",
        "course": "1º Curso DAM"
    },
    {
        "filename": "dam_bd.html",
        "title": "Bases de Datos",
        "code": "0484",
        "ects": "12",
        "hours": "205",
        "weekly": "6",
        "desc": "Módulo Profesional 0484. Diseño, gestión y manipulación de bases de datos relacionales y no relacionales.",
        "course": "1º Curso DAM"
    },
    {
        "filename": "dam_prog.html",
        "title": "Programación",
        "code": "0485",
        "ects": "15",
        "hours": "270",
        "weekly": "8",
        "desc": "Módulo Profesional 0485. Fundamentos de programación, estructuras de datos, programación orientada a objetos y buenas prácticas.",
        "course": "1º Curso DAM"
    },
    {
        "filename": "dam_ed.html",
        "title": "Entornos de Desarrollo",
        "code": "0487",
        "ects": "6",
        "hours": "60",
        "weekly": "2",
        "desc": "Módulo Profesional 0487. Uso de IDEs, control de versiones, optimización de código y pruebas unitarias.",
        "course": "1º Curso DAM"
    },
    {
        "filename": "dam_lm.html",
        "title": "Lenguajes de Marcas",
        "code": "0373",
        "ects": "7",
        "hours": "110",
        "weekly": "3",
        "desc": "Módulo Profesional 0373. Lenguajes de marcado (XML, HTML), hojas de estilo y sistemas de gestión de información empresarial.",
        "course": "1º Curso DAM"
    },
    {
        "filename": "dam_ipe1.html",
        "title": "Itinerario Personal para la Empleabilidad I",
        "code": "1709",
        "ects": "5",
        "hours": "100",
        "weekly": "3",
        "desc": "Módulo Profesional 1709. Orientación laboral, derechos y deberes, y prevención de riesgos laborales.",
        "course": "1º Curso DAM"
    },
    {
        "filename": "dam_da.html",
        "title": "Digitalización Aplicada",
        "code": "1665",
        "ects": "3",
        "hours": "30",
        "weekly": "1",
        "desc": "Módulo Profesional 1665. Competencias digitales aplicadas a los sectores productivos y transformación digital.",
        "course": "1º Curso DAM"
    },
    {
        "filename": "dam_ad.html",
        "title": "Acceso a Datos",
        "code": "0486",
        "ects": "10",
        "hours": "165",
        "weekly": "5",
        "desc": "Módulo Profesional 0486. Gestión de la persistencia de datos, mapeo objeto-relacional (ORM) y bases de datos nativas.",
        "course": "2º Curso DAM"
    },
    {
        "filename": "dam_pmdm.html",
        "title": "Prog. Multimedia y Disp. Móviles",
        "code": "0489",
        "ects": "7",
        "hours": "135",
        "weekly": "4",
        "desc": "Módulo Profesional 0489. Desarrollo de aplicaciones para dispositivos móviles, integración multimedia y librerías gráficas.",
        "course": "2º Curso DAM"
    },
    {
        "filename": "dam_psp.html",
        "title": "Prog. de Servicios y Procesos",
        "code": "0490",
        "ects": "5",
        "hours": "135",
        "weekly": "4",
        "desc": "Módulo Profesional 0490. Programación concurrente, programación de red y servicios telemáticos.",
        "course": "2º Curso DAM"
    },
    {
        "filename": "dam_sge.html",
        "title": "Sistemas de Gestión Empresarial",
        "code": "0491",
        "ects": "6",
        "hours": "95",
        "weekly": "3",
        "desc": "Módulo Profesional 0491. Implantación, adaptación y mantenimiento de sistemas de planificación de recursos empresariales (ERP).",
        "course": "2º Curso DAM"
    },
    {
        "filename": "dam_ip.html",
        "title": "Inglés Profesional",
        "code": "0179",
        "ects": "5",
        "hours": "50",
        "weekly": "2",
        "desc": "Módulo Profesional 0179. Comunicación en lengua inglesa en el entorno profesional del sector informático.",
        "course": "2º Curso DAM"
    },
    {
        "filename": "dam_ipe2.html",
        "title": "Itinerario Personal para la Empleabilidad II",
        "code": "1710",
        "ects": "5",
        "hours": "70",
        "weekly": "2",
        "desc": "Módulo Profesional 1710. Habilidades sociales, trabajo en equipo, liderazgo y emprendimiento.",
        "course": "2º Curso DAM"
    },
    {
        "filename": "dam_sa.html",
        "title": "Sostenibilidad Aplicada",
        "code": "1708",
        "ects": "3",
        "hours": "30",
        "weekly": "1",
        "desc": "Módulo Profesional 1708. Criterios de sostenibilidad y protección ambiental en el sector productivo.",
        "course": "2º Curso DAM"
    }
]

def generate_pages():
    # Read the template
    with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
        template_content = f.read()

    # Section placeholders for Lorem Ipsum replacement
    lorem_ra = """
            <div class="space-y-4">
                <!-- RA Generico -->
                <details class="group bg-white rounded-xl border border-slate-200 overflow-hidden transition-all duration-300 open:shadow-lg open:ring-1 open:ring-blue-500">
                    <summary class="flex justify-between items-center cursor-pointer p-5 bg-slate-50 hover:bg-slate-100 font-bold text-slate-800 select-none">
                        <div class="flex items-center gap-3">
                            <span class="bg-blue-600 text-white text-xs px-2 py-1 rounded font-mono">RA 1</span>
                            <span>Resultado de Aprendizaje Genérico 1</span>
                        </div>
                        <span class="group-open:rotate-180 transition-transform text-slate-400">▼</span>
                    </summary>
                    <div class="p-6 border-t border-slate-200 bg-white">
                        <p class="text-sm text-slate-600 mb-4 italic">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                        <ul class="space-y-2 text-sm text-slate-700">
                            <li class="flex items-start gap-2"><span class="text-blue-500 mt-1">•</span> Lorem ipsum dolor sit amet, consectetur adipiscing elit.</li>
                            <li class="flex items-start gap-2"><span class="text-blue-500 mt-1">•</span> Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</li>
                            <li class="flex items-start gap-2"><span class="text-blue-500 mt-1">•</span> Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.</li>
                        </ul>
                    </div>
                </details>

                <details class="group bg-white rounded-xl border border-slate-200 overflow-hidden transition-all duration-300 open:shadow-lg open:ring-1 open:ring-blue-500">
                    <summary class="flex justify-between items-center cursor-pointer p-5 bg-slate-50 hover:bg-slate-100 font-bold text-slate-800 select-none">
                        <div class="flex items-center gap-3">
                            <span class="bg-blue-600 text-white text-xs px-2 py-1 rounded font-mono">RA 2</span>
                            <span>Resultado de Aprendizaje Genérico 2</span>
                        </div>
                        <span class="group-open:rotate-180 transition-transform text-slate-400">▼</span>
                    </summary>
                    <div class="p-6 border-t border-slate-200 bg-white">
                        <p class="text-sm text-slate-600 mb-4 italic">Duis aute irure dolor in reprehenderit.</p>
                        <ul class="space-y-2 text-sm text-slate-700">
                            <li class="flex items-start gap-2"><span class="text-blue-500 mt-1">•</span> Excepteur sint occaecat cupidatat non proident.</li>
                            <li class="flex items-start gap-2"><span class="text-blue-500 mt-1">•</span> Sunt in culpa qui officia deserunt mollit anim id est laborum.</li>
                        </ul>
                    </div>
                </details>

                 <details class="group bg-white rounded-xl border border-slate-200 overflow-hidden transition-all duration-300 open:shadow-lg open:ring-1 open:ring-blue-500">
                    <summary class="flex justify-between items-center cursor-pointer p-5 bg-slate-50 hover:bg-slate-100 font-bold text-slate-800 select-none">
                        <div class="flex items-center gap-3">
                            <span class="bg-blue-600 text-white text-xs px-2 py-1 rounded font-mono">RA 3</span>
                            <span>Resultado de Aprendizaje Genérico 3</span>
                        </div>
                        <span class="group-open:rotate-180 transition-transform text-slate-400">▼</span>
                    </summary>
                    <div class="p-6 border-t border-slate-200 bg-white">
                        <p class="text-sm text-slate-600 mb-4 italic">Magna aliqua ut enim ad minim veniam.</p>
                        <ul class="space-y-2 text-sm text-slate-700">
                            <li class="flex items-start gap-2"><span class="text-blue-500 mt-1">•</span> Quis nostrud exercitation ullamco laboris nisi ut aliquip.</li>
                            <li class="flex items-start gap-2"><span class="text-blue-500 mt-1">•</span> Duis aute irure dolor in reprehenderit in voluptate velit esse.</li>
                        </ul>
                    </div>
                </details>
            </div>
    """

    lorem_contenidos = """
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div class="card p-6 border-l-4 border-l-blue-500">
                    <h4 class="text-lg font-bold text-slate-800 mb-3">Bloque de Contenido 1</h4>
                    <ul class="text-sm text-slate-600 space-y-1 list-disc pl-4">
                        <li>Lorem ipsum dolor sit amet.</li>
                        <li>Consectetur adipiscing elit.</li>
                        <li>Sed do eiusmod tempor incididunt.</li>
                    </ul>
                </div>

                <div class="card p-6 border-l-4 border-l-orange-500">
                    <h4 class="text-lg font-bold text-slate-800 mb-3">Bloque de Contenido 2</h4>
                    <ul class="text-sm text-slate-600 space-y-1 list-disc pl-4">
                        <li>Ut enim ad minim veniam.</li>
                        <li>Quis nostrud exercitation.</li>
                        <li>Ullamco laboris nisi ut aliquip.</li>
                    </ul>
                </div>

                <div class="card p-6 border-l-4 border-l-blue-500">
                    <h4 class="text-lg font-bold text-slate-800 mb-3">Bloque de Contenido 3</h4>
                    <ul class="text-sm text-slate-600 space-y-1 list-disc pl-4">
                        <li>Duis aute irure dolor.</li>
                        <li>Reprehenderit in voluptate.</li>
                        <li>Velit esse cillum dolore.</li>
                    </ul>
                </div>

                <div class="card p-6 border-l-4 border-l-orange-500">
                    <h4 class="text-lg font-bold text-slate-800 mb-3">Bloque de Contenido 4</h4>
                    <ul class="text-sm text-slate-600 space-y-1 list-disc pl-4">
                        <li>Excepteur sint occaecat.</li>
                        <li>Cupidatat non proident.</li>
                        <li>Sunt in culpa qui officia.</li>
                    </ul>
                </div>
            </div>
    """

    for module in MODULES:
        content = template_content

        # 1. Replace Title in <title> and <h2>
        content = content.replace("Desarrollo de Interfaces (DAM) - Módulo 0488", f"{module['title']} (DAM) - Módulo {module['code']}")
        content = content.replace('<h2 class="text-4xl md:text-5xl font-extrabold mb-4 leading-tight">Desarrollo de Interfaces</h2>', f'<h2 class="text-4xl md:text-5xl font-extrabold mb-4 leading-tight">{module["title"]}</h2>')

        # 2. Replace Course Badge
        content = content.replace("2º Curso DAM", module['course'])

        # 3. Replace Description
        # Need to find the p tag. It's unique enough.
        # "Módulo Profesional 0488. Diseño y implementación..."
        start_desc = content.find('<p class="text-xl text-slate-300 max-w-2xl">')
        end_desc = content.find('</p>', start_desc)
        if start_desc != -1:
            old_desc = content[start_desc:end_desc+4]
            new_desc = f'<p class="text-xl text-slate-300 max-w-2xl">\n                    {module["desc"]}\n                </p>'
            content = content.replace(old_desc, new_desc)

        # 4. Replace Stats (ECTS, Code, Hours, Weekly)
        # ECTS
        content = content.replace('<p class="text-3xl font-black text-white">10</p>', f'<p class="text-3xl font-black text-white">{module["ects"]}</p>', 1)
        # Code
        content = content.replace('<p class="text-3xl font-black text-orange-400">0488</p>', f'<p class="text-3xl font-black text-orange-400">{module["code"]}</p>')
        # Hours
        content = content.replace('<p class="text-3xl font-black text-white">150</p>', f'<p class="text-3xl font-black text-white">{module["hours"]}</p>')
        # Weekly
        content = content.replace('<p class="text-3xl font-black text-white">5</p>', f'<p class="text-3xl font-black text-white">{module["weekly"]}</p>')

        # 5. Replace "Resultados de Aprendizaje" section
        # We look for the div id="resultados" and replace the inner content below the header
        # The structure is: <section id="resultados"> ... <div class="space-y-4"> ... </div> </section>

        # Easier strategy: Replace the entire <div class="space-y-4">...</div> block inside #resultados
        start_ra = content.find('<div class="space-y-4">')
        end_ra = content.find('</section>', start_ra)
        # Find the last closing div of that section (it closes the space-y-4)
        # Actually, let's just find the closing tag before </section>
        if start_ra != -1:
            # We need to find the matching closing div for space-y-4.
            # Since the structure is consistent in the template, we can cut from <div class="space-y-4"> to the last </div> before </section>
            # But the template has many nested divs.
            # Let's verify the template structure. The section #resultados ends with </section>.
            # The div class="space-y-4" contains all the details.
            # We can replace from <div class="space-y-4"> up to the </div> that comes before </section>.
            # Let's count divs or use a simpler marker.

            # The section ends with:
            #     </div>
            # </section>

            # So we can search for the last </div> before </section>
            last_div = content.rfind('</div>', 0, end_ra)
            old_ra_block = content[start_ra:last_div+6]
            content = content.replace(old_ra_block, lorem_ra)

        # 6. Replace "Contenidos Básicos" section
        # <section id="contenidos"> ... <div class="grid grid-cols-1 md:grid-cols-2 gap-6"> ... </div> </section>
        start_con = content.find('<div class="grid grid-cols-1 md:grid-cols-2 gap-6">')
        end_con = content.find('</section>', start_con)
        if start_con != -1:
            last_div_con = content.rfind('</div>', 0, end_con)
            old_con_block = content[start_con:last_div_con+6]
            content = content.replace(old_con_block, lorem_contenidos)

        # Write file
        with open(module['filename'], "w", encoding="utf-8") as out:
            out.write(content)

        print(f"Generated {module['filename']}")

if __name__ == "__main__":
    generate_pages()
