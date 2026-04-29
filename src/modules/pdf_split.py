import os
from pikepdf import Pdf


def split_pdf(input_path: str, output_prefix: str, progress_cb=None) -> None:
    with Pdf.open(input_path) as pdf:
        total = len(pdf.pages)
        for i, page in enumerate(pdf.pages):
            out = Pdf.new()
            out.pages.append(page)
            page_path = f"{output_prefix} {i:02d}.pdf"
            if os.path.exists(page_path):
                os.remove(page_path)
            out.save(page_path)
            if progress_cb:
                progress_cb(10 + int(85 * (i + 1) / total))
