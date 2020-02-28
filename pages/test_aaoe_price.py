from Smoketest.locatorfile.test_Locators import Locators_test
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
import time

class AAOEprice():
    def __init__(self,driver):
        self.driver =driver


    def test_aaoevalidation(self, driver):
        try:
            time.sleep(3)
            actions = ActionChains(self.driver)
            Category3 = self.driver.find_element(By.XPATH,Locators_test.category3_xpath)
            actions.move_to_element(Category3).perform()
            ebookcategory = self.driver.find_element(By.XPATH, Locators_test.ebookcat_xpath)
            actions.move_to_element(ebookcategory).click().perform()

            aaoeprice = self.driver.find_element(By.XPATH,Locators_test.aaoeprice_xpath).text
            print(aaoeprice)

        except StaleElementReferenceException or ElementClickInterceptedException or TimeoutException as ex:
            print(ex.message)



