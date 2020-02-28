from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from Smoketest.locatorfile.test_Locators import Locators_test
from selenium.webdriver.common.by import By
import time

class AddToCart():

    def __init__(self,driver):
        self.driver = driver

    def add_to_cart(self,driver):

            try:
                time.sleep(3)
                addtoCart = self.driver.find_element(By.XPATH ,Locators_test.addtocart_xpath)
                while addtoCart.click() is True:
                    break
                time.sleep(2)
                self.driver.find_element(By.XPATH,Locators_test.postaddtocart_xpath).click()

            except StaleElementReferenceException or ElementClickInterceptedException or TimeoutException or NoSuchElementException as ex:
                print(ex.message)