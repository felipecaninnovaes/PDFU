import os
from PySide6.QtCore import Qt, QByteArray, QSize
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
    QListWidget, QListWidgetItem, QSizePolicy, QMessageBox
)
from views.pages.base_page import BasePage
from widgets.file_picker import FilePicker
from workers.rotate_worker import RotateWorker
from modules.pdf_rotate import get_page_thumbnails


THUMB_SIZE = 140


class RotatePage(BasePage):
    PAGE_TITLE = "Rotacionar / Reordenar"
    PAGE_SUBTITLE = "Arraste as páginas para reordenar. Selecione e rotacione conforme necessário."

    def setup_ui(self):
        self._source_path = ""
        # _page_data: list of [source_path, original_index, cumulative_rotation]
        self._page_data: list = []

        self._input_picker = FilePicker(label="Selecionar PDF:", mode="file", ext=".pdf")
        self._input_picker.path_changed.connect(self._load_pdf)
        self._card_layout.addWidget(self._input_picker)

        # Thumbnail grid
        self._list = QListWidget()
        self._list.setObjectName("thumbnailList")
        self._list.setViewMode(QListWidget.ViewMode.IconMode)
        self._list.setIconSize(QSize(THUMB_SIZE, THUMB_SIZE))
        self._list.setResizeMode(QListWidget.ResizeMode.Adjust)
        self._list.setDragDropMode(QListWidget.DragDropMode.InternalMove)
        self._list.setMovement(QListWidget.Movement.Snap)
        self._list.setSpacing(6)
        self._list.setMinimumHeight(260)
        self._list.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self._card_layout.addWidget(self._list)

        # Rotation controls
        ctrl_row = QHBoxLayout()
        ctrl_row.setSpacing(8)

        for label, deg in [("↺ 90°", 90), ("↻ -90°", 270), ("180°", 180)]:
            btn = QPushButton(label)
            btn.setObjectName("rotateActionButton")
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.clicked.connect(lambda checked, d=deg: self._rotate_selected(d))
            ctrl_row.addWidget(btn)

        remove_btn = QPushButton("Remover página")
        remove_btn.setObjectName("rotateActionButton")
        remove_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        remove_btn.clicked.connect(self._remove_selected)
        ctrl_row.addStretch()
        ctrl_row.addWidget(remove_btn)
        self._card_layout.addLayout(ctrl_row)

        self._output_picker = FilePicker(label="Salvar PDF em:", mode="save", ext=".pdf")
        self._card_layout.addWidget(self._output_picker)

    def _load_pdf(self, path: str):
        self._source_path = path
        self._list.clear()
        self._page_data = []

        try:
            thumbnails = get_page_thumbnails(path, size=THUMB_SIZE)
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Não foi possível abrir o PDF:\n{e}")
            return

        for i, png_bytes in enumerate(thumbnails):
            pixmap = QPixmap()
            pixmap.loadFromData(QByteArray(png_bytes), "PNG")
            item = QListWidgetItem(QIcon(pixmap), f"Pág. {i + 1}")
            item.setSizeHint(QSize(THUMB_SIZE + 20, THUMB_SIZE + 30))
            item.setData(Qt.ItemDataRole.UserRole, i)
            self._list.addItem(item)
            self._page_data.append([path, i, 0])

    def _rotate_selected(self, degrees: int):
        for item in self._list.selectedItems():
            orig_idx = item.data(Qt.ItemDataRole.UserRole)
            for pd in self._page_data:
                if pd[1] == orig_idx:
                    pd[2] = (pd[2] + degrees) % 360
                    break

    def _remove_selected(self):
        for item in reversed(self._list.selectedItems()):
            orig_idx = item.data(Qt.ItemDataRole.UserRole)
            row = self._list.row(item)
            self._list.takeItem(row)
            self._page_data = [pd for pd in self._page_data if pd[1] != orig_idx]

    def _get_ordered_page_data(self) -> list:
        result = []
        for i in range(self._list.count()):
            item = self._list.item(i)
            orig_idx = item.data(Qt.ItemDataRole.UserRole)
            for pd in self._page_data:
                if pd[1] == orig_idx:
                    result.append(tuple(pd))
                    break
        return result

    def _validate(self) -> bool:
        if not self._source_path:
            self._show_error("Selecione um PDF.")
            return False
        if self._list.count() == 0:
            self._show_error("O PDF não tem páginas para processar.")
            return False
        if not self._output_picker.path():
            self._show_error("Defina onde salvar o PDF.")
            return False
        return True

    def _get_worker(self):
        ordered = self._get_ordered_page_data()
        return RotateWorker(ordered, self._output_picker.path())

    def _reset_fields(self):
        self._input_picker.clear()
        self._output_picker.clear()
        self._list.clear()
        self._page_data = []
        self._source_path = ""
