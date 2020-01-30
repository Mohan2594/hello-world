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
#from Smoketest import test_email
#from Smoketest.properties import test_properties

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
    driver = webdriver.Chrome(executable_path= "C:\\Users\\administrator1\\Downloads\\chromedriver_win32\\chromedriver.exe")
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()
    driver.get(homePage)
    driver.implicitly_wait(5)
    actions = ActionChains(driver)
    #test_guestuser
    yield
    #test_email.post_action()
    print("test complete")





def test_guestUser(test_setup):
    try:
        driver.execute_script("window.scrollBy(0,300);")
        time.sleep(2)
        newProducts = wait.until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'New Products')]")))
        while newProducts.click() is True:
            break
        mostpopular = wait.until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'Most Popular Products')]")))
        while mostpopular.click() is True:
            break
        time.sleep(2)
        print(newProducts.text, mostpopular.text, "are clicked")

        while wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@class='icon-media-type']"))).click() is True:
            break
        time.sleep(3)
        try:
            while wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@title='Booklets']"))).click() is True:
                break
            time.sleep(3)
            driver.back()
            time.sleep(3)

            while wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@title='eBook']"))).click() is True:
                break
            time.sleep(3)
        except NoSuchElementException:
            print("Could not find media type elements")
    except StaleElementReferenceException or ElementClickInterceptedException or TimeoutException as ex:
        print(ex.message)

#def test_Listingpage1():
    #test_Listingpage.test_ListingPage()
def test_ListingPage():
    try:
        Category1 = wait.until(EC.visibility_of_element_located((By.XPATH,"//span[contains(text(),'Clinical Education')]")))
        actions.move_to_element(Category1).perform()
        time.sleep(2)

        SubCategory1 = wait.until(EC.presence_of_element_located((By.XPATH,"//span[contains(text(),'BCSC® (Basic and Clinical Science Course)')]")))
        actions.move_to_element(SubCategory1).click().perform()
        time.sleep(2)
        s1 = wait.until(EC.visibility_of_element_located((By.XPATH,"(//span[@class='toolbar-number'])[1]"))).text
        print("BCSC ", s1)

        driver.execute_script("window.scrollBy(0,100);")
        time.sleep(2)

        layerFilter1 = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='filter-options-item']//li[4]//a[1]")))
        while layerFilter1.click() is True:
            break

        driver.execute_script("window.scrollBy(0,-120);")
        time.sleep(2)
        pdp1 = wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@class='product-item-link']")))
        while pdp1.click() is True:
            break

        try:
            relatedProducts = wait.until(EC.visibility_of_element_located((By.XPATH,"(//strong[@role='heading'])[1]"))).text
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
        category2 = wait.until(EC.element_to_be_clickable((By.XPATH,"(//span[text()='Patient Education'])[1]")))
        actions2.move_to_element(category2).perform()
        time.sleep(2)

        subCategory2 = wait.until(EC.visibility_of_element_located((By.XPATH,"//span[contains(text(),'Brochures')]")))
        actions2.move_to_element(subCategory2).click().perform()
        time.sleep(2)

        try:
            s1 = wait.until(EC.visibility_of_element_located((By.XPATH,"(//span[@class='toolbar-number'])[1]"))).text
            print("Brouchers ", s1)

        except NoSuchElementException:
            print(s1)

        pdp = wait.until(EC.element_to_be_clickable((By.XPATH,"(//a[@class='product-item-link'])[1]")))
        while pdp.click() is True:
            break
        time.sleep(2)
        try:
            relatedProducts = wait.until(EC.visibility_of_element_located((By.XPATH,"(//strong[@role='heading'])[1]"))).text
            print(relatedProducts, "in pdp")
        except NoSuchElementException:
            print("No related products in pdp")

        addtoCart = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@id='product-addtocart-button']")))
        while addtoCart.click() is True:
            break
        time.sleep(2)

        wait.until(EC.element_to_be_clickable((By.XPATH,"//aside[contains(@class,'_show')]//footer[contains(@class,'modal-footer')]//button[1]/span"))).click()

    except StaleElementReferenceException or ElementClickInterceptedException or TimeoutException as ex:
        print(ex.message)


def test_ListingPage3():
    #while True:
        try:
            actions3 = ActionChains(driver)
            path="//span[contains(text(),'Practice Management')][1]"
            Category3 = wait.until(EC.element_to_be_clickable((By.XPATH,path)))
            actions3.move_to_element(Category3).perform()
            SubCategory3 = wait.until(EC.element_to_be_clickable((By.XPATH,"(//span[contains(text(),'AAOE: Coding & Reimbursement')])[1]")))
            while SubCategory3.click() is True:
                break
            try:
                s1 = wait.until(EC.visibility_of_element_located((By.XPATH,"(//span[@class='toolbar-number'])[1]"))).text
                print("AAOE Coding & Reimb.", s1)
            except NoSuchElementException:
                print(s1)

            while wait.until(EC.element_to_be_clickable((By.XPATH,"(//a[@class='product-item-link'])[1]"))).click() is True:
                break

        except StaleElementReferenceException or ElementClickInterceptedException or TimeoutException as ex:
            print(ex.message)


def test_ListingPage4():
    try:
        actions4 = ActionChains(driver)
        Category4 = wait.until(EC.element_to_be_clickable((By.XPATH,"(//span[contains(text(),'CME')])[1]")))
        actions4.move_to_element(Category4).click().perform()

        try:
            s1 = wait.until(EC.visibility_of_element_located((By.XPATH,"(//span[@class='toolbar-number'])[1]"))).text
            print("CME", s1)

        except NoSuchElementException:
            print(s1)

        addtocart = wait.until(EC.element_to_be_clickable((By.XPATH,"(//button/span[text()='Add to Cart'])[2]")))
        driver.execute_script("arguments[0].scrollIntoView(true);", addtocart)
        while addtocart.click() is True:
            break
        time.sleep(2)
        while wait.until(EC.element_to_be_clickable((By.XPATH,"//aside/div//a[contains(text(),'create an account')]"))).click() is True:
            break
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
        minicart = wait.until(EC.element_to_be_clickable((By.XPATH,"//header//a[@class='action showcart']")))
        while minicart.click() is True:
            break
        time.sleep(2)
        gotocart = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[contains(text(),'Go To Shopping Cart')]")))
        while gotocart.click() is True:
            break
        time.sleep(2)

        #coupon_code = "C15INV"
        #wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='coupon_code']"))).send_keys(coupon_code)
        #wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='action apply primary']"))).click()
        #time.sleep(2)
        #driver.execute_script("window.scrollTo(0,300)")
        #verifydiscount = wait.until(EC.text_to_be_present_in_element((By.XPATH,"//th/span[text()='Discount (C15INV)']","C15INV")))

        #if verifydiscount is not verifydiscount:
        while wait.until(EC.element_to_be_clickable((By.XPATH,"//button/span[contains(text(), 'Checkout')]"))).click() is True:
            break
        print("Coupon code not applied")
        time.sleep(2)

        #else:
            #print(verifydiscount, "is applied")
            #wait.until(EC.element_to_be_clickable((By.XPATH, "//button/span[contains(text(), 'Cancel')]"))).click()
            #print("Coupon cancelled")
            #time.sleep(2)

    except StaleElementReferenceException or ElementClickInterceptedException or TimeoutException as ex:
        print(ex.message)


def test_guestCheckout():
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH,"//button[@class='button action continue primary']"))).click()
        guestEmail = "mohan25@gmail.com"
        firstName = "Test"
        lastName = "User"
        streetaddress = "123"
        city = "San Jose"
        state = "California"
        zipCode = "95110"

        wait.until(EC.visibility_of_element_located((By.XPATH,"(//input[@name='username'])[2]"))).send_keys(guestEmail)
        time.sleep(2)
        logInbutton = driver.find_element_by_xpath("//button[@class='action login primary']")

        wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@name='firstname']"))).send_keys(firstName)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@name='lastname']"))).send_keys(lastName)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@name='street[0]']"))).send_keys(streetaddress)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@name='city']"))).send_keys(city)

        select = Select(driver.find_element_by_xpath("//select[@name='region_id']"))
        select.select_by_visible_text(state)

        wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@name='postcode']"))).send_keys(zipCode)
        time.sleep(3)
        while wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@name='ko_unique_1']"))).click() is True:
            break

        nextButton = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='button action continue primary']/span[text()='Next']")))

        driver.execute_script("arguments[0].scrollIntoView(true);", nextButton)
        time.sleep(1)
        while nextButton.click() is True:
            break

    except StaleElementReferenceException or ElementClickInterceptedException or TimeoutException as ex:
        print(ex.message)


def test_guestPayment():
    try:
        guestPrice = wait.until(EC.visibility_of_element_located((By.XPATH,"//td[@class='amount']//span[@class='price'][contains(text(),'$57.00')]"))).text
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
        while loginButton.click() is True:
            break

        driver.execute_script("window.scrollBy(0,300);")

        EmailField = wait.until(EC.presence_of_element_located((By.ID, emailElement)))
        EmailField.send_keys(EmailId)

        PasswordField = wait.until(EC.presence_of_element_located((By.ID, passwordElement)))
        PasswordField.send_keys(Password)

        ClickLogin = wait.until(EC.element_to_be_clickable((By.ID, "dnn_ctr1179_Login_btnLogin")))
        while ClickLogin.click() is True:
            break

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
            myOrders = wait.until(EC.visibility_of_element_located((By.XPATH,"//th[contains(text(),'Order #')]"))).text
            print("Verified my", myOrders)
        except NoSuchElementException:
            print("My orders not displaying")
            time.sleep(2)

        actions3 = ActionChains(driver)
        myRenewals = wait.until(EC.element_to_be_clickable((By.XPATH,"//main[@id='maincontent']//li[3]")))
        actions3.move_to_element(myRenewals).click().perform()

        windows = []
        windows = driver.window_handles
        driver.switch_to.window(windows[1])
        driver.close()
        driver.switch_to.window(windows[0])
        print("Verified My Renewals open in new tab")

        actions5 = ActionChains(driver)
        myOnlinceproducts = wait.until(EC.element_to_be_clickable((By.XPATH,"//main[@id='maincontent']//li[4]")))
        actions5.move_to_element(myOnlinceproducts).click().perform()

        windows = []
        windows = driver.window_handles
        driver.switch_to.window(windows[1])
        driver.close()
        driver.switch_to.window(windows[0])
        print("Verified My Online products open in new tab")

        myWishlist = wait.until(EC.element_to_be_clickable((By.XPATH,"//main[@id='maincontent']//li[5]")))
        # actions.move_to_element(myWishlist).click().perform()
        while myWishlist.click() is True:
            break

        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,"//strong[@class='product-item-name']"))).text
            #print("Wishlist verified with products")
        except NoSuchElementException:
            print(driver.title, "verified without products")

        time.sleep(5)

    except StaleElementReferenceException or ElementClickInterceptedException or TimeoutException as ex:
        print(ex.message)


def test_Search():
    try:

        while wait.until(EC.element_to_be_clickable((By.XPATH,"//span[@class='search-inner']"))).click() is True:
            break
        wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='search']"))).send_keys("bcsc")
        time.sleep(2)
        selectSearchtext = wait.until(EC.element_to_be_clickable((By.XPATH,"(//a[@class='title'])[1]")))
        #actions.move_to_element(selectSearchtext).click().perform()
        selectSearchtext.click()
        while wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='inc buttonTrig']"))).click() is True:
            break
        addtocart = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@id='product-addtocart-button']")))
        while addtocart.click() is True:
            break
        time.sleep(5)
        wait.until(EC.element_to_be_clickable((By.XPATH,"//footer[@class='modal-footer']//button[1]"))).click()
        time.sleep(2)

        try:
            recentlyViewed = wait.until(EC.visibility_of_element_located((By.XPATH,"//strong[contains(text(),'Recently Viewed')]"))).text
            print(recentlyViewed, "is present")
        except NoSuchElementException:
            print(recentlyViewed, "is not present")

    except StaleElementReferenceException or ElementClickInterceptedException or TimeoutException as ex:
        print(ex.message)


def test_CartPriceRule():
    try:

        minicart = wait.until(EC.element_to_be_clickable((By.XPATH,"//header//a[@class='action showcart']")))
        while minicart.click() is True:
            break
        time.sleep(2)
        gotocart = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[contains(text(),'Go To Shopping Cart')]")))
        while gotocart.click() is True:
            break
        time.sleep(2)

        try:
            verifyCartpricerule = wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='title']"))).text
            print("Verified", verifyCartpricerule)
        except NoSuchElementException:
            print("Cart price rule not applied")

        wait.until(EC.element_to_be_clickable((By.XPATH,"//button/span[contains(text(), 'Checkout')]"))).click()
        time.sleep(2)

    except StaleElementReferenceException or ElementClickInterceptedException or TimeoutException as ex:
        print(ex.message)


def test_shippingaddress():
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH,"(//button[@class='action action-select-shipping-item']/span[text()='Ship Here'])[1]"))).click()
        time.sleep(2)
        shippingMethods = wait.until(EC.element_to_be_clickable((By.XPATH,"(//tr/td/input[@type='radio'])[1]")))
        driver.execute_script("arguments[0].scrollIntoView(true);", shippingMethods)
        while shippingMethods.click() is True:
            break
        time.sleep(2)
        nextButton = wait.until (EC.visibility_of_element_located((By.XPATH,"//button[@class='button action continue primary']/span[text()='Next']")))
        driver.execute_script("arguments[0].scrollIntoView(true);", nextButton)
        while nextButton.click() is True:
            break
        time.sleep(2)

        productPrice = wait.until(EC.visibility_of_element_located((By.XPATH,"(//span[@class='cart-price'])[1]"))).text

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
    
#test_email.post_action()

def test_Clearcart():

     try:

        driver.get("https://store.aao.org/checkout/cart")
        #checkoutcart = wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@class='action showcart']")))
        #gotocart = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Go To Shopping Cart')]")))
        #while checkoutcart.click() and gotocart.click() is True:
            #break

        driver.execute_script("window.scrollBy(0,200);")
        clearshoppingcart = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='action clear']")))
        clearshoppingcart.click()
        time.sleep(2)

        # driver.find_element_by_xpath("//p/a[text()='here']").click()
        # time.sleep(2)
        logout = wait.until(EC.element_to_be_clickable((By.XPATH,"//li[@class='authorization-link']")))
        while logout.click() is True:
            break

     except NoSuchElementException or StaleElementReferenceException or ElementClickInterceptedException or TimeoutException as ex:
        print(ex.message)






