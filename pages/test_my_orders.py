from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from Smoketest.locatorfile.test_Locators import Locators_test
from selenium.webdriver.common.by import By
import time

class MyAccount():

    def __init__(self,driver):
        self.driver = driver


    def test_user_account(self,driver):
        try:
            time.sleep(3)
            myacccountbutton = self.driver.find_element(By.XPATH, Locators_test.myaccount_xpath)
            myacccountbutton.click()
            time.sleep(3)

            try:
                myOrders = self.driver.find_element(By.XPATH,Locators_test.myorders_xpath).text
                time.sleep(3)
                print("Verified my", myOrders)
                time.sleep(3)
            except NoSuchElementException:
                print("My orders not displaying")
                time.sleep(2)

        except StaleElementReferenceException or ElementClickInterceptedException or TimeoutException as ex:
            print(ex.message)

