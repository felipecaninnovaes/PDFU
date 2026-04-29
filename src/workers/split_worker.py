from workers.base_worker import BaseWorker
from modules.pdf_split import split_pdf


class SplitWorker(BaseWorker):
    def __init__(self, input_path: str, output_prefix: str):
        super().__init__()
        self._input = input_path
        self._output = output_prefix

    def run(self):
        try:
            self.progress.emit(10)
            split_pdf(self._input, self._output, progress_cb=self.progress.emit)
            self.progress.emit(100)
            self.finished.emit(self._output)
        except Exception as e:
            self.error.emit(str(e))
