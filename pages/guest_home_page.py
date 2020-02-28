from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from Smoketest.locatorfile.test_Locators import Locators_test
from selenium.webdriver.common.by import By
import time

class GuestHome():

    def __init__(self,driver):
        self.driver = driver

    def test_guest(self,driver):

        try:
            time.sleep(3)
            self.driver.execute_script("window.scrollBy(0,300);")
            time.sleep(2)
            newProducts = self.driver.find_element(By.XPATH,Locators_test.newProducts_xpath)
            while newProducts.click() is True:
                break
            mostpopular = self.driver.find_element(By.XPATH,Locators_test.mostpopular_xpath)
            while mostpopular.click() is True:
                break
            time.sleep(2)
            print(newProducts.text, mostpopular.text, "are clicked")
        except StaleElementReferenceException or ElementClickInterceptedException or TimeoutException as ex:
            print(ex.message)

