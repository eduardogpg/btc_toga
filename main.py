import toga
from toga.style import Pack
from toga.style.pack import *

from const import *

class BTC(toga.App):

    def __init__(self, id, title):
        toga.App.__init__(self, title, id)

        self.title = title
        self.size = SIZE

        self.create_components()

    def create_components(self):
        self.create_image()
        self.create_price_label()
        self.create_currency_label()
        self.create_price_elements_label()

    def create_image(self):
        image = toga.Image(BTC_ICON)
        self.logo = toga.ImageView(image=image, style=Pack(
            width=150, height=150,
            padding_top=20
        ))

    def create_price_label(self):
        self.price = toga.Label('$169,996.99', style=Pack(
            font_family=MONOSPACE, font_size=24,
            font_weight=BOLD,
            padding_top=40, text_align=CENTER
        ))

    def create_currency_label(self):
        self.currency = toga.Label('BTC/MXN')
        self.currency.style.update(font_family=MONOSPACE,
                                    font_size=18, padding_top=10,
                                    text_align=CENTER, color='GREEN')

    def create_price_elements_label(self):
        pass

    def startup(self):
        self.main_window = toga.MainWindow('main', title=self.title, size=self.size)

        top_container = toga.Box(children=[self.logo, self.price, self.currency],
            style=Pack(
                direction=COLUMN, alignment=CENTER
        ))

        bottom_container = toga.Box()

        split = toga.SplitContainer(direction=toga.SplitContainer.HORIZONTAL)
        split.content = [top_container, bottom_container]

        self.main_window.content = split
        self.main_window.show()

if __name__ == '__main__':
    btc = BTC('com.codigofacilito.btc', 'BTC price')
    btc.main_loop()
