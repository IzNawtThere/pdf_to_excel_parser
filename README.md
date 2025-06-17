# pdf_to_excel_parser

This repository contains a flexible PDF-to-Excel parsing pipeline built for extracting structured tabular data from scanned or digitally generated PDF documents — particularly those with complex layouts, inconsistent row heights, or overlapping text. It is optimized for column-based financial reports or cost sheets, where **manual column boundary definitions** give better results than automated detection.

---

## How It Works

This parser is built on a **manual alignment paradigm**, where you define exactly how columns are split. It's designed for layout-heavy documents where:

- Text may wrap across multiple lines
- Table structures are not clearly bordered
- OCR-based methods often fail

### The Workflow

1. Use `column_viewing.py` to visually define **column boundaries** by overlaying red lines on a PDF preview.
2. Define all file paths and column structure inside `config.py`.
3. Run the parser via `main.py` to:
   - Read the PDF using `pdfplumber`
   - Group lines into logical rows using vertical proximity
   - Bucket words into columns based on pixel `x` positions
   - Write the structured output directly into `.xlsx`

---

## Repository Structure

| File               | Purpose                                                                 |
|--------------------|--------------------------------------------------------------------------|
| `config.py`         | Centralized config: file paths, column headers, positions, tolerances   |
| `column_viewing.py` | View the PDF with vertical guides to manually fine-tune columns         |
| `main.py`           | The core parser script — reads PDF, assigns cells, exports Excel        |
| `requirements.txt`  | Python dependencies — use with `pip install -r`                         |
| `README.md`         | You're reading it.                                                      |

---

## Visual Column Alignment (Important Step)

Before parsing, make sure your column boundaries are precise:

### Run:

```bash
python column_viewing.py
