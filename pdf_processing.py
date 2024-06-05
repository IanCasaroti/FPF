import PyPDF2

def extract_content(pdf_file):
    pdf_file_obj = open(pdf_file, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
    page_obj = pdf_reader.getPage(0)
    return page_obj.extractText()