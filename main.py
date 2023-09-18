import PyPDF2
import os

merger = PyPDF2.Pdfmerger()

lista_arquivos = os.listdir("arquivos")
lista_arquivos.sort()
print(lista_arquivos)

for arquivo in lista_arquivos:
if ".pdf" in arquivo:
    merger.append("arquivos/{nome_do_arquivo}")

merger.write("PDF Final.pdf")
