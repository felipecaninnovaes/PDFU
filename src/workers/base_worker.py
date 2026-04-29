from PySide6.QtCore import QThread, Signal


class BaseWorker(QThread):
    progress = Signal(int)   # 0–100
    finished = Signal(str)   # output file path
    error = Signal(str)      # error message

    def run(self):
        raise NotImplementedError
