from workers.base_worker import BaseWorker
from modules.pdf_rotate import save_reordered_pdf


class RotateWorker(BaseWorker):
    def __init__(self, page_data: list, output_path: str):
        super().__init__()
        # page_data: list of (original_index, rotation_degrees)
        self._page_data = page_data
        self._output = output_path

    def run(self):
        try:
            self.progress.emit(10)
            save_reordered_pdf(self._page_data, self._output, progress_cb=self.progress.emit)
            self.progress.emit(100)
            self.finished.emit(self._output)
        except Exception as e:
            self.error.emit(str(e))
