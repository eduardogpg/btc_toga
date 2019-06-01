import requests

URL = 'https://api.bitso.com/v3/ticker/'

BITCOIN = 0
ETHERUM = 2
RIPPLE = 4
LITECOIN = 6

def get_cryptocurrency_price(currency=BITCOIN):
    response = requests.get(URL)

    if response.status_code == 200:
        json = response.json()
        payload = json.get('payload', [])
        if payload:
            return payload[currency]
        return dict()
