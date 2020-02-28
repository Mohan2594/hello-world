from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from Smoketest.locatorfile.test_Locators import Locators_test
from selenium.webdriver.common.by import By
import time

class Shippingaddress():

    def __init__(self,driver):
        self.driver = driver



    def test_shipping(self,driver):
        try:
            time.sleep(3)
            shiphere = self.driver.find_element(By.XPATH,Locators_test.shiphere_xpath)
            shiphere.click()
            time.sleep(2)
            shippingMethods = self.driver.find_element(By.XPATH,Locators_test.shippingradio_xpath)
            driver.execute_script("arguments[0].scrollIntoView(true);", shippingMethods)
            while shippingMethods.click() is True:
                break
            time.sleep(2)
            nextButton = self.driver.find_element(By.XPATH,Locators_test.shippingnext_xpath)
            driver.execute_script("arguments[0].scrollIntoView(true);", nextButton)
            while nextButton.click() is True:
                break
            time.sleep(2)

            productPrice = self.driver.find_element(By.XPATH,Locators_test.memberprice_xpath).text

            if productPrice is productPrice:
                print(productPrice)
            else:
                print("product price is not member price")

            #minicart = driver.find_element_by_xpath("//header//a[@class='action showcart']")
            #minicart.click()

            #time.sleep(2)
            #gotocart = ("//span[contains(text(),'Go To Shopping Cart')]")
            #gotocart.click()
            #time.sleep(2)
        except StaleElementReferenceException or ElementClickInterceptedException or TimeoutException or NoSuchElementException as ex:
            print(ex.message)