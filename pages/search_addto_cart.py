from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from Smoketest.locatorfile.test_Locators import Locators_test
from selenium.webdriver.common.by import By
import time

class SearchAdd():

    def __init__(self,driver):
        self.driver = driver

    def test_search_tocart(self,driver):

        try:
            time.sleep(3)
            addtocart = self.driver.find_element(By.XPATH,Locators_test.addtocart_xpath)
            while addtocart.click() is True:
                break
            time.sleep(5)
            self.driver.find_element(By.XPATH,Locators_test.search_page_xpath).click()
            time.sleep(2)

        except StaleElementReferenceException or ElementClickInterceptedException or TimeoutException as ex:
            print(ex.message)