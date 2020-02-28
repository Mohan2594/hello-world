from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from Smoketest.locatorfile.test_Locators import Locators_test
from selenium.webdriver.common.by import By
import time

class Search():

    def __init__(self,driver):
        self.driver = driver

    def test_Search(self,driver):

        try:
            time.sleep(3)
            while self.driver.find_element(By.XPATH,Locators_test.search_xpath).click() is True:
                break
            self.driver.find_element(By.XPATH,Locators_test.search_input_xpath).send_keys(Locators_test.search_term)
            time.sleep(2)
            selectSearchtext = self.driver.find_element(By.XPATH,Locators_test.search_results_xpath)
            #actions.move_to_element(selectSearchtext).click().perform()
            selectSearchtext.click()

            while self.driver.find_element(By.XPATH,Locators_test.qtyincrement_xpath).click() is True:
                break
        except StaleElementReferenceException or ElementClickInterceptedException or TimeoutException as ex:
            print(ex.message)








