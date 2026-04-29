from workers.base_worker import BaseWorker
from modules.pdf_merge import merge_pdfs


class MergeWorker(BaseWorker):
    def __init__(self, folder: str, output_path: str):
        super().__init__()
        self._folder = folder
        self._output = output_path

    def run(self):
        try:
            self.progress.emit(10)
            merge_pdfs(self._folder, self._output, progress_cb=self.progress.emit)
            self.progress.emit(100)
            self.finished.emit(self._output)
        except Exception as e:
            self.error.emit(str(e))
