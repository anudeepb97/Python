import PyPDF2 as pyp
from sys import argv

inputs = argv[1:]


def pdf_merge(pdf_list):
    merger = pyp.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')


pdf_merge(inputs)
