from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from Smoketest.locatorfile.test_Locators import Locators_test
from selenium.webdriver.common.by import By
import time

class GuestPayment():

    def __init__(self,driver):
        self.driver = driver


    def guest_payment(self,driver):

        try:
            time.sleep(3)
            guest_price = self.driver.find_element(By.XPATH,Locators_test.guest_pricing_xpath).text
            if guest_price is guest_price:
                print("Guest price validated", guest_price)
            else:
                print("Guest price failed")
            time.sleep(2)
            self.driver.get(Locators_test.homePage)
            time.sleep(3)

        except StaleElementReferenceException or ElementClickInterceptedException or TimeoutException or NoSuchElementException as ex:
            print(ex.message)