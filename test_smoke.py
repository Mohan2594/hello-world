import pytest
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from Smoketest import test_email
from selenium.webdriver.chrome.options import Options
#from Smoketest import test_email
#from Smoketest import test_Listingpage


homePage = "https://store.aao.org/"
s1 = ""
relatedProducts = ""
recentlyViewed = ""
addtoCartpopup = ""
pdp = ""
windows = []
minicart = ""
gotocart = ""
proceedtoCheckout = ""


@pytest.fixture(scope="session")
def test_setup():
    global driver
    global wait
    global actions
    #chome_options = Options()
    #chome_options.add_argument("--incognito")
    #driver = webdriver.Chrome(chome_options=chome_options)
    driver = webdriver.Chrome(executable_path="C:\\Users\\administrator1\\Downloads\\chromedriver_win32\\chromedriver.exe")
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()
    driver.get(homePage)
    driver.implicitly_wait(5)
    actions = ActionChains(driver)
    #test_guestuser
    yield
    test_email.post_action()





def test_guestUser(test_setup):
    try:
        driver.execute_script("window.scrollBy(0,300);")
        time.sleep(2)
        newProducts = driver.find_element_by_xpath("//a[contains(text(),'New Products')]")
        newProducts.click()
        mostpopular = driver.find_element_by_xpath("//a[contains(text(),'Most Popular Products')]")
        mostpopular.click()
        time.sleep(2)
        print(newProducts.text, mostpopular.text, "are clicked")

        driver.find_element_by_xpath("//a[@class='icon-media-type']").click()
        time.sleep(3)
        try:
            driver.find_element_by_xpath("//a[@title='Booklets']").click()
            time.sleep(3)
            driver.back()
            time.sleep(3)

            driver.find_element_by_xpath("//a[@title='eBook']").click()
            time.sleep(3)
        except NoSuchElementException:
            print("Could not find media type elements")
    except StaleElementReferenceException or ElementClickInterceptedException or TimeoutException as ex:
        print(ex.message)

#def test_Listingpage1():
    #test_Listingpage.test_ListingPage()
def test_ListingPage():
    try:
        Category1 = driver.find_element_by_xpath("//span[contains(text(),'Clinical Education')]")
        actions.move_to_element(Category1).perform()
        time.sleep(2)

        SubCategory1 = driver.find_element_by_xpath("//span[contains(text(),'BCSC® (Basic and Clinical Science Course)')]")
        actions.move_to_element(SubCategory1).click().perform()
        time.sleep(2)

        try:
            s1 = driver.find_element_by_xpath("(//span[@class='toolbar-number'])[1]").text
            print("BCSC ", s1)
        except NoSuchElementException:
            print(s1)
            time.sleep(2)

        driver.execute_script("window.scrollBy(0,100);")
        time.sleep(2)

        layerFilter1 = driver.find_element_by_xpath("//div[@class='filter-options-item']//li[4]//a[1]")
        layerFilter1.click()

        driver.execute_script("window.scrollBy(0,-120);")
        time.sleep(2)
        pdp1 = driver.find_element_by_xpath("//a[@class='product-item-link']")
        pdp1.click()

        try:
            relatedProducts = driver.find_element_by_xpath("(//strong[@role='heading'])[1]").text
            print(relatedProducts, "in pdp")
        except NoSuchElementException:
            print("No related products in pdp")
    except StaleElementReferenceException or ElementClickInterceptedException or TimeoutException as ex:
        print(ex.message)


def test_ListingPage2():
    try:
        time.sleep(3)
        actions2 = ActionChains(driver)
        # actions2.move_to_element(driver.find_element_by_xpath("(//a[@class='level-top ui-corner-all'])[2]")).perform()
        category2 = driver.find_element_by_xpath("(//span[text()='Patient Education'])[1]")
        actions2.move_to_element(category2).perform()
        time.sleep(2)

        subCategory2 = driver.find_element_by_xpath("//span[contains(text(),'Brochures')]")
        actions2.move_to_element(subCategory2).click().perform()
        time.sleep(2)

        try:
            s1 = driver.find_element_by_xpath("(//span[@class='toolbar-number'])[1]").text
            print("Brouchers ", s1)

        except NoSuchElementException:
            print(s1)

        pdp = driver.find_element_by_xpath("(//a[@class='product-item-link'])[1]")
        pdp.click()
        time.sleep(2)
        try:
            relatedProducts = driver.find_element_by_xpath("(//strong[@role='heading'])[1]").text
            print(relatedProducts, "in pdp")
        except NoSuchElementException:
            print("No related products in pdp")

        addtoCart = driver.find_element_by_xpath("//button[@id='product-addtocart-button']")
        addtoCart.click()
        time.sleep(2)

        driver.find_element_by_xpath("//aside[contains(@class,'_show')]//footer[contains(@class,'modal-footer')]//button[1]/span").click()

    except StaleElementReferenceException or ElementClickInterceptedException or TimeoutException as ex:
        print(ex.message)


def test_ListingPage3():
    try:
        time.sleep(3)
        actions3 = ActionChains(driver)
        Category3 = driver.find_element_by_xpath("(//span[contains(text(),'Practice Management')])[1]")
        actions3.move_to_element(Category3).perform()
        SubCategory3 = driver.find_element_by_xpath("(//span[contains(text(),'AAOE: Coding & Reimbursement')])[1]")
        SubCategory3.click()
        time.sleep(2)
        try:
            s1 = driver.find_element_by_xpath("(//span[@class='toolbar-number'])[1]").text
            print("AAOE Coding & Reimb.", s1)
        except NoSuchElementException:
            print(s1)

        driver.find_element_by_xpath("(//a[@class='product-item-link'])[1]").click()
        time.sleep(2)

    except StaleElementReferenceException or ElementClickInterceptedException or TimeoutException as ex:
        print(ex.message)


def test_ListingPage4():
    try:
        actions4 = ActionChains(driver)
        Category4 = driver.find_element_by_xpath("(//span[contains(text(),'CME')])[1]")
        actions4.move_to_element(Category4).click().perform()
        time.sleep(2)

        try:
            s1 = driver.find_element_by_xpath("(//span[@class='toolbar-number'])[1]").text
            print("CME", s1)

        except NoSuchElementException:
            print(s1)
            time.sleep(2)

        addtocart = driver.find_element_by_xpath("(//button/span[text()='Add to Cart'])[2]")
        driver.execute_script("arguments[0].scrollIntoView(true);", addtocart)
        addtocart.click()
        time.sleep(2)
        driver.find_element_by_xpath("//aside/div//a[contains(text(),'create an account')]").click()
        time.sleep(2)
        verifyPage = driver.title

        if verifyPage is verifyPage:
            driver.back()
            print(verifyPage, "is the createaccount page")
        else:
            print("Create an account link failed")

    except StaleElementReferenceException or ElementClickInterceptedException or TimeoutException as ex:
        print(ex.message)


def test_cartPage():
    try:
        time.sleep(2)
        minicart = driver.find_element_by_xpath("//header//a[@class='action showcart']")
        minicart.click()
        time.sleep(2)
        gotocart = driver.find_element_by_xpath("//span[contains(text(),'Go To Shopping Cart')]")
        gotocart.click()
        time.sleep(2)

        try:
            couponcode = driver.find_element_by_xpath("//input[@id='coupon_code']").send_keys("C15INV")
            applycoupon = driver.find_element_by_xpath("//button[@class='action apply primary']").click()
            time.sleep(2)
            verifydiscount = driver.find_element_by_xpath("//th/span[text()='Discount (C15INV)']").text

            if verifydiscount is not None:
                print(verifydiscount, "is applied")
            else:
                print("Discount not applied")
                time.sleep(2)

            driver.find_element_by_xpath("//button/span[contains(text(), 'Cancel')]").click()
            print("Coupon cancelled")
            time.sleep(2)
        except NoSuchElementException:
            driver.find_element_by_xpath("//button/span[contains(text(), 'Checkout')]").click()
            print("Coupon code not applied")
            time.sleep(2)

    except StaleElementReferenceException or ElementClickInterceptedException or TimeoutException as ex:
        print(ex.message)


def test_guestCheckout():
    try:
        driver.find_element_by_xpath("//button[@class='button action continue primary']").click()
        guestEmail = "mohan25@gmail.com"
        firstName = "Test"
        lastName = "User"
        streetaddress = "123"
        city = "San Jose"
        state = "California"
        zipCode = "95110"

        driver.find_element_by_xpath("(//input[@name='username'])[2]").send_keys(guestEmail)
        time.sleep(2)
        logInbutton = driver.find_element_by_xpath("//button[@class='action login primary']")

        driver.find_element_by_xpath("//input[@name='firstname']").send_keys(firstName)
        driver.find_element_by_xpath("//input[@name='lastname']").send_keys(lastName)
        driver.find_element_by_xpath("//input[@name='street[0]']").send_keys(streetaddress)
        driver.find_element_by_xpath("//input[@name='city']").send_keys(city)

        select = Select(driver.find_element_by_xpath("//select[@name='region_id']"))
        select.select_by_visible_text(state)

        driver.find_element_by_xpath("//input[@name='postcode']").send_keys(zipCode)
        time.sleep(3)
        driver.find_element_by_xpath("//input[@name='ko_unique_1']").click()

        nextButton = driver.find_element_by_xpath(
            "//button[@class='button action continue primary']/span[text()='Next']")

        driver.execute_script("arguments[0].scrollIntoView(true);", nextButton)
        time.sleep(1)
        nextButton.click()

    except StaleElementReferenceException or ElementClickInterceptedException or TimeoutException as ex:
        print(ex.message)


def test_guestPayment():
    try:
        guestPrice = driver.find_element_by_xpath(
            "//td[@class='amount']//span[@class='price'][contains(text(),'$57.00')]").text
        if guestPrice is guestPrice:
            print("Guest price validated", guestPrice)
        else:
            print("Guest price failed")
            time.sleep(2)

        driver.get(homePage)
        time.sleep(3)

    except StaleElementReferenceException or ElementClickInterceptedException or TimeoutException as ex:
        print(ex.message)


def test_Login():
    try:
        loginLink = "//a[@id='login-link']"
        EmailId = "Vignesh.muthusamy@ziffity.com"
        Password = "password"
        emailElement = "dnn_ctr1179_Login_txtEmail"
        passwordElement = "dnn_ctr1179_Login_txtPassword"

        loginButton = wait.until(EC.visibility_of_element_located((By.XPATH, loginLink)))
        loginButton.click()

        driver.execute_script("window.scrollBy(0,300);")

        EmailField = wait.until(EC.presence_of_element_located((By.ID, emailElement)))
        EmailField.send_keys(EmailId)

        PasswordField = wait.until(EC.presence_of_element_located((By.ID, passwordElement)))
        PasswordField.send_keys(Password)

        ClickLogin = wait.until(EC.presence_of_element_located((By.ID, "dnn_ctr1179_Login_btnLogin")))
        ClickLogin.click()

        time.sleep(5)
        userName = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/sales/order/history/']/span")))
        print("Logged in as", userName.text)

    except StaleElementReferenceException or ElementClickInterceptedException or TimeoutException as ex:
        print(ex.message)


def test_MyAccount():
    try:

        time.sleep(5)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/sales/order/history/']/span"))).click()

        try:
            myOrders = driver.find_element_by_xpath("//th[contains(text(),'Order #')]").text
            print("Verified my", myOrders)
        except NoSuchElementException:
            print("My orders not displaying")
            time.sleep(2)

        actions3 = ActionChains(driver)
        myRenewals = driver.find_element_by_xpath("//main[@id='maincontent']//li[3]")
        actions3.move_to_element(myRenewals).click().perform()

        windows = []
        windows = driver.window_handles
        driver.switch_to.window(windows[1])
        driver.close()
        driver.switch_to.window(windows[0])
        print("Verified My Renewals open in new tab")

        actions5 = ActionChains(driver)
        myOnlinceproducts = driver.find_element_by_xpath("//main[@id='maincontent']//li[4]")
        actions5.move_to_element(myOnlinceproducts).click().perform()

        windows = []
        windows = driver.window_handles
        driver.switch_to.window(windows[1])
        driver.close()
        driver.switch_to.window(windows[0])
        print("Verified My Online products open in new tab")

        myWishlist = driver.find_element_by_xpath("//main[@id='maincontent']//li[5]")
        # actions.move_to_element(myWishlist).click().perform()
        myWishlist.click()

        try:
            driver.find_element_by_xpath("//strong[@class='product-item-name']").text
            print("Wishlist verified with products")
        except NoSuchElementException:
            print(driver.title, "verified without products")

        time.sleep(5)

    except StaleElementReferenceException or ElementClickInterceptedException or TimeoutException as ex:
        print(ex.message)


def test_Search():
    try:

        driver.find_element_by_xpath("//span[@class='search-inner']").click()
        driver.find_element_by_xpath("//input[@id='search']").send_keys("bcsc")
        time.sleep(2)
        selectSearchtext = driver.find_element_by_xpath("(//a[@class='title'])[1]")
        # actions.move_to_element(selectSearchtext).click().perform()
        selectSearchtext.click()
        driver.find_element_by_xpath("//div[@class='inc buttonTrig']").click()
        addtocart = driver.find_element_by_xpath("//button[@id='product-addtocart-button']")
        addtocart.click()
        time.sleep(5)
        driver.find_element_by_xpath("//footer[@class='modal-footer']//button[1]").click()
        time.sleep(2)

        try:
            recentlyViewed = driver.find_element_by_xpath("//strong[contains(text(),'Recently Viewed')]").text
            print(recentlyViewed, "is present")
        except NoSuchElementException:
            print(recentlyViewed, "is not present")

    except StaleElementReferenceException or ElementClickInterceptedException or TimeoutException as ex:
        print(ex.message)


def test_CartPriceRule():
    try:

        minicart = driver.find_element_by_xpath("//header//a[@class='action showcart']")
        minicart.click()
        time.sleep(2)
        gotocart = driver.find_element_by_xpath("//span[contains(text(),'Go To Shopping Cart')]")
        gotocart.click()
        time.sleep(2)

        try:
            verifyCartpricerule = driver.find_element_by_xpath("//span[@class='title']").text
            print("Verified", verifyCartpricerule)
        except NoSuchElementException:
            print("Cart price rule not applied")

        driver.find_element_by_xpath("//button/span[contains(text(), 'Checkout')]").click()
        time.sleep(2)

    except StaleElementReferenceException or ElementClickInterceptedException or TimeoutException as ex:
        print(ex.message)


def test_Shippingaddress():
    try:
        driver.find_element_by_xpath("(//button[@class='action action-select-shipping-item']/span[text()='Ship Here'])[1]").click()
        time.sleep(2)
        shippingMethods = driver.find_element_by_xpath("(//tr/td/input[@type='radio'])[1]")
        driver.execute_script("arguments[0].scrollIntoView(true);", shippingMethods)
        shippingMethods.click()
        time.sleep(2)
        nextButton = driver.find_element_by_xpath("//button[@class='button action continue primary']/span[text()='Next']")
        driver.execute_script("arguments[0].scrollIntoView(true);", nextButton)
        nextButton.click()
        time.sleep(2)

        productPrice = driver.find_element_by_xpath("(//span[@class='cart-price'])[1]").text
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
    except StaleElementReferenceException or ElementClickInterceptedException or TimeoutException as ex:
        print(ex.message)

'''def test_Clearcart():

     try:

        driver.get("https://store.aao.org/checkout/cart")

        driver.execute_script("window.scrollBy(0,200);")
        clearshoppingcart = wait.until(EC.presence_of_element_located(By.XPATH,"//button[@class='action clear']"))
        clearshoppingcart.click()
        time.sleep(2)

        # driver.find_element_by_xpath("//p/a[text()='here']").click()
        # time.sleep(2)
        wait.until(EC.presence_of_element_located(By.XPATH,"//a[@id='logout-link']").click()


     except NoSuchElementException or StaleElementReferenceException or ElementClickInterceptedException or TimeoutException as ex:
        print(ex.message)'''






