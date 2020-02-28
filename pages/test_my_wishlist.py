from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from Smoketest.locatorfile.test_Locators import Locators_test
from selenium.webdriver.common.by import By
import time

class MyWishlist():

    def __init__(self,driver):
        self.driver = driver

    def test_wishlist(self,driver):


        try:
            time.sleep(3)
            myWishlist = self.driver.find_element(By.XPATH, Locators_test.wishlist_xpath)
            # actions.move_to_element(myWishlist).click().perform()
            while myWishlist.click() is True:
                break

            try:
                self.driver.find_element(By.XPATH,Locators_test.wishlist_products).text
                #print("Wishlist verified with products")
            except NoSuchElementException:
                print(driver.title, "verified without products")

            time.sleep(5)

        except StaleElementReferenceException or ElementClickInterceptedException or TimeoutException as ex:
            print(ex.message)
