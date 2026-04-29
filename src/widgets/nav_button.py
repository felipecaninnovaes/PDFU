from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon, QColor, QPainter, QPixmap
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtWidgets import QPushButton
import os

ICON_DIR = os.path.join(os.path.dirname(__file__), "..", "assets", "icons")
ICON_COLOR_DEFAULT = "#B0B8C1"
ICON_COLOR_ACTIVE = "#FFFFFF"
ICON_SIZE = 20


def _colorize_svg(svg_path: str, color: str) -> QPixmap:
    renderer = QSvgRenderer(svg_path)
    pixmap = QPixmap(ICON_SIZE, ICON_SIZE)
    pixmap.fill(Qt.transparent)
    painter = QPainter(pixmap)
    renderer.render(painter)
    painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
    painter.fillRect(pixmap.rect(), QColor(color))
    painter.end()
    return pixmap


class NavButton(QPushButton):
    def __init__(self, text: str, icon_name: str, is_active: bool = False, parent=None):
        super().__init__(parent)
        self._icon_name = icon_name
        self._text = text
        self._active = is_active
        self.setObjectName("navButton")
        self.setCheckable(False)
        self.setMinimumHeight(48)
        self.setIconSize(QSize(ICON_SIZE, ICON_SIZE))
        self._update_appearance()

    def set_active(self, active: bool):
        self._active = active
        self._update_appearance()
        self.setProperty("active", "true" if active else "false")
        self.style().unpolish(self)
        self.style().polish(self)

    def set_expanded(self, expanded: bool):
        self.setText(self._text if expanded else "")

    def _update_appearance(self):
        color = ICON_COLOR_ACTIVE if self._active else ICON_COLOR_DEFAULT
        icon_path = os.path.join(ICON_DIR, self._icon_name)
        if os.path.exists(icon_path):
            pixmap = _colorize_svg(icon_path, color)
            self.setIcon(QIcon(pixmap))
        self.setText(self._text)
        self.setProperty("active", "true" if self._active else "false")
