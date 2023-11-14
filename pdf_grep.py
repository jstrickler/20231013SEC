from pypdf import PdfReader

pdf_file = "/Users/jstrick/py/custom/pydummy/production_1.1_conan/pydummy_1.1_conan.pdf"

search_term = 'container'

reader = PdfReader(pdf_file)
for page_number, pdf_page in enumerate(reader.pages, -1):
    page_text = pdf_page.extract_text()
    if search_term in page_text:
        print(f"Found on page {page_number}")
