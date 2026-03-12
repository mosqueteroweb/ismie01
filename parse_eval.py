import os
import re
import json
import markdown

sirev_dir = 'sirev'

for filename in os.listdir(sirev_dir):
    if filename.endswith('_Evaluacion_rev.md'):
        filepath = os.path.join(sirev_dir, filename)
        new_filepath = os.path.join(sirev_dir, filename.replace('.md', '.mdx'))

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        questions = []

        # Determine the preamble
        preamble_match = re.search(r'^(.*?)(?=(###\s+Pregunta\s+1|## 1\. EXAMEN|## 1\. Examen|## 1\. PRUEBA|### 1\.\s+Pregunta|\*\*1\.\s+En el contexto))', content, re.DOTALL | re.IGNORECASE)
        preamble = preamble_match.group(1) if preamble_match else content.split('### Pregunta')[0]

        # Match anything that looks like "Pregunta X" or "**1. Question**" followed by options A, B, C, D
        question_blocks = re.finditer(r'(?:###\s*(?:Pregunta|Cuestión)\s*\d+.*?\n|\*\*\d+\.\s+.*?\n)(.*?)(?=(?:###\s*(?:Pregunta|Cuestión)\s*\d+|\*\*\d+\.\s+|##\s+2\.|##\s+CASOS|##\s+SUPUESTO|##\s+Solucionario|# PARTE 2|\Z))', content, re.DOTALL | re.IGNORECASE)

        for block_match in question_blocks:
            block = block_match.group(0)

            # Extract question text (before first option A)
            q_text_match = re.search(r'^(.*?)(?=\n\s*\*\*?[A-D][\)\.]\*\*?|\n\s*[A-D][\)\.])', block, re.DOTALL)
            if not q_text_match:
                continue
            question_text = q_text_match.group(1).strip()

            # Extract options
            options_match = re.findall(r'(?:\*\*?([A-D])[\)\.]\*\*?|([A-D])[\)\.])\s*(.*?)(?=\n\s*(?:\*\*?[A-D][\)\.]\*\*?|[A-D][\)\.])|\n\s*>|\n\s*\*|\n\n|\Z)', block, re.DOTALL)

            if len(options_match) < 2:
                continue # not a multiple choice question

            clean_options = []
            for opt in options_match:
                letter = opt[0] if opt[0] else opt[1]
                text = opt[2].strip()
                clean_options.append((letter, text))

            # Try inline first
            correct_index = 0
            justification_block = "Justificación no encontrada."

            ans_match = re.search(r'(?:Respuesta\s+Correcta:|Opción\s+Correcta:)\s*\*\*?([A-D])\*\*?', block, re.IGNORECASE)
            if ans_match:
                correct_letter = ans_match.group(1).upper()
                correct_index = ord(correct_letter) - ord('A')
                just_match = re.search(r'(?:Justificación\s+Técnica|SOLUCIÓN EXHAUSTIVA Y JUSTIFICACIÓN TÉCNICA|Justificación):?\**\s*(.*?)(?=\n\n###|\Z)', block, re.DOTALL | re.IGNORECASE)
                if just_match:
                    justification_block = just_match.group(1).strip()
                    justification_block = re.sub(r'^>\s?', '', justification_block, flags=re.MULTILINE).strip()
            else:
                # Look in Solucionario section at the end
                q_num_match = re.search(r'(?:Pregunta|Cuestión|\*\*)\s*(\d+)', question_text, re.IGNORECASE)
                if not q_num_match:
                    # In some docs the number is in the heading above
                    heading_match = re.search(r'(?:Pregunta|Cuestión)\s*(\d+)', block, re.IGNORECASE)
                    if heading_match:
                        q_num_match = heading_match

                if q_num_match:
                    q_num = q_num_match.group(1)
                    # Search entire file for the solution
                    sol_pattern = rf'(?:###\s*(?:Solución|Respuesta)?\s*(?:Pregunta|Cuestión)\s*{q_num}.*?|\*\*(?:Pregunta|Cuestión)\s*{q_num}\*\*.*?\n*|{q_num}\.\s+.*?\n*)(?:Respuesta\s+Correcta:|Opción\s+Correcta:)\s*\*\*?([A-D])\*\*?(.*?)(?=(?:###\s*(?:Solución|Respuesta)|###\s*(?:Pregunta|Cuestión)|\*\*(?:Pregunta|Cuestión)|##\s+|\d+\.\s+Respuesta|\Z))'
                    sol_match = re.search(sol_pattern, content, re.DOTALL | re.IGNORECASE)

                    if sol_match:
                        correct_letter = sol_match.group(1).upper()
                        correct_index = ord(correct_letter) - ord('A')
                        justification_block = sol_match.group(2).strip()
                        justification_block = re.sub(r'^>\s?', '', justification_block, flags=re.MULTILINE).strip()

            options_formatted = [f"**{opt[0]})** {opt[1]}" for opt in clean_options]

            questions.append({
                "question": question_text,
                "options": options_formatted,
                "correctAnswerIndex": correct_index,
                "justification": justification_block
            })

        # Generate MDX content
        mdx_content = f"---\nid: {filename.replace('.md', '')}_interactivo\ntitle: Evaluacion Interactiva ({filename[:3]})\n---\n\n"
        mdx_content += preamble.strip() + "\n\n"
        mdx_content += "import Quiz from '@site/src/components/Quiz';\n\n"

        if questions:
            mdx_content += "<Quiz questions={[\n"
            for q in questions:
                q_html = markdown.markdown(q['question'])
                options_html = [markdown.markdown(opt).replace('<p>', '').replace('</p>', '') for opt in q['options']]
                just_html = markdown.markdown(q['justification'])

                mdx_content += "  {\n"
                mdx_content += f"    question: {json.dumps(q_html)},\n"
                mdx_content += f"    options: {json.dumps(options_html)},\n"
                mdx_content += f"    correctAnswerIndex: {q['correctAnswerIndex']},\n"
                mdx_content += f"    justification: {json.dumps(just_html)}\n"
                mdx_content += "  },\n"
            mdx_content += "]} />\n\n"

        # Append the rest of the document (Casos prácticos)
        rest_of_doc_match = re.search(r'(##\s+2\..*?CASOS.*?|##\s+2\..*?Supuesto.*?|##\s+CASOS PRÁCTICOS.*?|##\s+2\..*?Ejercicios.*?|##\s+2\..*?ESCENARIOS.*|# PARTE 2.*)', content, re.DOTALL | re.IGNORECASE)
        if rest_of_doc_match:
            rest_text = rest_of_doc_match.group(1)
            solucionario_match = re.search(r'(.*?)(##\s+\d+\.\s+SOLUCIONARIO.*|##\s+SOLUCIONARIO.*|# PARTE 3: SOLUCIONARIO.*)', rest_text, re.DOTALL | re.IGNORECASE)
            if solucionario_match:
                rest_text = solucionario_match.group(1).strip()

            mdx_content += rest_text

        with open(new_filepath, 'w', encoding='utf-8') as f:
            f.write(mdx_content)
        print(f"Created {new_filepath} with {len(questions)} questions")
