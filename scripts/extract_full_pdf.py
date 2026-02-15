
import fitz  # PyMuPDF
import sys

filename = "bird.pdf"
output_file = "bird_pdf_content.txt"

try:
    print(f"Reading {filename}...")
    doc = fitz.open(filename)
    text = ""
    for i, page in enumerate(doc):
        text += f"\n--- Page {i+1} ---\n"
        text += page.get_text()
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text)
    
    print(f"Successfully extracted {len(text)} characters to {output_file}")
    doc.close()

except Exception as e:
    print(f"Error: {e}")
