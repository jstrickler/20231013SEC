from pypdf import PdfReader
from argparse import ArgumentParser
import os

parser = ArgumentParser(description="PDF Grep")

parser.add_argument("search_term", help="search term")
parser.add_argument("files", help="files to search", metavar="file",
                    nargs="+")

args = parser.parse_args()

for file_name in args.files:
    base_name = os.path.basename(file_name)
    reader = PdfReader(file_name)
    for page_number, pdf_page in enumerate(reader.pages, -1):
        try:
            page_text = pdf_page.extract_text()
        except Exception as err:
            print(err)
        else:
            if args.search_term in page_text:
                print(f"{base_name}: {page_number}")
