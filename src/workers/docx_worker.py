from workers.base_worker import BaseWorker
from modules.pdf_docx import pdf_to_docx


class DocxWorker(BaseWorker):
    def __init__(self, input_path: str, output_path: str):
        super().__init__()
        self._input = input_path
        self._output = output_path

    def run(self):
        try:
            self.progress.emit(10)
            pdf_to_docx(self._input, self._output)
            self.progress.emit(100)
            self.finished.emit(self._output)
        except Exception as e:
            self.error.emit(str(e))
