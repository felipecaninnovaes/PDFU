from views.pages.base_page import BasePage
from widgets.file_picker import FilePicker
from workers.docx_worker import DocxWorker


class DocxPage(BasePage):
    PAGE_TITLE = "PDF para Word"
    PAGE_SUBTITLE = "Converte um PDF em documento Word (.docx). Resultado pode variar conforme o PDF."

    def setup_ui(self):
        self._input_picker = FilePicker(label="Selecionar PDF:", mode="file", ext=".pdf")
        self._output_picker = FilePicker(label="Salvar Word em:", mode="save", ext=".docx")
        self._card_layout.addWidget(self._input_picker)
        self._card_layout.addWidget(self._output_picker)

    def _validate(self) -> bool:
        if not self._input_picker.path():
            self._show_error("Selecione um PDF.")
            return False
        if not self._output_picker.path():
            self._show_error("Defina onde salvar o arquivo Word.")
            return False
        return True

    def _get_worker(self):
        return DocxWorker(self._input_picker.path(), self._output_picker.path())

    def _reset_fields(self):
        self._input_picker.clear()
        self._output_picker.clear()
