from twilio_functions import twilio_call, twilio_text
from secrets import coins
from crypto_data import get_crypto_price


if __name__ == '__main__':
    
    # Declare empty list for coin values
    values = list()

    # Retrieve coin prices
    for coin in coins:

        if coin == dict:
            print('yes')

        # coin_value = get_crypto_price(coin)
        # values.append(coin_value)
    
    print(values)


