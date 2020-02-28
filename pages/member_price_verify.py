from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from Smoketest.locatorfile.test_Locators import Locators_test
from selenium.webdriver.common.by import By
import time

class MemberPrice():

    def __init__(self, driver):
        self.driver = driver

    def member_price(self,driver):
        try:
            time.sleep(3)
            productPrice = self.driver.find_element(By.XPATH, Locators_test.memberprice_xpath).text

            if productPrice is productPrice:
                print(productPrice)
            else:
                print("product price is not member price")

        except StaleElementReferenceException or ElementClickInterceptedException or TimeoutException or NoSuchElementException as ex:
            print(ex.message)