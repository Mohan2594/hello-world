from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from Smoketest.locatorfile.test_Locators import Locators_test
from selenium.webdriver.common.by import By
import time

class DiscountValidation():

    def __init__(self,driver):
        self.driver=driver

    def test_discount_validation(self,driver):

        try:
            time.sleep(3)
            mini_cart = self.driver.find_element(By.XPATH,Locators_test.minicart_xpath)
            while mini_cart.click() is True:
                break
            time.sleep(5)
            go_to_cart = self.driver.find_element(By.XPATH,Locators_test.gotocart_xpath)
            while go_to_cart.click() is True:
                break
            time.sleep(5)

            try:
                verify_cart_price_rule = self.driver.find_element(By.XPATH,Locators_test.cartpricerule_xpath).text
                print("Verified", verify_cart_price_rule)
            except NoSuchElementException:
                print("Cart price rule not applied")

            self.driver.find_element(By.XPATH,Locators_test.checkout_xpath).click()
            time.sleep(5)

        except StaleElementReferenceException or ElementClickInterceptedException or TimeoutException or NoSuchElementException as ex:
            print(ex.message)

