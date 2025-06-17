# pdf_to_excel_parser

This repository contains a customizable script to extract structured tabular data from scanned or digitally generated PDF documents and convert it directly into Excel format. The script is tailored for column-based financial and project reports — especially complex layouts where auto-detection fails and manual alignment works best.

---

## How It Works

1. You **manually define column positions** (in pixels) using `column_viewing.py` by visually overlaying red lines on a PDF page to verify vertical cuts.
2. All key settings like PDF path, Excel output path, headers, and column boundaries are stored in `config.py`.
3. The main parser (`main.py`) reads each page using `pdfplumber`, assigns words into cells based on column positions, and outputs a clean `.xlsx` table.

---

## How to Use `column_viewing.py`

Before running the parser:

- Open `config.py` and set:
  - `PDF_PATH`
  - `COL_POSITIONS` (you can start with rough estimates)
- Run:
  ```bash
  python column_viewing.py
