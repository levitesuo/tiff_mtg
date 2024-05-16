from services.text_splicer import text_processor
from services.pdf_sticher import PdfMaker


class UiService:
    def __init__(self):
        self.pdf_maker = PdfMaker()
        self.text = None
        self.dpi = None
        self.mark = None
        self.filename = None

    def init(self, text, dpi, mark, filename):
        self.text = text_processor(text)
        self.dpi = int(dpi)
        self.mark = int(mark)
        self.filename = filename

    def run(self, set_progres):
        self.pdf_maker.add_cards(self.text, self.dpi, self.mark, set_progres)
        self.pdf_maker.save(self.filename)


service = UiService()
