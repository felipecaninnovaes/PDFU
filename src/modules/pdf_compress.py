import os
import fitz  # PyMuPDF
from pikepdf import Pdf, PdfImage
from pikepdf._core import PdfError


# quality: 1=baixa (maior compressão), 2=média, 3=alta (menor compressão)
_QUALITY_MAP = {1: 30, 2: 60, 3: 85}


def compress_pdf(input_path: str, output_path: str, quality: int = 2, progress_cb=None) -> None:
    if os.path.exists(output_path):
        os.remove(output_path)

    jpeg_quality = _QUALITY_MAP.get(quality, 60)

    doc = fitz.open(input_path)
    total = doc.page_count

    tmp_path = output_path + ".tmp.pdf"
    doc_out = fitz.open()

    for i, page in enumerate(doc):
        pix = page.get_pixmap(dpi=150 if quality == 1 else (200 if quality == 2 else 300))
        img_page = doc_out.new_page(width=pix.width, height=pix.height)
        img_page.insert_image(img_page.rect, pixmap=pix)
        if progress_cb:
            progress_cb(10 + int(80 * (i + 1) / total))

    doc_out.save(tmp_path, garbage=4, deflate=True, clean=True)
    doc_out.close()
    doc.close()

    os.rename(tmp_path, output_path)
