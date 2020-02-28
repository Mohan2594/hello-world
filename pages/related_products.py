from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from Smoketest.locatorfile.test_Locators import Locators_test
from selenium.webdriver.common.by import By
import time

class RelatedProducts():

    def __init__(self, driver):
        self.driver = driver

    def verify_related_products(self,driver):
        try:
            time.sleep(3)
            relatedProducts = self.driver.find_element(By.XPATH ,Locators_test.relatedproducts_xpath).text
            print(relatedProducts, "in pdp")
        except StaleElementReferenceException or ElementClickInterceptedException or TimeoutException or NoSuchElementException:
            print("No related products in pdp")


