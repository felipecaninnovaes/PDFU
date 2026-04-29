from workers.base_worker import BaseWorker
from modules.pdf_image import image_to_pdf


class ImageWorker(BaseWorker):
    def __init__(self, input_path: str, output_path: str):
        super().__init__()
        self._input = input_path
        self._output = output_path

    def run(self):
        try:
            self.progress.emit(20)
            image_to_pdf(self._input, self._output)
            self.progress.emit(100)
            self.finished.emit(self._output)
        except Exception as e:
            self.error.emit(str(e))
