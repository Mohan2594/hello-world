from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from Smoketest.locatorfile.test_Locators import Locators_test
from selenium.webdriver.common.by import By
import time


class MediaType():

    def __init__(self, driver):

        self.driver = driver

    def test_media(self, driver):

        print("test")

        try:
            time.sleep(3)
            media_type = self.driver.find_element(By.XPATH,Locators_test.mediapath_xpath)
            media_type.click()

            try:
                time.sleep(3)
                booklets = self.driver.find_element(By.XPATH, Locators_test.booklets_xpath)
                booklets.click()
                time.sleep(3)
                self.driver.back()
                time.sleep(3)

                ebook = self.driver.find_element(By.XPATH, Locators_test.ebook_xpath)
                ebook.click()
                time.sleep(3)
            except Exception:
                print("Could not find media type elements")
        except StaleElementReferenceException or ElementClickInterceptedException or TimeoutException as ex:
            print(ex.message)
