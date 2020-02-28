from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from Smoketest.locatorfile.test_Locators import Locators_test
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

class ListingPage():

    def __init__(self,driver):
        self.driver = driver

    def listing_page(self,driver):

        try:
            time.sleep(3)
            actions = ActionChains(self.driver)
            Category1 = self.driver.find_element(By.XPATH,Locators_test.category1_xpath)
            actions.move_to_element(Category1).perform()
            time.sleep(2)

            SubCategory1 = self.driver.find_element(By.XPATH,Locators_test.subcategory1_xpath)
            actions.move_to_element(SubCategory1).click().perform()
            time.sleep(2)
            s1 = self.driver.find_element(By.XPATH,Locators_test.s1_xpath).text
            print("BCSC ", s1)

            self.driver.execute_script("window.scrollBy(0,100);")
            time.sleep(2)

            layerFilter1 = self.driver.find_element(By.XPATH,Locators_test.layerfilter_xpath)
            while layerFilter1.click() is True:
                break

            self.driver.execute_script("window.scrollBy(0,-120);")
            time.sleep(2)
            pdp1 = self.driver.find_element(By.XPATH,Locators_test.pdp_xpath)
            while pdp1.click() is True:
                break

        except StaleElementReferenceException or ElementClickInterceptedException or TimeoutException or NoSuchElementException as ex:
            print(ex.message)
