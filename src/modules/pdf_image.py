import os
import img2pdf
from PIL import Image


def image_to_pdf(input_path: str, output_path: str) -> None:
    if os.path.exists(output_path):
        os.remove(output_path)

    with Image.open(input_path) as img:
        if img.mode in ("RGBA", "P"):
            rgb_path = input_path + "_converted.png"
            img.convert("RGB").save(rgb_path)
            source = rgb_path
        else:
            source = input_path

    with open(output_path, "wb") as f:
        f.write(img2pdf.convert(source))

    if source != input_path and os.path.exists(source):
        os.remove(source)
