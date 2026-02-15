
import fitz  # PyMuPDF
import sys

# Target file
filename = "bird.pdf"

try:
    print(f"Reading {filename} with PyMuPDF...")
    doc = fitz.open(filename)
    text = ""
    # Read first 5 pages
    for i, page in enumerate(doc):
        if i >= 5: break 
        text += f"\n--- Page {i+1} ---\n"
        text += page.get_text()
    
    if len(text.strip()) < 50:
        print("WARNING: Extracted text is very short or empty. Checking for images...")
        image_count = 0
        for page in doc:
            images = page.get_images()
            image_count += len(images)
        print(f"Total images found: {image_count}")
        if image_count > 0:
             print("PDF appears to contain images (likely scanned).")
    else:
        print(text[:2000]) # Print first 2000 chars to avoid huge output
        print("\n... (truncated)")
    
    doc.close()

except Exception as e:
    print(f"Error reading PDF: {e}")
