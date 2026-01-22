import json
import string
from odf.opendocument import load
from odf.table import Table, TableRow, TableCell
from odf.text import P

def get_col_letter(col_idx):
    """Converts 0-based column index to letter (A, B, C...). Assumes < 26 columns."""
    return chr(65 + col_idx)

def generate_ods():
    # 1. Load Data
    with open('module_data.json', 'r') as f:
        data = json.load(f)

    module_code = "0488"
    if module_code not in data:
        print(f"Error: Module {module_code} not found.")
        return

    module_data = data[module_code]
    ras = module_data['learning_results']
    print(f"Loaded {len(ras)} RAs for {module_data['name']}")

    # 2. Load Template
    doc = load('Prueba_RA.ods')
    spreadsheet = doc.spreadsheet
    table = spreadsheet.getElementsByType(Table)[0]
    rows = table.getElementsByType(TableRow)

    # 3. Extract Styles
    def extract_row_styles(row):
        r_style = row.getAttribute('stylename')
        cells = row.getElementsByType(TableCell)
        c_styles = [c.getAttribute('stylename') for c in cells]
        return r_style, c_styles

    if len(rows) > 12:
        ra_row_style, ra_cell_styles = extract_row_styles(rows[3])
        crit_row_style, crit_cell_styles = extract_row_styles(rows[4])
        note_row_style, note_cell_styles = extract_row_styles(rows[12])
    else:
        print("Error: Template has fewer rows than expected.")
        return

    print("Styles extracted.")

    # 4. Truncate Table
    rows_to_keep = 3
    nodes_to_remove = rows[rows_to_keep:]
    for node in nodes_to_remove:
        table.removeChild(node)

    print(f"Truncated table to {rows_to_keep} rows.")

    # 5. Rebuild Table
    current_row_idx = 4

    for ra in ras:
        # --- RA Row ---
        ra_row = TableRow(stylename=ra_row_style)

        # Cell A: Description
        tc = TableCell(stylename=ra_cell_styles[0] if len(ra_cell_styles)>0 else None,
                       valuetype="string")
        tc.addElement(P(text=f"RA {ra['id']} {ra['description']}"))
        ra_row.addElement(tc)

        # Cell B: Weight (0)
        tc = TableCell(stylename=ra_cell_styles[1] if len(ra_cell_styles)>1 else None,
                       valuetype="float",
                       value="0")
        tc.addElement(P(text="0"))
        ra_row.addElement(tc)

        # Cells C-Y: Empty
        for i in range(2, 25):
            style = ra_cell_styles[i] if i < len(ra_cell_styles) else None
            ra_row.addElement(TableCell(stylename=style))

        table.addElement(ra_row)
        current_row_idx += 1

        # --- Criteria Rows ---
        criteria_start_row = current_row_idx

        for criterion in ra['evaluation_criteria']:
            crit_row = TableRow(stylename=crit_row_style)

            # Cell A: Criterion Text
            crit_text = criterion.strip()
            tc = TableCell(stylename=crit_cell_styles[0] if len(crit_cell_styles)>0 else None,
                           valuetype="string")
            tc.addElement(P(text=crit_text))
            crit_row.addElement(tc)

            # Cell B: Weight (0)
            tc = TableCell(stylename=crit_cell_styles[1] if len(crit_cell_styles)>1 else None,
                           valuetype="float",
                           value="0")
            tc.addElement(P(text="0"))
            crit_row.addElement(tc)

            # Cells C-Y: Empty
            for i in range(2, 25):
                style = crit_cell_styles[i] if i < len(crit_cell_styles) else None
                crit_row.addElement(TableCell(stylename=style))

            table.addElement(crit_row)
            current_row_idx += 1

        criteria_end_row = current_row_idx - 1

        # --- NOTA Row ---
        note_row = TableRow(stylename=note_row_style)

        # Cell A: Label
        tc = TableCell(stylename=note_cell_styles[0] if len(note_cell_styles)>0 else None,
                       valuetype="string")
        tc.addElement(P(text="NOTA:"))
        note_row.addElement(tc)

        # Cell B: Empty
        note_row.addElement(TableCell(stylename=note_cell_styles[1] if len(note_cell_styles)>1 else None))

        # Cells C-Y: Formulas
        for col_i in range(2, 25):
            col_letter = get_col_letter(col_i)
            terms = []
            for r in range(criteria_start_row, criteria_end_row + 1):
                # ODF Formula Syntax: [.B4]*[.C4]
                term = f"[.B{r}]*[.{col_letter}{r}]"
                terms.append(term)

            formula_str = "of:=(" + "+".join(terms) + ")/100"

            style = note_cell_styles[col_i] if col_i < len(note_cell_styles) else None

            tc = TableCell(stylename=style,
                           valuetype="float",
                           value="0",
                           formula=formula_str)
            tc.addElement(P(text="0"))
            note_row.addElement(tc)

        table.addElement(note_row)
        current_row_idx += 1

    # 6. Save
    output_filename = "dam_di_evaluacionRA.ods"
    doc.save(output_filename)
    print(f"Saved to {output_filename}")

if __name__ == "__main__":
    generate_ods()
