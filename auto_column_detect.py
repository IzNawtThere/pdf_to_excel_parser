# auto_column_detect.py

import pdfplumber
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks, savgol_filter
import cv2
from config import pdf_path, DPI, CUT_TOP, CUT_LEFT, CUT_RIGHT, SAVGOL_WIN, SAVGOL_POLY, PEAK_PROM, PEAK_DIST

with pdfplumber.open(pdf_path) as pdf:
    page = pdf.pages[0]
    pil = page.to_image(resolution=DPI).original.convert("L")
    gray = np.array(pil)

work = gray.copy()
work[:CUT_TOP, :] = 255
work[:, :CUT_LEFT] = 255
work[:, -CUT_RIGHT:] = 255

_, bin_img = cv2.threshold(work, 180, 255, cv2.THRESH_BINARY_INV)
profile_raw = np.sum(bin_img, axis=0)
profile_sg = savgol_filter(profile_raw, SAVGOL_WIN, SAVGOL_POLY)
inverted = np.max(profile_sg) - profile_sg
peaks, _ = find_peaks(inverted, prominence=PEAK_PROM, distance=PEAK_DIST)

col_positions = [0] + sorted(peaks.tolist()) + [gray.shape[1]]

print(f"\nDetected {len(col_positions)-1} columns.")
print("Copy this list into your config.py:")
print("col_positions = [")
for x in col_positions:
    print(f"    {x},")
print("]")

plt.figure(figsize=(20, 3))
plt.plot(profile_raw, alpha=0.3, label="Raw")
plt.plot(profile_sg, color="black", label="Smoothed")
for p in peaks:
    plt.axvline(p, color='red', linestyle='--', linewidth=0.6)
plt.title("Vertical Projection Profile")
plt.legend()
plt.tight_layout()
plt.show()

overlay = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
for x in col_positions:
    cv2.line(overlay, (x, 0), (x, gray.shape[0]), (0, 0, 255), 2)

from PIL import Image
Image.fromarray(overlay)
