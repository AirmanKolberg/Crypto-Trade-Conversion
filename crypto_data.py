import cryptocompare


def get_crypto_supply(coin):

    total_supply = cryptocompare.get_price(coin=coin,
                                           currency='USD',
                                           full=True)['RAW'][coin]['USD']['SUPPLY']

    return total_supply


if __name__ == '__main__':

    pass
