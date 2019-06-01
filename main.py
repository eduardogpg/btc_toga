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
        self.create_price_elements_value_label()

    def create_image(self):
        image = toga.Image(BTC_ICON)
        self.logo = toga.ImageView(image=image, style=Pack(
            width=150, height=150,
            padding_top=25, padding_bottom=25
        ))

    def create_price_label(self):
        self.price = toga.Label('$169,996.99', style=Pack(
            font_family=MONOSPACE, font_size=24,
            font_weight=BOLD,
            text_align=CENTER
        ))

    def create_currency_label(self):
        self.currency = toga.Label('BTC/MXN')
        self.currency.style.update(font_family=MONOSPACE,
                                    font_size=18, padding_top=10,
                                    text_align=CENTER, color='GREEN')

    def create_price_elements_label(self):
        style = Pack(color='GREEN', alignment=CENTER, font_size=16, padding_left=40, padding_bottom=5)

        self.bid = toga.Label('Bid', style=style)
        self.ask = toga.Label('Ask', style=style)
        self.low = toga.Label('Low', style=style)
        self.high = toga.Label('High', style=style)
        self.volume = toga.Label('24 H Volume', style=style)
        self.spread = toga.Label('Spread', style=style)

        self.volume.style.update(padding_left=10)
        self.spread.style.update(padding_left=30)

    def create_price_elements_value_label(self):
        style = Pack(color='BLACK', alignment=CENTER, font_size=18, padding_bottom=PADDING_BOTTOM_VAL)
        #120
        self.bid_val = toga.Label('$169,003.39', style=style)
        self.ask_val = toga.Label('$169,899.82', style=style)
        self.low_val = toga.Label('$161,500.00', style=style)
        self.high_val = toga.Label('$170,960.87', style=style)
        self.volume_val = toga.Label('207.76', style=style)
        self.spread_val = toga.Label('0.53%', style=style)

        self.volume_val.style.update(padding_left=23)
        self.spread_val.style.update(padding_left=30)

    def startup(self):
        self.main_window = toga.MainWindow('main', title=self.title, size=self.size)

        top_container = toga.Box(children=[self.logo, self.price, self.currency],
            style=Pack(
                direction=COLUMN, alignment=CENTER
        ))

        bottom_container = toga.SplitContainer()
        right = toga.Box(
            children=[self.bid, self.bid_val, self.low, self.low_val, self.volume, self.volume_val],
            style=Pack(
                direction=COLUMN,
                padding_left=40, padding_top=20
            )
        )
        left = toga.Box(
            children=[self.ask, self.ask_val, self.high, self.high_val, self.spread, self.spread_val],
            style=Pack(
                direction=COLUMN,
                padding_left=40, padding_top=20
            )
        )
        bottom_container.content = [right, left]

        split = toga.SplitContainer(direction=toga.SplitContainer.HORIZONTAL)
        split.content = [top_container, bottom_container]

        self.main_window.content = split
        self.main_window.show()

if __name__ == '__main__':
    btc = BTC('com.codigofacilito.btc', 'BTC price')
    btc.main_loop()
