from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from Smoketest.locatorfile.test_Locators import Locators_test
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

class ListingPage2():

    def __init__(self,driver):
        self.driver = driver

    def listing2(self,driver):

        try:
            time.sleep(3)
            actions = ActionChains(self.driver)
            # actions.move_to_element(driver.find_element_by_xpath("(//a[@class='level-top ui-corner-all'])[2]")).perform()
            category2 = self.driver.find_element(By.XPATH,Locators_test.category2_xpath)
            actions.move_to_element(category2).perform()
            time.sleep(2)

            subCategory2 = self.driver.find_element(By.XPATH ,Locators_test.subcategory2_xpath)
            actions.move_to_element(subCategory2).click().perform()
            time.sleep(2)

            try:
                s1 = self.driver.find_element(By.XPATH ,Locators_test.s1_xpath).text
                print("Brouchers ",s1)

            except NoSuchElementException:
                print(s1)

            pdp = self.driver.find_element(By.XPATH ,Locators_test.pdp1_xpath)

            while pdp.click() is True:
                break
            time.sleep(2)

        except StaleElementReferenceException or ElementClickInterceptedException or TimeoutException as ex:
            print(ex.message)