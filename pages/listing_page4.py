from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from Smoketest.locatorfile.test_Locators import Locators_test
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class ListingPage4():

    def __init__(self, driver):
        self.driver = driver

    def listing_page_4(self,driver):

        try:
            time.sleep(4)
            actions4 = ActionChains(self.driver)
            Category4 = self.driver.find_element(By.XPATH ,Locators_test.category4_xpath)
            actions4.move_to_element(Category4).click().perform()

            try:
                s1 = self.driver.find_element(By.XPATH ,Locators_test.s1_xpath).text
                print("CME", s1)

            except NoSuchElementException:
                print(s1)

            addtocart = self.driver.find_element(By.XPATH ,Locators_test.addtocart1_xpath)
            #driver.execute_script("arguments[0].scrollIntoView(true);", addtocart)
            while addtocart.click() is True:
                break
            time.sleep(2)

        except StaleElementReferenceException or ElementClickInterceptedException or TimeoutException as ex:
            print(ex.message)