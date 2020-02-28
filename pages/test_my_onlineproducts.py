from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from Smoketest.locatorfile.test_Locators import Locators_test
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class MyOnlineproducts():

    def __init__(self,driver):

        self.driver = driver

    def test_myonlineproducts(self,driver):

        try:
            time.sleep(3)
            actions = ActionChains(self.driver)
            myOnlinceproducts = self.driver.find_element(By.XPATH,Locators_test.myonlineproducts_xpath)
            actions.move_to_element(myOnlinceproducts).click().perform()
            time.sleep(3)


            windows = []
            windows = self.driver.window_handles
            self.driver.switch_to.window(windows[1])
            time.sleep(3)
            self.driver.close()
            time.sleep(3)
            self.driver.switch_to.window(windows[0])
            print("Verified My Online products open in new tab")

        except StaleElementReferenceException or ElementClickInterceptedException or TimeoutException as ex:
            print(ex.message)