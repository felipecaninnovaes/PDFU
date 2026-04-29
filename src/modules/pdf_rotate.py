import os
import fitz  # PyMuPDF
from pikepdf import Pdf


def get_page_thumbnails(input_path: str, size: int = 160) -> list:
    """Return list of QPixmap-compatible bytes for each page."""
    doc = fitz.open(input_path)
    thumbnails = []
    for page in doc:
        mat = fitz.Matrix(size / page.rect.width, size / page.rect.height)
        pix = page.get_pixmap(matrix=mat)
        thumbnails.append(pix.tobytes("png"))
    doc.close()
    return thumbnails


def save_reordered_pdf(page_data: list, output_path: str, progress_cb=None) -> None:
    """
    page_data: list of (source_pdf_path, original_page_index, rotation_degrees)
    All pages must share the same source PDF in this implementation.
    """
    if not page_data:
        raise ValueError("Nenhuma página para salvar.")

    source_path = page_data[0][0]
    if os.path.exists(output_path):
        os.remove(output_path)

    with Pdf.open(source_path) as src:
        out = Pdf.new()
        total = len(page_data)
        for i, (_, orig_idx, rotation) in enumerate(page_data):
            page = src.pages[orig_idx]
            # Apply rotation relative to existing rotation
            existing = int(page.get("/Rotate", 0))
            new_rot = (existing + rotation) % 360
            page = out.copy_foreign(page)
            page["/Rotate"] = new_rot
            out.pages.append(page)
            if progress_cb:
                progress_cb(10 + int(80 * (i + 1) / total))
        out.save(output_path)
