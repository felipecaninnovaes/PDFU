from views.pages.base_page import BasePage
from widgets.file_picker import FilePicker
from workers.image_worker import ImageWorker


class ImagePage(BasePage):
    PAGE_TITLE = "Converter Imagem para PDF"
    PAGE_SUBTITLE = "Converte uma imagem (JPG, PNG, BMP, etc.) em um arquivo PDF."

    def setup_ui(self):
        self._input_picker = FilePicker(
            label="Selecionar imagem:",
            mode="file",
            ext="",
            button_text="Procurar",
        )
        self._output_picker = FilePicker(label="Salvar PDF em:", mode="save", ext=".pdf")
        self._card_layout.addWidget(self._input_picker)
        self._card_layout.addWidget(self._output_picker)

    def _validate(self) -> bool:
        if not self._input_picker.path():
            self._show_error("Selecione uma imagem.")
            return False
        if not self._output_picker.path():
            self._show_error("Defina o caminho para salvar o PDF.")
            return False
        return True

    def _get_worker(self):
        return ImageWorker(self._input_picker.path(), self._output_picker.path())

    def _reset_fields(self):
        self._input_picker.clear()
        self._output_picker.clear()
