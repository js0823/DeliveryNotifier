import sys
from market import AmazonFreshBot
from market import WholeFoodsBot

def main():
    print("Welcome to auto delivery service.")
    print("This program intends to notify user of delivery when delivery is available.")
    print("Please make sure Chrome is logged into Amazon, and the basket is not empty.")
    print("Also make sure you can navigate to delivery page without any errors in your cart.")

    # choose market
    market = None
    while True:
        market = input("Choose market via number (AmazonFresh(1), WholeFoods(2)): ")
        if not market.isdigit() or not 1 <= int(market) <= 2:
            print("Sorry. Please choose a number (1 or 2).")
        else:
            break

    if market == '1':
        bot = AmazonFreshBot()
        bot.goToCart()
        bot.goToDeliveryPage()
        bot.run()
    elif market == '2':
        bot = WholeFoodsBot()
        bot.goToCart()
        bot.goToDeliveryPage()
        bot.run()
    
    exit()

if __name__ == "__main__":
    main()