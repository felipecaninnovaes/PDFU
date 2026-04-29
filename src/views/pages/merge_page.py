from views.pages.base_page import BasePage
from widgets.file_picker import FilePicker
from workers.merge_worker import MergeWorker


class MergePage(BasePage):
    PAGE_TITLE = "Juntar PDFs"
    PAGE_SUBTITLE = "Combina todos os PDFs de uma pasta em um único arquivo."

    def setup_ui(self):
        self._folder_picker = FilePicker(label="Pasta com os PDFs:", mode="folder")
        self._output_picker = FilePicker(label="Salvar resultado em:", mode="save", ext=".pdf")
        self._card_layout.addWidget(self._folder_picker)
        self._card_layout.addWidget(self._output_picker)

    def _validate(self) -> bool:
        if not self._folder_picker.path():
            self._show_error("Selecione a pasta com os PDFs.")
            return False
        if not self._output_picker.path():
            self._show_error("Defina o caminho para salvar o arquivo.")
            return False
        return True

    def _get_worker(self):
        return MergeWorker(self._folder_picker.path(), self._output_picker.path())

    def _reset_fields(self):
        self._folder_picker.clear()
        self._output_picker.clear()
