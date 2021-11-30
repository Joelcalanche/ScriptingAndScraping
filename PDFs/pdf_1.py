import PyPDF2 as pypdf
from PyPDF2.pagerange import PAGE_RANGE_ALL

template = pypdf.PdfFileReader(open('super.pdf', 'rb'))
watermark = pypdf.PdfFileReader(open('wtr.pdf', 'rb'))

output = pypdf.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i) 
    # une dos pginas en una, combinacion
    page.mergePage(watermark.getPage(0))
    
    output.addPage(page)


    with open('watermarked_output.pdf', 'wb') as file:
        output.write(file)