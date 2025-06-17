# pdf_to_excel_parser

This repository contains a customizable script to extract structured tabular data from scanned or digitally generated PDF documents and convert it directly into Excel format. The workflow is ideal for column-based financial and project reports — especially complex layouts where auto-detection fails and manual alignment is necessary.

---

## How It Works

1. You **manually define column positions** (in pixels) using `column_viewing.py` by visually overlaying vertical lines on the PDF to guide parsing.
2. All key settings like PDF path, Excel output, and column definitions are stored in `config.py`.
3. The parser (`main.py`) extracts and buckets words into cells using `pdfplumber`, and saves a clean `.xlsx` file.

---

## New: Auto Column Detection (Optional)

Use `auto_column_detect.py` to automatically suggest column boundaries using vertical projection profiling.

### How It Works:
- Converts the PDF to grayscale
- Applies a vertical projection (ink density) profile
- Uses peak detection to locate whitespace valleys between columns
- Prints a suggested list of column coordinates to paste into your config or overlay tool

### How to Use:
1. Open `auto_column_detect.py`
2. Update the `PDF_PATH`, `DPI`, and cropping bounds (`CUT_TOP`, `CUT_LEFT`, `CUT_RIGHT`) as needed
3. Run the script:
   ```bash
   python auto_column_detect.py
4. Copy the printed `col_positions` list into `column_viewing.py` or `config.py`
5. Manually tweak any incorrect or extra boundaries

## How to Use column_viewing.py
Before running the parser:

1. Open config.py and set:

- `PDF_PATH`

- `COL_POSITIONS` (either manually defined or auto-suggested and edited)

2. Run:

```python column_viewing.py```

This visually overlays red vertical lines at each `col_positions[x]` to confirm layout before parsing.


## How to Run the Parser
Once columns and headers are finalized:


```python main.py```
You’ll get a clean Excel `.xlsx` output file from the defined pages.

## Installation
Clone and install requirements:


```git clone https://github.com/IzNawtThere/pdf_to_excel_parser.git
cd pdf_to_excel_parser
pip install -r requirements.txt
