from PyPDF2 import PdfMerger  #install PyPDF2(pip install PyPDF2)
import os

pdf = PdfMerger()

for file in os.listdir():
    if file.endswith(".pdf"):
        pdf.append(file)

pdf.write("MergeRRRR.pdf")
pdf.close()
print("Marge completed !!")
