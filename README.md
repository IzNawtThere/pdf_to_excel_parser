# pdf_to_excel_parser

This repository contains a customizable pipeline to extract structured tabular data from scanned or digitally generated PDF reports. It is designed for column-based layouts — especially where automatic parsing tools fail due to inconsistent formatting.

---

## How It Works (Three-Step Flow)

1. **Run `auto_column_detect.py`**  
   This analyzes the visual density of the first page and prints suggested vertical column boundaries.  
   - Copy the printed `col_positions` into `config.py`.

2. **Run `column_viewing.py`**  
   This overlays vertical red lines using your manually verified or auto-detected columns.  
   - Helps visually confirm or tweak alignment.

3. **Run `main.py`**  
   Once confirmed, this extracts all tables into a clean `.xlsx` using only what’s defined in `config.py`.

---

## Edit This Single File: `config.py`

Only `config.py` needs manual editing. It includes:
- `pdf_path`: path to your PDF
- `output_path`: Excel output location
- `col_positions`: vertical column splits
- `column_headers`: column names to appear in the Excel

---

## Installation

```bash
git clone https://github.com/IzNawtThere/pdf_to_excel_parser.git
cd pdf_to_excel_parser
pip install -r requirements.txt
