import os
import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication


def _load_stylesheet(app: QApplication) -> None:
    qss_path = os.path.join(os.path.dirname(__file__), "..", "assets", "styles", "main.qss")
    try:
        with open(qss_path, "r", encoding="utf-8") as f:
            app.setStyleSheet(f.read())
    except FileNotFoundError:
        pass


def _load_icon(app: QApplication) -> None:
    icon_path = os.path.join(os.path.dirname(__file__), "..", "icon.png")
    if os.path.exists(icon_path):
        app.setWindowIcon(QIcon(icon_path))


def create_app(argv: list) -> QApplication:
    app = QApplication(argv)
    app.setApplicationName("PDFU")
    app.setOrganizationName("felipecaninnovaes")
    _load_stylesheet(app)
    _load_icon(app)
    return app
