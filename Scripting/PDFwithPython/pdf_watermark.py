import PyPDF2

input = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf','rb'))
output = PyPDF2.PdfFileWriter()

for i in range(input.getNumPages()):
    page = input.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('wrtpdfmark.pdf','wb') as file:
        output.write(file)