import PyPDF2
# f= open('examplepdf.pdf','rb')
# pdfread = PyPDF2.PdfFileReader(f)
# print(pdfread.numPages)
# pageone= pdfread.getPage(5)
# pageonetext= pageone.extractText()
# print(pageonetext)
# f.close()


f= open('examplepdf.pdf','rb')
pdfread = PyPDF2.PdfFileReader(f)
firstpage=pdfread.getPage(50)
pdfwrite=PyPDF2.PdfFileWriter()
pdfwrite.addPage(firstpage)
outputpdf= open('newpdf.pdf','wb')
pdfwrite.write(outputpdf)
f.close()