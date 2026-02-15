
import sys
import shutil
import pytesseract
from pdf2image import convert_from_path, pdfinfo_from_path

print("Checking OCR dependencies...")

# Check Tesseract
tesseract_cmd = shutil.which("tesseract")
if tesseract_cmd:
    print(f"Tesseract found at: {tesseract_cmd}")
else:
    print("Tesseract NOT found in PATH.")

# Check Poppler
# pdf2image usually relies on 'pdftoppm' or 'pdftocairo' from poppler
pdftoppm = shutil.which("pdftoppm")
if pdftoppm:
    print(f"Poppler (pdftoppm) found at: {pdftoppm}")
else:
    print("Poppler (pdftoppm) NOT found in PATH.")

try:
    print("Attempting to get Tesseract version...")
    print(pytesseract.get_tesseract_version())
except Exception as e:
    print(f"Error getting Tesseract version: {e}")

try:
    print("Attempting to get PDF info (requires Poppler)...")
    info = pdfinfo_from_path("paper.pdf")
    print("Poppler seems to be working.")
except Exception as e:
    print(f"Error checking Poppler with pdf2image: {e}")
