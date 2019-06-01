import toga
import time
import threading

from toga.style import Pack
from toga.style.pack import *

from cryptocurrency import get_cryptocurrency_price

from const import *

class BTC(toga.App):

    def __init__(self, id, title):
        toga.App.__init__(self, title, id)

        self.title = title
        self.size = SIZE

        self.variables()
        self.create_components()
        self.start_clock()

    def variables(self):
        self.v_bid = ''

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
        self.volume_24 = toga.Label('24 H Change', style=style)
        self.volume = toga.Label('Volume', style=style)

        self.volume_24.style.update(padding_left=10)
        self.volume.style.update(padding_left=30)

    def create_price_elements_value_label(self):
        style = Pack(color='BLACK', alignment=CENTER, font_size=18, padding_bottom=PADDING_BOTTOM_VAL)

        self.bid_val = toga.Label(self.v_bid, style=style)
        self.ask_val = toga.Label('', style=style)
        self.low_val = toga.Label('', style=style)
        self.high_val = toga.Label('', style=style)
        self.volume_24_val = toga.Label('', style=style)
        self.volume_val = toga.Label('', style=style)

        self.volume_24_val.style.update(padding_left=23)
        self.volume_val.style.update(padding_left=30)

    def startup(self):
        self.main_window = toga.MainWindow('main', title=self.title, size=self.size)

        self.top_container = toga.Box(children=[self.logo, self.price, self.currency],
            style=Pack(
                direction=COLUMN, alignment=CENTER
        ))

        self.bottom_container = toga.SplitContainer()
        right = toga.Box(
            children=[self.bid, self.bid_val, self.low, self.low_val, self.volume_24, self.volume_24_val],
            style=Pack(
                direction=COLUMN,
                padding_left=40, padding_top=20
            )
        )
        left = toga.Box(
            children=[self.ask, self.ask_val, self.high, self.high_val, self.volume, self.volume_val],
            style=Pack(
                direction=COLUMN,
                padding_left=40, padding_top=20
            )
        )
        self.bottom_container.content = [right, left]

        self.split = toga.SplitContainer(direction=toga.SplitContainer.HORIZONTAL)
        self.split.content = [self.top_container, self.bottom_container]

        self.main_window.content = self.split
        self.main_window.show()

    def update_values(self):
        currency = get_cryptocurrency_price()
        print(currency)

        self.bid_val.text = self.dolar_format(self.get_price(currency, 'bid'))
        self.low_val.text = self.dolar_format(self.get_price(currency, 'low'))
        self.ask_val.text = self.dolar_format(self.get_price(currency, 'ask'))
        self.high_val.text = self.dolar_format(self.get_price(currency, 'high'))
        self.volume_24_val.text = self.get_price(currency, 'change_24')
        self.volume_val.text = '{:3,.2f}'.format(self.get_price(currency, 'volume'))

    def get_price(self, currency, key):
        return float(currency.get(key, '0'))

    def dolar_format(self, val):
        return '${:3,.2f}'.format(val)

    def __clock(self):
        self.update_values()

    def start_clock(self):
        p = threading.Thread(target=self.__clock)
        p.start()
        p.join()

if __name__ == '__main__':
    btc = BTC('com.codigofacilito.btc', 'BTC price')
    btc.main_loop()
