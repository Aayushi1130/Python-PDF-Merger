import PyPDF2


pdf = ['example.pdf','test.pdf']
result = 'merged_file.pdf'
pdfM = PyPDF2.PdfFileMerger()

for p in pdf:
    pdfM.append(p)

with open(result,'wb') as f:
    pdfM.write(f)

print("Files Merged Successfully!!!")
