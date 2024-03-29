import os

WIDTH = 400
HEIGHT = 600

SIZE = (WIDTH, HEIGHT)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ICON_DIR = os.path.join(BASE_DIR, 'resources')

BTC_ICON = os.path.join(ICON_DIR, 'btc.png')
PADDING_VALUES = (WIDTH / 2) * 0.09
PADDING_BOTTOM_VAL = 20
