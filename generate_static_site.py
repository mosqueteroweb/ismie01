import os
import re
import markdown
import glob
import html

SOURCE_DIR = "sirev"
DEST_DIR = "docsi"

# Tailwind Colors and Styles based on the image
THEME = {
    "bg_body": "bg-[#F3FDE8]",
    "text_main": "text-gray-800",
    "text_green": "text-[#008037]",
    "card_bg": "bg-white",
    "card_border": "border-[#008037]",
    "number_bg": "bg-[#00A859]",
}

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css" rel="stylesheet" />
    <script type="module">
        import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
        mermaid.initialize({{ startOnLoad: true }});
    </script>
    <style>
        .markdown-content h3 {{ font-size: 1.25rem; font-weight: 600; color: #008037; margin-top: 1.5rem; margin-bottom: 0.5rem; }}
        .markdown-content p {{ margin-bottom: 1rem; color: #374151; }}
        .markdown-content ul {{ list-style-type: disc; padding-left: 1.5rem; margin-bottom: 1rem; color: #374151; }}
        .markdown-content li {{ margin-bottom: 0.25rem; }}
        .markdown-content strong {{ font-weight: 600; color: #111827; }}
        .markdown-content pre {{ background-color: #1f2937; color: #f3f4f6; padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem; overflow-x: auto; position: relative; }}
        .markdown-content code {{ font-family: monospace; }}
        .markdown-content table {{ width: 100%; border-collapse: collapse; margin-bottom: 1rem; }}
        .markdown-content th, .markdown-content td {{ border: 1px solid #e5e7eb; padding: 0.75rem; text-align: left; }}
        .markdown-content th {{ background-color: #f9fafb; font-weight: 600; color: #374151; }}

        /* Transition for accordion */
        .accordion-content {{
            transition: max-height 0.3s ease-out, opacity 0.3s ease-out;
            max-height: 0;
            opacity: 0;
            overflow: hidden;
        }}
        .accordion-content.open {{
            max-height: 5000px; /* Arbitrary large number to allow content to expand */
            opacity: 1;
            padding-top: 1rem;
            padding-bottom: 1rem;
        }}
        .rotate-180 {{ transform: rotate(180deg); }}
        .copy-btn {{
            position: absolute; top: 0.5rem; right: 0.5rem; background: #374151; color: white; padding: 0.2rem 0.5rem; border-radius: 0.25rem; font-size: 0.75rem; cursor: pointer; border: none;
        }}
        .copy-btn:hover {{ background: #4b5563; }}
    </style>
</head>
<body class="{body_class} font-sans min-h-screen p-8 relative">
    {back_button}
    <div class="max-w-4xl mx-auto">
        <header class="mb-10">
            <h1 class="text-3xl font-bold {text_green} mb-2">{title}</h1>
            <p class="text-gray-500 text-sm uppercase">{subtitle}</p>
        </header>

        <div class="space-y-6">
            {content}
        </div>
    </div>

    <script>
        // Accordion Logic
        function toggleAccordion(id) {{
            const content = document.getElementById('content-' + id);
            const icon = document.getElementById('icon-' + id);

            if (content.classList.contains('open')) {{
                content.classList.remove('open');
                icon.classList.remove('rotate-180');
            }} else {{
                content.classList.add('open');
                icon.classList.add('rotate-180');
            }}
        }}

        // Copy Code Logic
        document.querySelectorAll('pre').forEach((block) => {{
            if(block.classList.contains('mermaid')) return; // skip mermaid

            const button = document.createElement('button');
            button.className = 'copy-btn';
            button.innerText = 'Copiar';
            block.appendChild(button);

            button.addEventListener('click', async () => {{
                const code = block.querySelector('code').innerText;
                try {{
                    await navigator.clipboard.writeText(code);
                    button.innerText = '¡Copiado!';
                    setTimeout(() => {{ button.innerText = 'Copiar'; }}, 2000);
                }} catch (err) {{
                    console.error('Failed to copy', err);
                }}
            }});
        }});
    </script>
</body>
</html>
"""

ACCORDION_TEMPLATE = """
<div class="bg-white rounded-xl shadow-sm border-l-8 border-[#00A859] overflow-hidden">
    <button onclick="toggleAccordion('{id}')" class="w-full flex items-center justify-between p-6 bg-white hover:bg-gray-50 transition-colors focus:outline-none">
        <div class="flex items-center gap-6">
            <div class="bg-[#00A859] text-white text-xl font-bold rounded-lg w-12 h-12 flex items-center justify-center shrink-0">
                {number}
            </div>
            <div class="text-left">
                <h2 class="text-xl font-bold text-gray-900">{title}</h2>
                {subtitle_html}
            </div>
        </div>
        <svg id="icon-{id}" class="w-6 h-6 text-gray-400 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
        </svg>
    </button>
    <div id="content-{id}" class="accordion-content px-6 markdown-content border-t border-gray-100">
        {content}
    </div>
</div>
"""

def parse_markdown_to_accordions(md_content):
    # Some markdown files use different newline characters
    lines = md_content.splitlines()
    accordions = []
    current_accordion = None

    # Simple state machine to capture code blocks and mermaid
    in_code_block = False
    code_block_type = ""
    current_code_content = []

    for line in lines:
        is_opening = not in_code_block and line.startswith('```')
        is_closing = in_code_block and (line.startswith('```') or line.startswith('´´´'))

        if is_opening:
            in_code_block = True
            code_block_type = line[3:].strip()
            current_code_content = []
            continue
        elif is_closing:
            in_code_block = False
            code_content = "\n".join(current_code_content)
            if current_accordion:
                if code_block_type == 'mermaid':
                    current_accordion['content'] += f'<pre class="mermaid">{html.escape(code_content)}</pre>\n'
                else:
                    lang_class = f'language-{code_block_type}' if code_block_type else 'language-none'
                    current_accordion['content'] += f'<pre><code class="{lang_class}">{html.escape(code_content)}</code></pre>\n'
            continue

        if in_code_block:
            current_code_content.append(line)
            continue

        if line.startswith('## '):
            if current_accordion:
                accordions.append(current_accordion)

            title = line[3:].strip()
            current_accordion = {
                'title': title,
                'subtitle': '',
                'content': ''
            }
        elif line.startswith('### ') and current_accordion and not current_accordion['content'].strip() and not current_accordion['subtitle']:
            # If it's H3 right after H2, make it a subtitle of the accordion
            current_accordion['subtitle'] = line[4:].strip()
        elif current_accordion:
             current_accordion['content'] += line + '\n'

    if current_accordion:
        accordions.append(current_accordion)

    return accordions

def generate_html_content(accordions):
    html_output = ""
    for i, acc in enumerate(accordions):
        num_str = f"{i+1:02d}"

        # Convert markdown content to HTML
        html_content = markdown.markdown(acc['content'], extensions=['tables'])

        subtitle_html = f'<p class="text-sm text-gray-500 uppercase mt-1">{acc["subtitle"]}</p>' if acc['subtitle'] else ''

        html_output += ACCORDION_TEMPLATE.format(
            id=f"acc-{i}",
            number=num_str,
            title=acc['title'],
            subtitle_html=subtitle_html,
            content=html_content
        )
    return html_output

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def process_files():
    create_directory(DEST_DIR)

    md_files = glob.glob(os.path.join(SOURCE_DIR, "*.md"))

    # Dictionary to hold RA relations: RA_Number -> {'teoria': link, 'practicas': link, 'evaluacion': link}
    ra_data = {}

    for md_file in md_files:
        filename = os.path.basename(md_file)
        if filename.lower() == 'readme.md': continue

        # Parse filename e.g., RA1_Teoria_rev.md
        match = re.match(r'(RA\d+)_([A-Za-zñáéíóú]+)_', filename)
        if match:
            ra_id = match.group(1)
            type_id = match.group(2).lower()

            # map variations of practicas
            if "practica" in type_id:
                type_id = "practicas"

            if ra_id not in ra_data:
                ra_data[ra_id] = {}

            out_filename = filename.replace('.md', '.html')
            ra_data[ra_id][type_id] = out_filename

            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            accordions = parse_markdown_to_accordions(content)
            html_content = generate_html_content(accordions)

            title = f"{type_id.capitalize()} {ra_id}"

            back_btn = f'<a href="{ra_id}.html" class="absolute top-8 right-8 bg-white border border-gray-200 text-gray-700 px-4 py-2 rounded-lg shadow-sm hover:bg-gray-50 flex items-center gap-2"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg> Volver a {ra_id}</a>'

            full_html = HTML_TEMPLATE.format(
                title=title,
                subtitle=f"MÓDULO DE SISTEMAS INFORMÁTICOS",
                body_class=THEME['bg_body'],
                text_green=THEME['text_green'],
                back_button=back_btn,
                content=html_content
            )

            out_path = os.path.join(DEST_DIR, out_filename)
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(full_html)

    return ra_data

def generate_ra_pages(ra_data):
    for ra_id, links in ra_data.items():
        cards_html = ""
        types = [('teoria', 'Teoría'), ('practicas', 'Práctica'), ('evaluacion', 'Evaluación')]

        for type_key, label in types:
            if type_key in links:
                link = links[type_key]
                cards_html += f'''
                <a href="{link}" class="block bg-white rounded-xl shadow-sm border-l-8 border-[#00A859] p-8 hover:shadow-md transition-shadow">
                    <h2 class="text-2xl font-bold text-gray-900 mb-2">{label}</h2>
                    <p class="text-gray-500">Acceder al contenido de {label.lower()} para el {ra_id}</p>
                </a>
                '''

        back_btn = f'<a href="index.html" class="absolute top-8 right-8 bg-white border border-gray-200 text-gray-700 px-4 py-2 rounded-lg shadow-sm hover:bg-gray-50 flex items-center gap-2"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg> Volver a Inicio</a>'

        full_html = HTML_TEMPLATE.format(
            title=f"Contenidos del {ra_id}",
            subtitle="SELECCIONA UNA SECCIÓN",
            body_class=THEME['bg_body'],
            text_green=THEME['text_green'],
            back_button=back_btn,
            content=f'<div class="grid grid-cols-1 md:grid-cols-3 gap-6">{cards_html}</div>'
        )

        out_path = os.path.join(DEST_DIR, f"{ra_id}.html")
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(full_html)

def generate_index_page(ra_data):
    cards_html = ""
    sorted_ras = sorted(ra_data.keys(), key=lambda x: int(x.replace('RA', '')))

    for ra_id in sorted_ras:
        cards_html += f'''
        <a href="{ra_id}.html" class="block bg-white rounded-xl shadow-sm border-l-8 border-[#00A859] p-6 hover:shadow-md transition-shadow">
            <h2 class="text-xl font-bold text-gray-900">{ra_id}</h2>
            <p class="text-sm text-gray-500 mt-2">Ver teoría, prácticas y evaluación</p>
        </a>
        '''

    full_html = HTML_TEMPLATE.format(
        title="Índice de Resultados de Aprendizaje",
        subtitle="MÓDULO DE SISTEMAS INFORMÁTICOS",
        body_class=THEME['bg_body'],
        text_green=THEME['text_green'],
        back_button='',
        content=f'<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">{cards_html}</div>'
    )

    out_path = os.path.join(DEST_DIR, "index.html")
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(full_html)

if __name__ == "__main__":
    ra_data = process_files()
    generate_ra_pages(ra_data)
    generate_index_page(ra_data)
    print("Static site generated successfully in 'docsi/' directory.")
