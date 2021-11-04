import time
from glob import glob
from PyPDF2 import PdfFileMerger

seconds = time.time()
local_time = time.ctime(seconds)
local_time = local_time.replace(":", "_")
local_time = local_time.replace(" ", "_")

def pdf_merge():
    merger = PdfFileMerger()
    allpdfs = [a for a in glob("*.pdf")]
    [merger.append(pdf) for pdf in allpdfs]
    with open(local_time + ".pdf" ,"wb") as new_file:
        merger.write(new_file)


if __name__ == "__main__":
    pdf_merge()
