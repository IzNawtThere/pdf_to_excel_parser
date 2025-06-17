import pdfplumber

pdf_path = r"C:\Users\abhiraj.singh\Downloads\pg116-119.pdf"
output_img = r"C:\Users\abhiraj.singh\Downloads\columns116119.png"

col_positions = [
    34, 50, 100, 150, 220, 250, 375, 430, 465, 485,
    530, 570, 600, 630, 675, 710, 750, 765, 815, 850,
    870, 915, 950, 980, 1010, 1055, 1090, 1125, 1155
]

with pdfplumber.open(pdf_path) as pdf:
    page = pdf.pages[0]
    im = page.to_image(resolution=150)

    for x in col_positions:
        im.draw_line([(x, 130), (x, page.height)], stroke="red", stroke_width=1)

    im.save(output_img)
    print(f"Overlay image saved to: {output_img}")
