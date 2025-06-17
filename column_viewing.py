import pdfplumber

pdf_path = r"your/path/here.pdf" # input PDF path here
output_img = r"your/output/here.png" # export image path here

col_positions = [
    # input your custom coordinates here
]

with pdfplumber.open(pdf_path) as pdf:
    page = pdf.pages[0]
    im = page.to_image(resolution=150)

    for x in col_positions:
        im.draw_line([(x, 130), (x, page.height)], stroke="red", stroke_width=1)

    im.save(output_img)
    print(f"Overlay image saved to: {output_img}") # cross check column divides
