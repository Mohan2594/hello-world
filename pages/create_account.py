from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from Smoketest.locatorfile.test_Locators import Locators_test
from selenium.webdriver.common.by import By
import time

class CreateAccount():

    def __init__(self, driver):
        self.driver = driver

    def verify_create_account(self,driver):
        try:
            time.sleep(3)
            while self.driver.find_element(By.XPATH ,Locators_test.createaccount_xpath).click() is True:
                break
            time.sleep(2)
            verifyPage = self.driver.title

            if verifyPage is verifyPage:
                self.driver.back()
                print(verifyPage, "is the createaccount page")
            else:
                print("Create an account link failed")
        except StaleElementReferenceException or ElementClickInterceptedException or TimeoutException or NoSuchElementException as ex:
            print(ex.message)