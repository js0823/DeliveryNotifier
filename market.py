from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
import sys, os

class AmazonFreshBot:
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("debuggerAddress", "localhost:9222")
        self.driver = webdriver.Chrome(chrome_options=self.chrome_options)
    
    def goToAvailabilityPage(self):
        # navigate to amazon's delivery page
        self.driver.get("https://smile.amazon.com")
        sleep(2)
        try:
            self.driver.find_element_by_id("nav-cart").click()
        except:
            self.driver.find_element_by_class_name('nav-cart').click()
        sleep(2)

        try:
            self.driver.find_element_by_name("proceedToALMCheckout-QW1hem9uIEZyZXNo").click()
        except:
            self.driver.find_element_by_css_selector("input[class='a-button-input'][value='Proceed to checkout']").submit()
        sleep(2)
        
        self.driver.find_element_by_name("proceedToCheckout").click()
        sleep(2)

    def checkAvailability(self, availabilities):
        # check if any slot is available
        is_available=False
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
        
        print("Slot is available!! Click now!")