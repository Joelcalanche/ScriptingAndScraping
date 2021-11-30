import PyPDF2 as pypdf
import sys
# # entrada
# with open('dummy.pdf', 'rb') as file:
#     reader = pypdf.PdfFileReader(file)
#     page = reader.getPage(0)
#     page.rotateCounterClockwise(90)
#     writer = pypdf.PdfFileWriter()
#     writer.addPage(page)
# #salida
#     with open('tilt.pdf','wb') as new_file:
#         writer.write(new_file)


# de esta forma capturo todos los argumentos
imputs = sys.argv[1:]
def pdf_combiner(pdf_list):
    merger = pypdf.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')


pdf_combiner(imputs)
        
