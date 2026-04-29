from PySide6.QtCore import QEasingCurve, QPropertyAnimation, Qt
from PySide6.QtWidgets import (
    QFrame, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout
)
from widgets.nav_button import NavButton

SIDEBAR_COLLAPSED = 52
SIDEBAR_EXPANDED = 220
ANIMATION_MS = 280

NAV_ITEMS = [
    ("Juntar PDFs",            "icon_home.svg",     "merge"),
    ("Imagem para PDF",        "icon_imageconv.svg","image"),
    ("Dividir PDF",            "icon_split.svg",    "split"),
    ("PDF para Word",          "icon_docx.svg",     "docx"),
    ("Comprimir PDF",          "icon_compress.svg", "compress"),
    ("Rotacionar / Reordenar", "icon_rotate.svg",   "rotate"),
]


class Sidebar(QFrame):
    def __init__(self, version: str, on_navigate, parent=None):
        super().__init__(parent)
        self.setObjectName("sidebar")
        self._expanded = True
        self._on_navigate = on_navigate
        self._buttons: dict[str, NavButton] = {}
        self._animation = None

        self.setMinimumWidth(SIDEBAR_EXPANDED)
        self.setMaximumWidth(SIDEBAR_EXPANDED)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Toggle button
        self._toggle_btn = QPushButton()
        self._toggle_btn.setObjectName("toggleButton")
        self._toggle_btn.setText("  PDFU")
        self._toggle_btn.setMinimumHeight(52)
        self._toggle_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self._toggle_btn.clicked.connect(self.toggle)
        layout.addWidget(self._toggle_btn)

        # Nav buttons
        for text, icon, key in NAV_ITEMS:
            btn = NavButton(text=text, icon_name=icon)
            btn.clicked.connect(lambda checked, k=key: self._navigate(k))
            layout.addWidget(btn)
            self._buttons[key] = btn

        layout.addItem(QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # Version label
        self._version_lbl = QLabel(version)
        self._version_lbl.setObjectName("versionLabel")
        self._version_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._version_lbl.setMinimumHeight(32)
        layout.addWidget(self._version_lbl)

        # Activate first button
        self._active_key = "merge"
        self._buttons["merge"].set_active(True)

    def _navigate(self, key: str):
        for k, btn in self._buttons.items():
            btn.set_active(k == key)
        self._active_key = key
        self._on_navigate(key)

    def toggle(self):
        self._expanded = not self._expanded
        target = SIDEBAR_EXPANDED if self._expanded else SIDEBAR_COLLAPSED

        self._animation = QPropertyAnimation(self, b"minimumWidth")
        self._animation.setStartValue(self.width())
        self._animation.setEndValue(target)
        self._animation.setDuration(ANIMATION_MS)
        self._animation.setEasingCurve(QEasingCurve.Type.OutCubic)
        self._animation.start()

        anim2 = QPropertyAnimation(self, b"maximumWidth")
        anim2.setStartValue(self.width())
        anim2.setEndValue(target)
        anim2.setDuration(ANIMATION_MS)
        anim2.setEasingCurve(QEasingCurve.Type.OutCubic)
        anim2.start()
        self._anim2 = anim2

        for btn in self._buttons.values():
            btn.set_expanded(self._expanded)

        self._toggle_btn.setText("  PDFU" if self._expanded else "")
        self._version_lbl.setVisible(self._expanded)
