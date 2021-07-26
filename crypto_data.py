import cryptocompare


def get_crypto_price(coin):

    crypto_price = cryptocompare.get_price(coin=coin,
                                           currency='USD',
                                           full=True)['RAW'][coin]['USD']['PRICE']

    return crypto_price


if __name__ == '__main__':

    pass
