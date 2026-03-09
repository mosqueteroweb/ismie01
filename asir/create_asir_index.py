import os

MODULES_YR1 = [
    {"filename": "asir_fh.html", "title": "Fundamentos de hardware", "code": "0371"},
    {"filename": "asir_gbd.html", "title": "Gestión de bases de datos", "code": "0372"},
    {"filename": "asir_iso.html", "title": "Implantación de sistemas operativos", "code": "0369"},
    {"filename": "asir_lmsgi.html", "title": "Lenguajes de marcas y sistemas de gestión de información", "code": "0373"},
    {"filename": "asir_par.html", "title": "Planificación y administración de redes", "code": "0370"},
    {"filename": "asir_ipe1.html", "title": "Itinerario personal para la empleabilidad I", "code": "1709"},
    {"filename": "#", "title": "Módulo Profesional Optativo", "code": "OPT1"},
]

MODULES_YR2 = [
    {"filename": "asir_asgbd.html", "title": "Administración de sistemas gestores de bases de datos", "code": "0375"},
    {"filename": "asir_aso.html", "title": "Administración de sistemas operativos", "code": "0374"},
    {"filename": "asir_iaw.html", "title": "Implantación de aplicaciones web", "code": "0377"},
    {"filename": "asir_sad.html", "title": "Seguridad y alta disponibilidad", "code": "0378"},
    {"filename": "asir_sri.html", "title": "Servicios de red e internet", "code": "0376"},
    {"filename": "asir_ip.html", "title": "Inglés profesional", "code": "0179"},
    {"filename": "asir_ipe2.html", "title": "Itinerario personal para la empleabilidad II", "code": "1710"},
    {"filename": "asir_sa.html", "title": "Sostenibilidad Aplicada", "code": "1708"},
    {"filename": "asir_da.html", "title": "Digitalización Aplicada", "code": "1665"},
    {"filename": "#", "title": "Módulo Profesional Optativo", "code": "OPT2"},
    {"filename": "asir_proy.html", "title": "Proyecto intermodular de administración de sistemas informáticos en red", "code": "0379"},
]

INDEX_FILENAME = "asir/asir.html"
BACK_LINK_OLD = '<a href="../index.html" class="text-slate-400 hover:text-blue-600 transition-colors">'
BACK_LINK_NEW = '<a href="asir.html" class="text-slate-400 hover:text-blue-600 transition-colors">'

def create_card(module):
    tag = "a" if module['filename'] != "#" else "div"
    href = f' href="{module["filename"]}"' if module['filename'] != "#" else ""

    return f"""
            <{tag}{href} class="block group">
                <div class="bg-white rounded-xl border border-slate-200 p-6 shadow-sm hover:shadow-md transition-all duration-300 hover:-translate-y-1 relative overflow-hidden">
                    <div class="absolute top-0 right-0 p-4 opacity-10 group-hover:opacity-20 transition-opacity">
                        <span class="text-6xl font-black text-slate-800">{module['code']}</span>
                    </div>
                    <div class="relative z-10">
                        <span class="inline-block bg-blue-100 text-blue-700 text-xs font-bold px-2 py-1 rounded mb-3">Módulo {module['code']}</span>
                        <h3 class="text-xl font-bold text-slate-800 leading-tight group-hover:text-blue-600 transition-colors">{module['title']}</h3>
                    </div>
                </div>
            </{tag}>
    """

def create_index_page():
    cards_yr1 = "\n".join([create_card(m) for m in MODULES_YR1])
    cards_yr2 = "\n".join([create_card(m) for m in MODULES_YR2])

    html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FP ASIR - Módulos Formativos</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700;900&display=swap" rel="stylesheet">
    <style>
        body {{
            font-family: 'Roboto', sans-serif;
            background-color: #f8fafc;
        }}
    </style>
</head>
<body class="antialiased min-h-screen flex flex-col">

    <!-- Header -->
    <header class="bg-white shadow-sm sticky top-0 z-50 border-b border-gray-100">
        <div class="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
            <div class="flex items-center gap-4">
                <a href="../index.html" class="text-slate-400 hover:text-blue-600 transition-colors">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
                    </svg>
                </a>
                <h1 class="text-2xl font-bold text-slate-800 tracking-tight">FP <span class="text-blue-900">ASIR</span></h1>
            </div>
        </div>
    </header>

    <main class="flex-grow max-w-7xl mx-auto px-6 py-12 space-y-16 w-full">

        <!-- 1º Curso -->
        <section>
            <div class="flex items-center gap-4 mb-8">
                <div class="h-10 w-2 bg-blue-500 rounded-full"></div>
                <h2 class="text-3xl font-black text-slate-900">1º Curso</h2>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
                {cards_yr1}
            </div>
        </section>

        <!-- 2º Curso -->
        <section>
            <div class="flex items-center gap-4 mb-8">
                <div class="h-10 w-2 bg-orange-500 rounded-full"></div>
                <h2 class="text-3xl font-black text-slate-900">2º Curso</h2>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
                {cards_yr2}
            </div>
        </section>

    </main>

    <footer class="bg-white border-t border-slate-200 mt-auto py-12">
        <div class="max-w-7xl mx-auto px-6 text-center text-slate-400 text-sm">
            <p>Autor &copy; Pedro Salazar 2026</p>
        </div>
    </footer>

</body>
</html>
"""
    with open(INDEX_FILENAME, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Created {INDEX_FILENAME}")

def update_module_pages():
    all_modules = MODULES_YR1 + MODULES_YR2
    for module in all_modules:
        filename = "asir/" + module['filename']
        if module['filename'] == "#": continue # Skip modules without files
        if not os.path.exists(filename):
            # print(f"Warning: {filename} does not exist yet.")
            continue

        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()

        if BACK_LINK_OLD in content:
            new_content = content.replace(BACK_LINK_OLD, BACK_LINK_NEW)
            with open(filename, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated back link in {filename}")
        elif BACK_LINK_NEW in content:
            print(f"Back link already updated in {filename}")
        else:
            print(f"Warning: Back link not found in {filename}")

if __name__ == "__main__":
    create_index_page()
    update_module_pages()
