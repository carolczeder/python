import os
import sys
from pypdf import PdfMerger
# Check if a folder path argument has been provided
if len(sys.argv) > 1:
    folder_path = sys.argv[1]
else:
    print("Usage: python script_name.py <folder_path>")
    sys.exit(1)
# List all PDF files in the specified folder
pdfs = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]
merger = PdfMerger()
for pdf in pdfs:
    # Append the full path if your folder is not the current working directory
    full_path = os.path.join(folder_path, pdf)
    merger.append(full_path)
# Extract the folder name to use as the PDF file name
folder_name = os.path.basename(folder_path)
# Write the result to a new PDF file named after the folder
output_pdf_path = os.path.join(folder_path, f"{folder_name}.pdf")
merger.write(output_pdf_path)
merger.close()