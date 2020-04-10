from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import sys, os

class AmazonBot:
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("debuggerAddress", "localhost:9222")
        self.driver = webdriver.Chrome(chrome_options=self.chrome_options)
    
    def goToCart(self):
        # navigate to cart
        print("Going to Amazon Smile page.")
        self.driver.get("https://smile.amazon.com")
        sleep(2)

        print("Accessing the cart.")
        try:
            self.driver.find_element_by_id("nav-cart").click()
            sleep(2)
        except NoSuchElementException:
            print("Could not access cart. Aborting")
            self.driver.quit()
    
    def checkAvailability(self, availabilities):
        # check if any slot is available
        is_available = False
        for availability in availabilities:
            availability_innerHTML=availability.get_attribute('innerHTML').strip().lower()
            if availability_innerHTML != "not available":
                is_available=True
                break

        return is_available

    def run(self):
        # run the bot
        slotsAvailable = False
        while not slotsAvailable:
            sleep(3)
            slotsAvailable = self.checkAvailability(self.driver. \
                find_elements_by_xpath("//div[@class='ufss-date-select-toggle-text-availability']"))
            
            if not slotsAvailable:
                print("Slot is not available. Trying again in 15 seconds.")
                sleep(15)
                self.driver.refresh()
        
        for _ in range(1000):
            self.foundAlert()
            print("Slot is available!! Click now!")
            
        self.driver.quit()
    
    def foundAlert(self):
        if sys.platform == "linux" or sys.platform == "linux2":
            os.system('spd-say "Slot found."')
        elif sys.platform == "darwin":
            os.system('say "Slot found."')

class AmazonFreshBot(AmazonBot):
    def __init__(self):
        super().__init__()
    
    def goToDeliveryPage(self):
        try:
            print("Checking out Amazon Fresh page.")
            self.driver.find_element_by_name("proceedToALMCheckout-QW1hem9uIEZyZXNo").click()
            sleep(2)
        except NoSuchElementException:
            print("Could not check out Amnazon Fresh page. Aborting.")
            self.driver.quit()
        
        try:
            print("Navigating to delivery page.")
            self.driver.find_element_by_name("proceedToCheckout").click()
            sleep(2)
        except NoSuchElementException:
            print("Could not go to delivery page. Aborting.")
            self.driver.quit()

class WholeFoodsBot(AmazonBot):
    def __init__(self):
        super().__init__()
    
    def goToDeliveryPage(self):
        try:
            print("Checking out WholeFoods page.")
            self.driver.find_element_by_name("proceedToALMCheckout-VUZHIFdob2xlIEZvb2Rz").click()
            sleep(2)
        except NoSuchElementException:
            print("Could not check out WholeFoods page. Aborting.")
            self.driver.quit()
        
        try:
            print("Navigating to substitution page.")
            self.driver.find_element_by_name("proceedToCheckout").click()
            sleep(2)
        except NoSuchElementException:
            print("Could not go to substitution page. Aborting.")
            self.driver.quit()
        
        try:
            print("Navigating to delivery page.")
            self.driver.find_element_by_class_name("a-button-input").click()
            sleep(2)
        except NoSuchElementException:
            print("Could not go to delivery page. Aborting")
            self.driver.quit()