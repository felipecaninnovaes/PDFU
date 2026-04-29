from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHBoxLayout, QLabel, QSlider
from views.pages.base_page import BasePage
from widgets.file_picker import FilePicker
from workers.compress_worker import CompressWorker


class CompressPage(BasePage):
    PAGE_TITLE = "Comprimir PDF"
    PAGE_SUBTITLE = "Reduz o tamanho do arquivo PDF com controle de qualidade."

    def setup_ui(self):
        self._input_picker = FilePicker(label="Selecionar PDF:", mode="file", ext=".pdf")
        self._output_picker = FilePicker(label="Salvar PDF comprimido em:", mode="save", ext=".pdf")
        self._card_layout.addWidget(self._input_picker)
        self._card_layout.addWidget(self._output_picker)

        # Quality slider
        quality_row = QHBoxLayout()
        quality_row.setSpacing(12)

        quality_lbl = QLabel("Qualidade:")
        quality_lbl.setObjectName("filePickerLabel")
        quality_row.addWidget(quality_lbl)

        self._slider = QSlider(Qt.Horizontal)
        self._slider.setRange(1, 3)
        self._slider.setValue(2)
        self._slider.setTickPosition(QSlider.TicksBelow)
        self._slider.setTickInterval(1)
        self._slider.setPageStep(1)
        quality_row.addWidget(self._slider, 1)

        self._quality_label = QLabel("Média")
        self._quality_label.setMinimumWidth(60)
        quality_row.addWidget(self._quality_label)

        self._slider.valueChanged.connect(self._update_quality_label)
        self._card_layout.addLayout(quality_row)

    def _update_quality_label(self, value: int):
        labels = {1: "Baixa", 2: "Média", 3: "Alta"}
        self._quality_label.setText(labels[value])

    def _validate(self) -> bool:
        if not self._input_picker.path():
            self._show_error("Selecione um PDF.")
            return False
        if not self._output_picker.path():
            self._show_error("Defina onde salvar o PDF comprimido.")
            return False
        return True

    def _get_worker(self):
        return CompressWorker(
            self._input_picker.path(),
            self._output_picker.path(),
            self._slider.value(),
        )

    def _reset_fields(self):
        self._input_picker.clear()
        self._output_picker.clear()
        self._slider.setValue(2)
