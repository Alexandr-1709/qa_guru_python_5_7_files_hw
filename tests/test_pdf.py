from pypdf import PdfReader
import os
from os_path.os_path_scripts import resources
pdf_path = os.path.join(resources, 'docs-pytest-org-en-latest.pdf')


# TODO оформить в тест, добавить ассерты и использовать универсальный путь


def test_pdf_file():
    reader = PdfReader(pdf_path)
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()
    print(page)
    print(number_of_pages)
    print(text)
    assert number_of_pages == 412
    assert text == 'pytest Documentation\n' \
                   'Release 0.1\n' \
                   'holger krekel, trainer and consultant, https://merlinux.eu/\n' \
                   'Jul 14, 2022'
