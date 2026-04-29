from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog

# mode: "file" | "folder" | "save"

class FilePicker(QWidget):
    path_changed = Signal(str)

    def __init__(self, label: str, mode: str = "file", ext: str = "", button_text: str = "Procurar", parent=None):
        super().__init__(parent)
        self._mode = mode
        self._ext = ext
        self._path = ""

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(4)

        lbl = QLabel(label)
        lbl.setObjectName("filePickerLabel")
        layout.addWidget(lbl)

        row = QHBoxLayout()
        row.setSpacing(8)
        row.setContentsMargins(0, 0, 0, 0)

        self._input = QLineEdit()
        self._input.setObjectName("filePickerInput")
        self._input.setReadOnly(True)
        self._input.setPlaceholderText("Nenhum arquivo selecionado")
        row.addWidget(self._input)

        btn = QPushButton(button_text)
        btn.setObjectName("filePickerButton")
        btn.setCursor(Qt.PointingHandCursor)
        btn.setFixedWidth(100)
        btn.clicked.connect(self._open_dialog)
        row.addWidget(btn)

        layout.addLayout(row)

    def _open_dialog(self):
        path = ""
        if self._mode == "folder":
            path = QFileDialog.getExistingDirectory(self, "Selecionar pasta")
        elif self._mode == "save":
            ext_filter = f"Arquivos (*{self._ext})" if self._ext else "Todos os arquivos (*)"
            path, _ = QFileDialog.getSaveFileName(self, "Salvar como", "", ext_filter)
            if path and self._ext:
                ext_lower = self._ext.lower()
                if not path.lower().endswith(ext_lower):
                    path += self._ext
        else:
            ext_filter = f"Arquivos (*{self._ext})" if self._ext else "Todos os arquivos (*)"
            path, _ = QFileDialog.getOpenFileName(self, "Abrir arquivo", "", ext_filter)

        if path:
            self._path = path
            self._input.setText(path)
            self.path_changed.emit(path)

    def path(self) -> str:
        return self._path

    def clear(self):
        self._path = ""
        self._input.clear()
