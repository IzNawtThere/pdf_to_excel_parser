# config.py

pdf_path = r"your/path/here.pdf" # path to your input PDF
output_path = r"your/output/path.xlsx" # output Excel file

col_positions = [ 
    34, 50, 100, 150, 220, 250, 375, 430, 465, 485, 530,
    570, 600, 630, 675, 710, 750, 765, 815, 850, 870,
    915, 950, 980, 1010, 1055, 1090, 1125, 1155
] # manually estimated column x-coordinates

column_headers = [
    "Project Status Rank", "Project Status", "Revised Portfolio", "District", "Project Code", "Project Name",
    "Total Board TDC", "Total Board TDC Contingency", "Total Board TDC Contingency %",
    "Board TDC Cost Head 2-8", "Board TDC Cost Head 4 & 5", "Design Original Contingency", "Design Original Contingency %",
    "Construction Original Contingency", "Construction Original Contingency %", "Development Original Contingency", "Development Original Contingency %",
    "Total Current TDC", "Total Current TDC Contingency", "Total Current TDC Contingency %",
    "Current TDC Cost Head 2-8", "Current TDC Cost Head 4 & 5", "Design Remaining Contingency", "Design Remaining Contingency %",
    "Construction Remanining Contingency", "Construction Remaining Contingency %", "Development Remaining Contingency", "Development Remaining Contingency %"
] # headers for Excel export
