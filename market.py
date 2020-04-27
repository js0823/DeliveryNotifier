from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import sys, os
import random
from datetime import datetime
import pygame

class AmazonBot:
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("debuggerAddress", "localhost:9222")
        self.driver = webdriver.Chrome(chrome_options=self.chrome_options)
        self.musicSet = False
    
    def foundAlert(self):
        if not self.musicSet:
            root_dir = os.path.abspath(os.path.dirname(__file__))
            sound_path = os.path.join(root_dir, "slotfound.mp3")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_path)
            self.musicSet = True

        pygame.mixer.music.play()

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
            exit()
    
    def checkAvailability(self, availabilities):
        # check if any slot is available
        is_available = False
        if not availabilities:
            print("Delivery date availability could not be found on the page.")
            print("Please check whether current webpage is the delivery webpage. Aborting.")
            self.driver.quit()
            exit()

        for availability in availabilities:
            availability_innerHTML = availability.get_attribute('innerHTML').strip().lower()
            if availability_innerHTML != "not available":
                is_available=True
                break

        return is_available

    def run(self):
        # run the bot
        slotsAvailable = False
        while not slotsAvailable:
            sleep(2)
            slotsAvailable = self.checkAvailability(self.driver. \
                find_elements_by_xpath("//div[@class='ufss-date-select-toggle-text-availability']"))
            
            if not slotsAvailable:
                randomTime = random.randrange(10, 60, 5)
                now = datetime.now().strftime("%H:%M:%S")
                print("No slots available at {}. Trying again in {} seconds.".format(now, randomTime))
                sleep(randomTime)
                self.driver.refresh()
        
        for _ in range(100):
            self.foundAlert()
            print("Slot is available!! Click now!")
            sleep(2)
            
        self.driver.quit()

class AmazonFreshBot(AmazonBot):
    def __init__(self):
        super().__init__()
    
    def goToDeliveryPage(self):
        try:
            print("Checking out Amazon Fresh page.")
            self.driver.find_element_by_name("proceedToALMCheckout-QW1hem9uIEZyZXNo").click()
            sleep(2)
        except NoSuchElementException:
            print("Could not check out Amazon Fresh page. Aborting.")
            self.driver.quit()
            exit()
        
        try:
            print("Navigating to delivery page.")
            self.driver.find_element_by_name("proceedToCheckout").click()
            sleep(2)
        except NoSuchElementException:
            print("Could not go to delivery page. Aborting.")
            self.driver.quit()
            exit()

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
            exit()
        
        try:
            print("Navigating to substitution page.")
            self.driver.find_element_by_name("proceedToCheckout").click()
            sleep(2)
        except NoSuchElementException:
            print("Could not go to substitution page. Aborting.")
            self.driver.quit()
            exit()
        
        try:
            print("Navigating to delivery page.")
            self.driver.find_element_by_class_name("a-button-input").click()
            sleep(2)
        except NoSuchElementException:
            print("Could not go to delivery page. Aborting")
            self.driver.quit()
            exit()