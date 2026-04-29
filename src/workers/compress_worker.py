from workers.base_worker import BaseWorker
from modules.pdf_compress import compress_pdf


class CompressWorker(BaseWorker):
    def __init__(self, input_path: str, output_path: str, quality: int = 2):
        super().__init__()
        self._input = input_path
        self._output = output_path
        self._quality = quality  # 1=baixa, 2=média, 3=alta

    def run(self):
        try:
            self.progress.emit(10)
            compress_pdf(self._input, self._output, self._quality, progress_cb=self.progress.emit)
            self.progress.emit(100)
            self.finished.emit(self._output)
        except Exception as e:
            self.error.emit(str(e))
