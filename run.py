import sys
from market import AmazonFreshBot
from market import WholeFoodsBot

def main():
    s = """
    Welcome to Auto Delivery Notifier.

    This program intends to notify user of delivery when delivery is available.
    Please make sure Chrome is logged into Amazon, the basket is not empty,
    and you are able to proceed to delivery page manually.
    Also make sure you can navigate to delivery page without any errors in your cart.
    """
    print(s)
    # choose market
    markets = ["Amazon Fresh", "WholeFoods"]
    choice = None
    while True:
        print("Please choose a number for the market you wish to buy from. \n")
        for i, market in enumerate(markets):
            print("{}) {}".format(i + 1, market))
        choice = input("Enter number: ")
        if not choice.isdigit() or not 1 <= int(choice) <= len(markets):
            print("Sorry. Please choose again. \n")
        else:
            break

    if choice == '1':
        bot = AmazonFreshBot()
        bot.goToCart()
        bot.goToDeliveryPage()
        bot.run()
    elif choice == '2':
        bot = WholeFoodsBot()
        bot.goToCart()
        bot.goToDeliveryPage()
        bot.run()
    
    exit()

if __name__ == "__main__":
    main()