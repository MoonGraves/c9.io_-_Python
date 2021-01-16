from fpdf import FPDF
from PyPDF2 import PdfFileWriter, PdfFileReader

def secure_pdf(file, password):
  parser = PdfFileWriter()
  pdf = PdfFileReader(file)

  for page in range(pdf.numPages):

    parser.addPage(pdf.getPage(page))

  parser.encrypt(password)

  #wb = writing in binary mode
  with open(f"encrypted_{file}", "wb") as f:
    parser.write(f)
    f.close()

  print(f"encrypted_{file} is created... ")

if __name__ == "__main__":
#set file name & and password , only read same path with other files
  file = "asd.pdf"
  password = "qwerty123"
  secure_pdf(file, password)
