from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from Smoketest.locatorfile.test_Locators import Locators_test
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class ListingPage3():

    def __init__(self,driver):
        self.driver = driver

    def listing_page_3(self,driver):

        try:
            time.sleep(3)
            actions3 = ActionChains(self.driver)
            Category3 = self.driver.find_element(By.XPATH, Locators_test.category3_xpath)
            actions3.move_to_element(Category3).perform()
            SubCategory3 = self.driver.find_element(By.XPATH,Locators_test.subcategory3_xpath)
            while SubCategory3.click() is True:
                break
            try:
                s1 = self.driver.find_element(By.XPATH,Locators_test.s1_xpath).text
                print("AAOE Coding & Reimb.", s1)
            except NoSuchElementException:
                print(s1)

            while self.driver.find_element(By.XPATH,Locators_test.pdp1_xpath).click() is True:
                break

        except StaleElementReferenceException or ElementClickInterceptedException or TimeoutException as ex:
            print(ex.message)