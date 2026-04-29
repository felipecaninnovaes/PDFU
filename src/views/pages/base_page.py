from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QHBoxLayout,
    QPushButton, QMessageBox, QFrame
)
from widgets.progress_bar import InlineProgressBar


class BasePage(QWidget):
    PAGE_TITLE = "Página"
    PAGE_SUBTITLE = ""

    def __init__(self, parent=None):
        super().__init__(parent)
        self._worker = None
        self._setup_base_ui()
        self.setup_ui()

    def _setup_base_ui(self):
        self._root_layout = QVBoxLayout(self)
        self._root_layout.setContentsMargins(32, 28, 32, 28)
        self._root_layout.setSpacing(0)

        # Header
        title = QLabel(self.PAGE_TITLE)
        title.setObjectName("pageTitle")
        self._root_layout.addWidget(title)

        if self.PAGE_SUBTITLE:
            sub = QLabel(self.PAGE_SUBTITLE)
            sub.setObjectName("pageSubtitle")
            self._root_layout.addWidget(sub)

        self._root_layout.addSpacing(20)

        # Card
        self._card = QFrame()
        self._card.setObjectName("card")
        self._card_layout = QVBoxLayout(self._card)
        self._card_layout.setContentsMargins(24, 20, 24, 20)
        self._card_layout.setSpacing(16)
        self._root_layout.addWidget(self._card)

        self._root_layout.addStretch()

        # Progress bar (below card)
        self._progress = InlineProgressBar()
        self._root_layout.addWidget(self._progress)

        # Action row
        action_row = QHBoxLayout()
        action_row.setContentsMargins(0, 16, 0, 0)
        self._action_btn = QPushButton("Processar")
        self._action_btn.setObjectName("primaryButton")
        self._action_btn.setCursor(Qt.PointingHandCursor)
        self._action_btn.clicked.connect(self._on_process)
        action_row.addStretch()
        action_row.addWidget(self._action_btn)
        self._root_layout.addLayout(action_row)

    def setup_ui(self):
        """Override in subclasses to add widgets to self._card_layout."""
        pass

    def _get_worker(self):
        """Override to return the QThread worker for this page."""
        raise NotImplementedError

    def _validate(self) -> bool:
        """Override to validate inputs before processing. Return True if OK."""
        return True

    def _on_process(self):
        if not self._validate():
            return
        if self._worker and self._worker.isRunning():
            return

        self._worker = self._get_worker()
        self._worker.progress.connect(self._progress.set_value)
        self._worker.finished.connect(self._on_finished)
        self._worker.error.connect(self._on_error)

        self._action_btn.setEnabled(False)
        self._progress.start()
        self._worker.start()

    def _on_finished(self, output_path: str):
        self._progress.finish()
        self._action_btn.setEnabled(True)
        QMessageBox.information(self, "Concluído", f"Arquivo gerado com sucesso:\n{output_path}")
        self._reset_fields()

    def _on_error(self, message: str):
        self._progress.reset()
        self._action_btn.setEnabled(True)
        QMessageBox.critical(self, "Erro", f"Ocorreu um erro:\n{message}")

    def _reset_fields(self):
        """Override to clear pickers after successful operation."""
        pass

    def _show_error(self, message: str):
        QMessageBox.warning(self, "Atenção", message)
