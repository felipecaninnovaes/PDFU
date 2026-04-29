from views.pages.base_page import BasePage
from widgets.file_picker import FilePicker
from workers.split_worker import SplitWorker


class SplitPage(BasePage):
    PAGE_TITLE = "Dividir PDF"
    PAGE_SUBTITLE = "Separa cada página do PDF em arquivos individuais."

    def setup_ui(self):
        self._input_picker = FilePicker(label="Selecionar PDF:", mode="file", ext=".pdf")
        self._output_picker = FilePicker(
            label="Prefixo para os arquivos gerados:",
            mode="save",
            ext=".pdf",
            button_text="Escolher",
        )
        self._card_layout.addWidget(self._input_picker)
        self._card_layout.addWidget(self._output_picker)

    def _validate(self) -> bool:
        if not self._input_picker.path():
            self._show_error("Selecione um PDF para dividir.")
            return False
        if not self._output_picker.path():
            self._show_error("Defina o prefixo de saída.")
            return False
        return True

    def _get_worker(self):
        output = self._output_picker.path().replace(".pdf", "").replace(".PDF", "")
        return SplitWorker(self._input_picker.path(), output)

    def _reset_fields(self):
        self._input_picker.clear()
        self._output_picker.clear()
