import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from unittestpackage.test_guestuser_case import GuestUser


class TestCaseBrowser(unittest.TestCase):

    #@classmethod
    def unittestsmoke(self):
        homePage = "https://store.aao.org/"
        driver =webdriver.Chrome(executable_path="C:\\Users\\administrator1\\Downloads\\chromedriver_win32\\chromedriver.exe")
        wait = WebDriverWait(driver, 10)
        driver.maximize_window()
        driver.get(homePage)
        driver.implicitly_wait(10)
        actions = ActionChains(driver)

        GU =GuestUser(driver)
        GU.guestflow()


