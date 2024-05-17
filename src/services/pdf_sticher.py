from services.image_sticher import PageMaker
from repository.card import getCardImages
from PIL import ImageFile
import os


class PdfMaker:
    def __init__(self):
        self.dpi = None
        self.mark = None
        self.page_num = 0
        self.page_maker = None
        self.filename = "deck"

    def _add_page_to_pdf(self, cards):
        ImageFile.LOAD_TRUNCATED_IMAGES = True
        page = self.page_maker.get_page_png(cards).convert('RGB')
        page.save(f"pages/{self.filename}_page_{self.page_num}.pdf")

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
                self.page_num += 1
        if len(cards) != 9:
            self._add_page_to_pdf(cards)
