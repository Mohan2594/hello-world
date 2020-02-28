from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from Smoketest.locatorfile.test_Locators import Locators_test
from selenium.webdriver.common.by import By
import time

class CartPage():

    def __init__(self, driver):
        self.driver = driver

    def cart_page(self,driver):

        try:
            time.sleep(3)
            mini_cart = self.driver.find_element(By.XPATH,Locators_test.minicart_xpath)
            while mini_cart.click() is True:
                break
            time.sleep(2)
            go_to_cart = self.driver.find_element(By.XPATH,Locators_test.gotocart_xpath)
            while go_to_cart.click() is True:
               break
            time.sleep(2)

            '''coupon_code = "C15INV"
            wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='coupon_code']"))).send_keys(coupon_code)
            wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='action apply primary']"))).click()
            time.sleep(2)
            driver.execute_script("window.scrollTo(0,300)")
            verifydiscount = wait.until(EC.text_to_be_present_in_element((By.XPATH,"//th/span[text()='Discount (C15INV)']","C15INV")))
            if verifydiscount is not verifydiscount:'''

            while self.driver.find_element(By.XPATH,Locators_test.checkout_xpath).click() is True:
                break
            print("Coupon code not applied")
            time.sleep(2)

            '''else:
            print(verifydiscount, "is applied")
            wait.until(EC.element_to_be_clickable((By.XPATH,"//button/span[contains(text(), 'Cancel')]"))).click()
            print("Coupon cancelled")
            time.sleep(2)'''

        except StaleElementReferenceException or ElementClickInterceptedException or TimeoutException or NoSuchElementException as ex:
            print(ex.message)