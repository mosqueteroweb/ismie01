import json

def fix_module_0179():
    with open('module_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    if '0179' in data:
        print("Fixing module 0179...")
        # Keep only the first 5 RAs (which correspond to English)
        # The IDs are strings "1" to "5".
        # We can just slice the list if we are sure the first 5 are correct.
        # Let's verify by checking the description of the 6th element (index 5)
        ras = data['0179']['learning_results']
        if len(ras) > 5:
            print(f"Removing {len(ras) - 5} extra RAs.")
            data['0179']['learning_results'] = ras[:5]

        # Populate contents
        data['0179']['contents'] = [
            "Análisis de mensajes orales:",
            "−\tComprensión de mensajes profesionales y cotidianos.",
            "−\tMensajes directos, telefónicos y grabados.",
            "−\tTerminología específica del sector.",
            "−\tIdea principal y detalles secundarios.",
            "−\tMensajes con diferentes registros.",
            "Interpretación de mensajes escritos:",
            "−\tComprensión de mensajes, textos, artículos básicos profesionales y cotidianos.",
            "−\tSoportes telemáticos: fax, e-mail, burofax.",
            "−\tTerminología específica del sector.",
            "−\tIdea principal y detalles secundarios.",
            "−\tRelaciones lógicas: oposición, concesión, comparación, condición, causa, finalidad, resultado.",
            "−\tRelaciones temporales: anterioridad, posterioridad, simultaneidad.",
            "Producción de mensajes orales:",
            "−\tRegistros utilizados en la emisión de mensajes orales.",
            "−\tTerminología específica del sector.",
            "−\tFórmulas y saludos.",
            "−\tMantenimiento y seguimiento del discurso oral.",
            "−\tMarcadores lingüísticos de relaciones sociales, normas de cortesía y diferencias de registro.",
            "Emisión de textos escritos:",
            "−\tExpresión y cumplimentación de mensajes y textos profesionales y cotidianos.",
            "−\tCurriculum vitae y soportes telemáticos: fax, e-mail, burofax.",
            "−\tTerminología específica del sector.",
            "−\tIdea principal y detalles secundarios.",
            "−\tRelaciones lógicas: oposición, concesión, comparación, condición, causa, finalidad, resultado.",
            "−\tRelaciones temporales: anterioridad, posterioridad, simultaneidad.",
            "Identificación e interpretación de los elementos culturales:",
            "−\tElementos culturales más significativos de los países de lengua inglesa.",
            "−\tNormas de conducta y protocolo.",
            "−\tRelaciones sociales y laborales."
        ]

        with open('module_data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print("module_data.json updated successfully.")
    else:
        print("Module 0179 not found.")

if __name__ == "__main__":
    fix_module_0179()
