from PIL import Image


class PageMaker:
    def __init__(self, dpi, mark):
        self.dpi = dpi
        self.a4_width = int(8.3 * dpi)
        self.a4_height = int(self.a4_width * 1.4142)
        self.card_width = int(0.3*self.a4_width)
        self.card_height = int(0.41904761904*self.a4_width)
        self.x_marg = int((self.a4_width - self.card_width * 3)/2)
        self.y_marg = int((self.a4_height - self.card_height * 3)/2)

        self.mark_size = mark

    def get_page_png(self, card_image_list):
        page = Image.new(mode='RGBA', size=(
            self.a4_width, self.a4_height), color=(24, 21, 16, 255))
        for i, image in enumerate(card_image_list):
            x = i // 3
            y = i % 3
            scaled = image.resize(
                size=(self.card_width, self.card_height), resample=Image.LANCZOS)
            page.paste(im=scaled, box=(self.card_width * x +
                                       self.x_marg, self.card_height * y + self.y_marg), mask=scaled)
        if not self.mark_size:
            return page
        for i in range(9):
            x = i // 3
            y = i % 3
            hori_mark_im = Image.new(mode='RGBA', size=(7, self.mark_size),
                                     color=(255, 255, 255, 255))
            vert_mark_im = Image.new(mode='RGBA', size=(self.mark_size, 7),
                                     color=(255, 255, 255, 255))
            if x == 0:
                for j in range(2):
                    page.paste(im=vert_mark_im, box=(
                        self.x_marg - vert_mark_im.size[0], self.card_height * (y+j) + self.y_marg))
            if y == 0:
                for j in range(2):
                    page.paste(im=hori_mark_im, box=(
                        self.card_width * (x+j) + self.x_marg, self.y_marg - hori_mark_im.size[1]))
            if x == 2:
                for j in range(2):
                    page.paste(im=vert_mark_im, box=(
                        self.card_width * 3 + self.x_marg, self.card_height * (y+j) + self.y_marg))
            if y == 2:
                for j in range(2):
                    page.paste(im=hori_mark_im, box=(
                        self.card_width * (x+j) + self.x_marg, self.card_height * 3 + self.y_marg))
        return page
