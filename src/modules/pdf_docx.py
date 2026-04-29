import os
from pdf2docx import Converter


def pdf_to_docx(input_path: str, output_path: str) -> None:
    if os.path.exists(output_path):
        os.remove(output_path)
    cv = Converter(input_path)
    cv.convert(output_path)
    cv.close()
