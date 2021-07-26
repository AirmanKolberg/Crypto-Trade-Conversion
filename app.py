from twilio_functions import twilio_call, twilio_text
from secrets import coins
from crypto_data import get_crypto_price
from time import sleep


def determine_extra_coins():

    # Declare empty list for coin values
    values = list()

    # Declare ticker to multiply only sell-coin by amount held
    ticker = 0

    # Retrieve coin prices
    for coin in coins:

        coin_value = get_crypto_price(coin)

        if ticker == 0:
            
            # Multiply value by amount
            coin_value = (coin_value * coins[coin]).__round__(2)
            ticker += 1

        values.append(coin_value)
    
    extra = (values[0] / values[1]).__round__(2)

    return extra


if __name__ == '__main__':
    
    

