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
        self.driver.get("https://smile.amazon.com")
        sleep(2)
        self.driver.find_element_by_id("nav-cart").click()
        sleep(2)
        self.driver.find_element_by_name("proceedToALMCheckout-QW1hem9uIEZyZXNo").click()
        sleep(2)
        self.driver.find_element_by_name("proceedToCheckout").click()
    
    def run(self):
        # run the bot
        slotAvailable = False

        while not slotAvailable:
            # TODO
            pass