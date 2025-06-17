import pdfplumber
import pandas as pd
from config import pdf_path, output_path, col_positions, column_headers

cleaned_rows = []

with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        words = page.extract_words(x_tolerance=2, y_tolerance=2, keep_blank_chars=True, use_text_flow=True)

        rows_by_y = {}
        for word in words:
            y0 = round(word["top"], 1)
            if y0 not in rows_by_y:
                rows_by_y[y0] = []
            rows_by_y[y0].append(word)

        for y0 in sorted(rows_by_y.keys()):
            if y0 < 140:
                continue

            line_words = sorted(rows_by_y[y0], key=lambda w: w["x0"])
            row_cells = [''] * (len(col_positions) - 1)

            for word in line_words:
                x_center = (word["x0"] + word["x1"]) / 2
                for i in range(len(col_positions) - 1):
                    if col_positions[i] <= x_center < col_positions[i + 1]:
                        row_cells[i] += word["text"]
                        break

            if any(cell.strip() for cell in row_cells):
                cleaned_rows.append(row_cells)

df = pd.DataFrame(cleaned_rows)
df.columns = column_headers[:len(df.columns)] + [f"Extra Col {i+1}" for i in range(len(df.columns) - len(column_headers))]
df.to_excel(output_path, index=False)
print(f"Saved to: {output_path}")
