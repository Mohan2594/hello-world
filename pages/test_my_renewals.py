from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from Smoketest.locatorfile.test_Locators import Locators_test
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class MyRenewals():

    def __init__(self,driver):
        self.driver = driver

    def test_myrenewals(self,driver):

        try:
            time.sleep(3)
            actions3 = ActionChains(self.driver)
            myRenewals = self.driver.find_element(By.XPATH,Locators_test.myrenewals_xpath)
            actions3.move_to_element(myRenewals).click().perform()
            time.sleep(3)

            windows = []
            windows = self.driver.window_handles
            self.driver.switch_to.window(windows[1])
            time.sleep(3)
            self.driver.close()
            self.driver.switch_to.window(windows[0])
            time.sleep(3)
            print("Verified My Renewals open in new tab")
        except StaleElementReferenceException or ElementClickInterceptedException or TimeoutException as ex:
            print(ex.message)