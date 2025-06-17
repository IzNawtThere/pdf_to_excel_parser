# config.py

# FILE PATHS
pdf_path = r"your/path/to/input.pdf"
output_path = r"your/path/to/output.xlsx"
column_overlay_path = r"your/path/to/column_overlay.png"

# COLUMN COORDINATES (TO BE FILLED BY USER)
col_positions = [
    # replace this after running auto_column_detect.py
]

# HEADERS (manually edit these to match your PDF structure)
column_headers = [
    # Your Excel headers here
]

# GLOBAL PARAMS (used by all modules)
DPI = 400
CUT_TOP, CUT_LEFT, CUT_RIGHT = 100, 100, 80
SAVGOL_WIN, SAVGOL_POLY = 51, 3
PEAK_PROM, PEAK_DIST = 30000, 50
