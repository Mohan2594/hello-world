from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from Smoketest.locatorfile.test_Locators import Locators_test
from selenium.webdriver.common.by import By
import time

class RecentlyViewed():

    def __init__(self,driver):
        self.driver = driver

    def test_recently(self,driver):

        try:
            time.sleep(3)
            recentlyViewed = self.driver.find_element(By.XPATH, Locators_test.recentlyviewed_xpath).text
            print(recentlyViewed, "is present")

        except StaleElementReferenceException or ElementClickInterceptedException or TimeoutException as ex:
            print(recentlyViewed, "is not present")