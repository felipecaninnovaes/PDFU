from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QProgressBar, QLabel


class InlineProgressBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setVisible(False)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 8, 0, 0)
        layout.setSpacing(4)

        self._bar = QProgressBar()
        self._bar.setRange(0, 100)
        self._bar.setValue(0)
        self._bar.setTextVisible(False)
        self._bar.setFixedHeight(8)
        layout.addWidget(self._bar)

        row = QHBoxLayout()
        self._label = QLabel("Processando...")
        self._label.setObjectName("progressLabel")
        self._pct = QLabel("0%")
        self._pct.setObjectName("progressLabel")
        self._pct.setAlignment(Qt.AlignRight)
        row.addWidget(self._label)
        row.addWidget(self._pct)
        layout.addLayout(row)

    def start(self, message: str = "Processando..."):
        self._label.setText(message)
        self._bar.setValue(0)
        self._pct.setText("0%")
        self.setVisible(True)

    def set_value(self, value: int):
        self._bar.setValue(value)
        self._pct.setText(f"{value}%")

    def finish(self):
        self._bar.setValue(100)
        self._pct.setText("100%")

    def reset(self):
        self._bar.setValue(0)
        self._pct.setText("0%")
        self.setVisible(False)
