import os

MODULES_YR1 = [
    {"filename": "dam_si.html", "title": "Sistemas Informáticos", "code": "0483"},
    {"filename": "dam_bd.html", "title": "Bases de Datos", "code": "0484"},
    {"filename": "dam_prog.html", "title": "Programación", "code": "0485"},
    {"filename": "dam_ed.html", "title": "Entornos de Desarrollo", "code": "0487"},
    {"filename": "dam_lm.html", "title": "Lenguajes de Marcas", "code": "0373"},
    {"filename": "dam_ipe1.html", "title": "Itinerario Personal para la Empleabilidad I", "code": "1709"},
    {"filename": "dam_da.html", "title": "Digitalización Aplicada", "code": "1665"},
]

MODULES_YR2 = [
    {"filename": "dam_di.html", "title": "Desarrollo de Interfaces", "code": "0488"},
    {"filename": "dam_ad.html", "title": "Acceso a Datos", "code": "0486"},
    {"filename": "dam_pmdm.html", "title": "Prog. Multimedia y Disp. Móviles", "code": "0489"},
    {"filename": "dam_psp.html", "title": "Prog. de Servicios y Procesos", "code": "0490"},
    {"filename": "dam_sge.html", "title": "Sistemas de Gestión Empresarial", "code": "0491"},
    {"filename": "dam_ip.html", "title": "Inglés Profesional", "code": "0179"},
    {"filename": "dam_ipe2.html", "title": "Itinerario Personal para la Empleabilidad II", "code": "1710"},
    {"filename": "dam_sa.html", "title": "Sostenibilidad Aplicada", "code": "1708"},
]

INDEX_FILENAME = "dam.html"
BACK_LINK_OLD = '<a href="infografia01c.html" class="text-slate-400 hover:text-blue-600 transition-colors">'
BACK_LINK_NEW = '<a href="dam.html" class="text-slate-400 hover:text-blue-600 transition-colors">'

def create_card(module):
    return f"""
            <a href="{module['filename']}" class="block group">
                <div class="bg-white rounded-xl border border-slate-200 p-6 shadow-sm hover:shadow-md transition-all duration-300 hover:-translate-y-1 relative overflow-hidden">
                    <div class="absolute top-0 right-0 p-4 opacity-10 group-hover:opacity-20 transition-opacity">
                        <span class="text-6xl font-black text-slate-800">{module['code']}</span>
                    </div>
                    <div class="relative z-10">
                        <span class="inline-block bg-blue-100 text-blue-700 text-xs font-bold px-2 py-1 rounded mb-3">Módulo {module['code']}</span>
                        <h3 class="text-xl font-bold text-slate-800 leading-tight group-hover:text-blue-600 transition-colors">{module['title']}</h3>
                    </div>
                </div>
            </a>
    """

def create_index_page():
    cards_yr1 = "\n".join([create_card(m) for m in MODULES_YR1])
    cards_yr2 = "\n".join([create_card(m) for m in MODULES_YR2])

    html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FP DAM - Módulos Formativos</title>
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
            <h1 class="text-2xl font-bold text-slate-800 tracking-tight">FP <span class="text-orange-500">DAM</span></h1>
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
            <p>&copy; 2024 - FP Informática y Comunicaciones</p>
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
        filename = module['filename']
        if not os.path.exists(filename):
            print(f"Warning: {filename} does not exist.")
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
