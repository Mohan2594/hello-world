from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from Smoketest.locatorfile.test_Locators import Locators_test
from selenium.webdriver.common.by import By
import time


class Logout():

    def __init__(self,driver):
        self.driver = driver

    def test_Signout(self,driver):
        try:
            time.sleep(3)
            logout = self.driver.find_element(By.XPATH,Locators_test.logout_xpath)
            while logout.click() is True:
                break

        except NoSuchElementException or StaleElementReferenceException or ElementClickInterceptedException or TimeoutException as ex:
            print(ex.message)