from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QHBoxLayout, QVBoxLayout,
    QFrame, QLabel, QStackedWidget, QSizePolicy, QSpacerItem
)
from views.sidebar import Sidebar
from views.pages.merge_page import MergePage
from views.pages.image_page import ImagePage
from views.pages.split_page import SplitPage
from views.pages.docx_page import DocxPage
from views.pages.compress_page import CompressPage
from views.pages.rotate_page import RotatePage

APP_VERSION = "2.0.0"

PAGE_TITLES = {
    "merge":    "Juntar PDFs",
    "image":    "Imagem para PDF",
    "split":    "Dividir PDF",
    "docx":     "PDF para Word",
    "compress": "Comprimir PDF",
    "rotate":   "Rotacionar / Reordenar",
}


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PDFU")
        self.setMinimumSize(900, 560)
        self.resize(1100, 680)

        root = QWidget()
        root_layout = QHBoxLayout(root)
        root_layout.setContentsMargins(0, 0, 0, 0)
        root_layout.setSpacing(0)

        # Sidebar
        self._sidebar = Sidebar(
            version=f"v{APP_VERSION}",
            on_navigate=self._navigate,
        )
        root_layout.addWidget(self._sidebar)

        # Content area
        content = QFrame()
        content.setObjectName("contentArea")
        content_layout = QVBoxLayout(content)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(0)

        # Top bar
        top_bar = QFrame()
        top_bar.setObjectName("topBar")
        top_bar.setFixedHeight(44)
        top_bar_layout = QHBoxLayout(top_bar)
        top_bar_layout.setContentsMargins(20, 0, 20, 0)

        brand = QLabel("PDFU")
        brand.setObjectName("topBarBrand")
        top_bar_layout.addWidget(brand)

        top_bar_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

        self._page_label = QLabel("Juntar PDFs")
        self._page_label.setObjectName("topBarTitle")
        top_bar_layout.addWidget(self._page_label)

        content_layout.addWidget(top_bar)

        # Pages stack
        self._stack = QStackedWidget()
        self._stack.setObjectName("pageContainer")

        self._pages: dict[str, QWidget] = {
            "merge":    MergePage(),
            "image":    ImagePage(),
            "split":    SplitPage(),
            "docx":     DocxPage(),
            "compress": CompressPage(),
            "rotate":   RotatePage(),
        }
        for page in self._pages.values():
            self._stack.addWidget(page)

        content_layout.addWidget(self._stack)
        root_layout.addWidget(content, 1)

        self.setCentralWidget(root)

        # Show first page
        self._navigate("merge")

    def _navigate(self, key: str):
        self._stack.setCurrentWidget(self._pages[key])
        self._page_label.setText(PAGE_TITLES.get(key, ""))
