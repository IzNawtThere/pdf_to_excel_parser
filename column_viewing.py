# column_viewing.py

import pdfplumber
from config import pdf_path, column_overlay_path, col_positions

with pdfplumber.open(pdf_path) as pdf:
    page = pdf.pages[0]
    im = page.to_image(resolution=150)

    for x in col_positions:
        im.draw_line([(x, 130), (x, page.height)], stroke="red", stroke_width=1)

    im.save(column_overlay_path)
    print(f"Overlay image saved to: {column_overlay_path}")
