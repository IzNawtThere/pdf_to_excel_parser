# pdf_to_excel_parser

This repository contains a customizable script to extract structured tabular data from scanned or digitally generated PDF documents and convert it directly into Excel format. The script is tailored for column-based financial and project reports — especially complex layouts where auto-detection fails and manual alignment works best.

---

## How It Works

- You manually define **column positions** (in pixels) using vertical guidelines.
- A `config.py` file contains all key settings — file paths, header definitions, and column splits.
- The parser reads each PDF page, extracts text using `pdfplumber`, and maps words to grid cells based on their horizontal position.
- The output is a clean `.xlsx` file ready for analysis.

---

## Installation

Clone the repo and install dependencies:

```bash
git clone https://github.com/lzNawtThere/pdf_to_excel_parser.git
cd pdf_to_excel_parser
pip install -r requirements.txt
