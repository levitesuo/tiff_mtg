from services.image_sticher import PageMaker
from repository.card import getCardImages
from PIL import ImageFile


class PdfMaker:
    def __init__(self):
        self.dpi = None
        self.mark = None
        self._pdf = []

    def _add_page_to_pdf(self, cards):
        page = self.page_maker.get_page_png(cards)
        self._pdf.append(page)

    def add_cards(self, card_data_list, dpi, mark, set_progres):
        self.page_maker = PageMaker(dpi, mark)
        card_images = []
        size = len(card_data_list)
        for i, card_data in enumerate(card_data_list):
            images = getCardImages(card_data)
            set_progres((i+1)/size)
            for _ in range(int(card_data['amount'])):
                for im in images:
                    card_images.append(im)
        cards = []
        for i, card_image in enumerate(card_images):
            if i % 9 == 0:
                cards = []
            cards.append(card_image)
            if i % 9 == 8:
                self._add_page_to_pdf(cards)
        if len(cards) != 9:
            self._add_page_to_pdf(cards)

    def save(self, filename):
        ImageFile.LOAD_TRUNCATED_IMAGES = True
        first_image = self._pdf[0].convert('RGB')
        if len(self._pdf) > 1:
            rest = [im.convert('RGB') for im in self._pdf[1:]]
            first_image.save(filename, save_all=True,
                             append_images=rest)
        else:
            first_image.save(fp=filename)
