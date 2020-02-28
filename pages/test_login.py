from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from Smoketest.locatorfile.test_Locators import Locators_test
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC


import time

class Login():

    def __init__(self,driver):

        self.driver = driver
        #self.driver.implicitly_wait(30)
        #wait = WebDriverWait(self.driver,10)

    def login_user(self,driver):

        try:
            time.sleep(3)
            loginButton = self.driver.find_element(By.XPATH, Locators_test.loginlink_xpath)
            while loginButton.click() is True:
                break
            time.sleep(3)
            self.driver.execute_script("window.scrollBy(0,300);")
            time.sleep(3)

            emailfield = self.driver.find_element(By.ID, Locators_test.loginemail_id)
            emailfield.send_keys(Locators_test.login_email)

            passwordfield = self.driver.find_element(By.ID, Locators_test.loginpassword_id)
            passwordfield.send_keys(Locators_test.login_password)


            clicklogin = self.driver.find_element(By.ID, Locators_test.clicklogin_id)
            while clicklogin.click() is True:
                break

            time.sleep(5)
            userName = self.driver.find_element(By.XPATH, Locators_test.username_xpath)
            print("Logged in as", userName.text)

        except StaleElementReferenceException or ElementClickInterceptedException or TimeoutException as ex:
            print(ex.message)