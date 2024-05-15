from services.image_sticher import PageMaker
from repository.card import getCardImages
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True


class PdfMaker:
    def __init__(self, dpi, mark):
        self.page_maker = PageMaker(dpi, mark)
        self._pdf = []

    def _add_page_to_pdf(self, cards):
        page = self.page_maker.get_page_png(cards)
        self._pdf.append(page)

    def add_cards(self, card_data_list):
        card_images = []
        for i, card_data in enumerate(card_data_list):
            images = getCardImages(card_data)
            print(f"{i+1}/{len(card_data_list)}")
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
        if len(self._pdf) > 1:
            self._pdf[0].save(filename, save_all=True,
                              append_images=self._pdf[1:])
        else:
            self._pdf[0].save(fp=filename)
