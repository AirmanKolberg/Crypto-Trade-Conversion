from system_functions import clear_screen
from twilio_functions import twilio_call, twilio_text
from secrets import coins, my_number
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


# Determine the amount of Coin 2 the user wishes to receive from transferring Coin 1
def get_coin_goal():

    try:
        
        goal_amount = float(input('How much of Coin 2 are you looking to receive?\n'))

    except ValueError:

        print("Numbers only, please try again...")
        get_coin_goal()
    
    else:

        return goal_amount



if __name__ == '__main__':

    clear_screen()

    goal_amount = get_coin_goal()

    checking_prices = True
    
    while checking_prices:

        clear_screen()

        extra = determine_extra_coins()
        print(extra)
        print(f'Goal: {goal_amount}')

        if extra >= goal_amount:

            # Notify me
            twilio_text(f'Trade now!\nConversion to {extra} coins!', my_number)
            twilio_call(my_number)

            # Stop updating/checking
            checking_prices = False
        
        # Check again in ten minutes
        sleep(60 * 10)
