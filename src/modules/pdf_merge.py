import os
from glob import glob
from pikepdf import Pdf


def merge_pdfs(folder: str, output_path: str, progress_cb=None) -> None:
    pattern = os.path.join(folder, "*.pdf")
    files = sorted(glob(pattern))
    if not files:
        raise ValueError(f"Nenhum PDF encontrado em: {folder}")

    if os.path.exists(output_path):
        os.remove(output_path)

    pdf = Pdf.new()
    version = pdf.pdf_version
    total = len(files)

    for i, file in enumerate(files):
        src = Pdf.open(file)
        version = max(version, src.pdf_version)
        pdf.pages.extend(src.pages)
        if progress_cb:
            progress_cb(10 + int(85 * (i + 1) / total))

    pdf.remove_unreferenced_resources()
    pdf.save(output_path, min_version=version)
