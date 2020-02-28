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
from Smoketest.locatorfile.test_Locators import Locators_test

s1 = ""
relatedProducts = ""
recentlyViewed = ""
addtoCartpopup = ""
pdp = ""
windows = []
minicart = ""
gotocart = ""
proceedtoCheckout = ""


@pytest.fixture(scope="module")
def test_setup():
    global driver
    global wait
    global actions
    driver = webdriver.Chrome(executable_path=Locators_test.browser_path)
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.get(Locators_test.homePage)
    driver.implicitly_wait(5)
    actions = ActionChains(driver)
    yield
    driver.quit()
    print("test complete")



def test_guest_user(test_setup):

    from Smoketest.pages.guest_home_page import GuestHome

    gh = GuestHome(driver)
    gh.test_guest((Locators_test.newProducts_xpath,Locators_test.mostpopular_xpath))

def test_media_type():

    from Smoketest.pages.home_media_type import MediaType

    mt = MediaType(driver)
    mt.test_media((Locators_test.mediapath_xpath,Locators_test.booklets_xpath))



def test_listing_page():

    from Smoketest.pages.listing_page import ListingPage

    lp = ListingPage(driver)
    lp.listing_page((Locators_test.category1_xpath,Locators_test.subcategory1_xpath,Locators_test.s1_xpath,Locators_test.layerfilter_xpath,Locators_test.pdp_xpath))

def test_releated_products():

    from Smoketest.pages.related_products import RelatedProducts

    rp = RelatedProducts(driver)
    rp.verify_related_products(Locators_test.relatedproducts_xpath)

def test_listing_page_2():

    from Smoketest.pages.listing_page2 import ListingPage2

    lp2 = ListingPage2(driver)
    lp2.listing2((Locators_test.category2_xpath,Locators_test.subcategory2_xpath,Locators_test.s1_xpath,Locators_test.pdp1_xpath))

def test_listing2_add_to_cart():

    from Smoketest.pages.category_add_to_cart import AddToCart

    ac = AddToCart(driver)
    ac.add_to_cart((Locators_test.addtocart_xpath,Locators_test.postaddtocart_xpath))

def test_listing3_page():

    from Smoketest.pages.listing_page3 import ListingPage3

    lp3 = ListingPage3(driver)
    lp3.listing_page_3((Locators_test.category3_xpath,Locators_test.subcategory3_xpath,Locators_test.s1_xpath,Locators_test.pdp1_xpath))

def test_price():
    from Smoketest.pages.test_aaoe_price import AAOEprice
    ap = AAOEprice(driver)
    ap.test_aaoevalidation((Locators_test.category3_xpath,Locators_test.ebookcat_xpath,Locators_test.aaoeprice_xpath))

def test_listing4_page():

    from Smoketest.pages.listing_page4 import ListingPage4

    lp4 = ListingPage4(driver)
    lp4.listing_page_4((Locators_test.category4_xpath,Locators_test.s1_xpath,Locators_test.addtocart1_xpath))

def test_create_account():

    from Smoketest.pages.create_account import CreateAccount

    ca = CreateAccount(driver)
    ca.verify_create_account(Locators_test.createaccount_xpath)

def test_cart_page():

    from Smoketest.pages.cart_page import CartPage

    cp = CartPage(driver)
    cp.cart_page((Locators_test.minicart_xpath,Locators_test.gotocart_xpath,Locators_test.checkout_xpath))



def test_guestCheckout():
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH,Locators_test.guestlogin_xpath))).click()

        wait.until(EC.visibility_of_element_located((By.XPATH,Locators_test.guestemail_xpath))).send_keys(Locators_test.guest_email)
        time.sleep(2)
        

        wait.until(EC.visibility_of_element_located((By.XPATH,Locators_test.guestfirst_name_xpath))).send_keys(Locators_test.guestfirst_name)
        wait.until(EC.visibility_of_element_located((By.XPATH,Locators_test.guestlast_name_xpath))).send_keys(Locators_test.guestlast_name)
        wait.until(EC.visibility_of_element_located((By.XPATH,Locators_test.address_1_xpath))).send_keys(Locators_test.address_1)
        wait.until(EC.visibility_of_element_located((By.XPATH,Locators_test.city_guest_xpath))).send_keys(Locators_test.city_guest)

        select = Select(driver.find_element_by_xpath(Locators_test.state_guest_xpath))
        select.select_by_visible_text(Locators_test.state_guest)

        wait.until(EC.visibility_of_element_located((By.XPATH,Locators_test.zip_guest_xpath))).send_keys(Locators_test.zip_guest)
        time.sleep(3)
        while wait.until(EC.element_to_be_clickable((By.XPATH,Locators_test.guest_shipping_xpath))).click() is True:
            break

        nextButton = wait.until(EC.element_to_be_clickable((By.XPATH,Locators_test.shippingnext_xpath)))

        driver.execute_script("arguments[0].scrollIntoView(true);", nextButton)
        time.sleep(1)
        while nextButton.click() is True:
            break

    except StaleElementReferenceException or ElementClickInterceptedException or TimeoutException as ex:
        print(ex.message)


def test_guest_payment():

    from Smoketest.pages.guest_payment import GuestPayment

    gp = GuestPayment(driver)
    gp.guest_payment((Locators_test.guest_pricing_xpath,Locators_test.homePage))




def test_login():

    from Smoketest.pages.test_login import Login

    lo = Login(driver)
    lo.login_user((Locators_test.loginlink_xpath, Locators_test.loginemail_id, Locators_test.login_email, Locators_test.loginpassword_id, Locators_test.login_password, Locators_test.clicklogin_id, Locators_test.username_xpath))




def test_my_account():

    from Smoketest.pages.test_my_orders import MyAccount

    mo = MyAccount(driver)
    mo.test_user_account((Locators_test.myaccount_xpath,Locators_test.myorders_xpath))

def test_my_renewals():

    from Smoketest.pages.test_my_renewals import MyRenewals

    mr = MyRenewals(driver)
    mr.test_myrenewals(Locators_test.myrenewals_xpath)

def test_my_online():

    from Smoketest.pages.test_my_onlineproducts import MyOnlineproducts

    mo = MyOnlineproducts(driver)
    mo.test_myonlineproducts(Locators_test.myonlineproducts_xpath)

def test_my_wishlist():

    from Smoketest.pages.test_my_wishlist import MyWishlist

    mw = MyWishlist(driver)
    mw.test_wishlist((Locators_test.wishlist_xpath,Locators_test.wishlist_products))

def test_search():

    from Smoketest.pages.test_search_product import Search

    sp = Search(driver)
    sp.test_Search((Locators_test.search_xpath,Locators_test.search_input_xpath,Locators_test.search_term,Locators_test.search_results_xpath,Locators_test.qtyincrement_xpath))

def test_searc_addto():

    from Smoketest.pages.search_addto_cart import SearchAdd

    sa = SearchAdd(driver)
    sa.test_search_tocart((Locators_test.addtocart_xpath,Locators_test.search_page_xpath))

def test_recently_viewed():

    from Smoketest.pages.recently_viewed import RecentlyViewed

    rv = RecentlyViewed(driver)
    rv.test_recently(Locators_test.recentlyviewed_xpath)

def test_cart_price_rule():

    from Smoketest.pages.test_discountrule import DiscountValidation

    cp = DiscountValidation(driver)
    cp.test_discount_validation((Locators_test.minicart_xpath,Locators_test.gotocart_xpath,Locators_test.cartpricerule_xpath,Locators_test.checkout_xpath))

def test_loggedin_shipping():

    from Smoketest.pages.logged_in_shipping import LoggedinShipping

    ls = LoggedinShipping(driver)
    ls.test_loggedinship((Locators_test.shiphere_xpath,Locators_test.shippingradio_xpath,Locators_test.shippingnext_xpath))

def test_member_price():

    from Smoketest.pages.member_price_verify import MemberPrice

    mp = MemberPrice(driver)
    mp.member_price(Locators_test.memberprice_xpath)

def test_clearcart():

    from Smoketest.pages.test_clearcart import ClearCart

    cc = ClearCart(driver)
    cc.test_clear_cart((Locators_test.minicart_xpath,Locators_test.gotocart_xpath,Locators_test.clearcart_xpath))

    time.sleep(5)


def test_Logout():

    from Smoketest.pages.test_logout import Logout

    lo = Logout(driver)
    lo.test_Signout(Locators_test.logout_xpath)


'''def test_listingpage1():
    try:
        Category1 = wait.until(EC.visibility_of_element_located((By.XPATH,Locators_test.category1_xpath)))
        actions.move_to_element(Category1).perform()
        time.sleep(2)

        SubCategory1 = wait.until(EC.presence_of_element_located((By.XPATH,Locators_test.subcategory1_xpath)))
        actions.move_to_element(SubCategory1).click().perform()
        time.sleep(2)
        s1 = wait.until(EC.visibility_of_element_located((By.XPATH,Locators_test.s1_xpath))).text
        print("BCSC ", s1)

        driver.execute_script("window.scrollBy(0,100);")
        time.sleep(2)

        layerFilter1 = wait.until(EC.element_to_be_clickable((By.XPATH,Locators_test.layerfilter_xpath)))
        while layerFilter1.click() is True:
            break

        driver.execute_script("window.scrollBy(0,-120);")
        time.sleep(2)
        pdp1 = wait.until(EC.element_to_be_clickable((By.XPATH,Locators_test.pdp_xpath)))
        while pdp1.click() is True:
            break

        try:
            relatedProducts = wait.until(EC.visibility_of_element_located((By.XPATH,Locators_test.relatedproducts_xpath))).text
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
        category2 = wait.until(EC.element_to_be_clickable((By.XPATH,Locators_test.category2_xpath)))
        actions2.move_to_element(category2).perform()
        time.sleep(2)

        subCategory2 = wait.until(EC.visibility_of_element_located((By.XPATH,Locators_test.subcategory2_xpath)))
        actions2.move_to_element(subCategory2).click().perform()
        time.sleep(2)

        try:
            s1 = wait.until(EC.visibility_of_element_located((By.XPATH,Locators_test.s1_xpath))).text
            print("Brouchers ", s1)

        except NoSuchElementException:
            print(s1)

        pdp = wait.until(EC.element_to_be_clickable((By.XPATH,Locators_test.pdp1_xpath)))
        while pdp.click() is True:
            break
        time.sleep(2)
        try:
            relatedProducts = wait.until(EC.visibility_of_element_located((By.XPATH,Locators_test.relatedproducts_xpath))).text
            print(relatedProducts, "in pdp")
        except NoSuchElementException:
            print("No related products in pdp")

        addtoCart = wait.until(EC.element_to_be_clickable((By.XPATH,Locators_test.addtocart_xpath)))
        while addtoCart.click() is True:
            break
        time.sleep(2)

        wait.until(EC.element_to_be_clickable((By.XPATH,Locators_test.postaddtocart_xpath))).click()

    except StaleElementReferenceException or ElementClickInterceptedException or TimeoutException as ex:
        print(ex.message)


def test_ListingPage3():
        try:
            actions3 = ActionChains(driver)
            Category3 = wait.until(EC.element_to_be_clickable((By.XPATH,Locators_test.category3_xpath)))
            actions3.move_to_element(Category3).perform()
            SubCategory3 = wait.until(EC.element_to_be_clickable((By.XPATH,Locators_test.subcategory3_xpath)))
            while SubCategory3.click() is True:
                break
            try:
                s1 = wait.until(EC.visibility_of_element_located((By.XPATH,Locators_test.s1_xpath))).text
                print("AAOE Coding & Reimb.", s1)
            except NoSuchElementException:
                print(s1)

            while wait.until(EC.element_to_be_clickable((By.XPATH,Locators_test.pdp1_xpath))).click() is True:
                break

        except StaleElementReferenceException or ElementClickInterceptedException or TimeoutException as ex:
            print(ex.message)
            
def test_ListingPage4():
    try:
        actions4 = ActionChains(driver)
        Category4 = wait.until(EC.element_to_be_clickable((By.XPATH,Locators_test.category4_xpath)))
        actions4.move_to_element(Category4).click().perform()

        try:
            s1 = wait.until(EC.visibility_of_element_located((By.XPATH,Locators_test.s1_xpath))).text
            print("CME", s1)

        except NoSuchElementException:
            print(s1)

        addtocart = wait.until(EC.element_to_be_clickable((By.XPATH,Locators_test.addtocart1_xpath)))
        driver.execute_script("arguments[0].scrollIntoView(true);", addtocart)
        while addtocart.click() is True:
            break
        time.sleep(2)
        while wait.until(EC.element_to_be_clickable((By.XPATH,Locators_test.createaccount_xpath))).click() is True:
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
        minicart = wait.until(EC.element_to_be_clickable((By.XPATH,Locators_test.minicart_xpath)))
        while minicart.click() is True:
            break
        time.sleep(2)
        gotocart = wait.until(EC.element_to_be_clickable((By.XPATH,Locators_test.gotocart_xpath)))
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
        while wait.until(EC.element_to_be_clickable((By.XPATH,Locators_test.checkout_xpath))).click() is True:
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
        
def test_guestPayment():
    try:
        guestPrice = wait.until(EC.visibility_of_element_located((By.XPATH,Locators_test.guest_pricing_xpath))).text
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
        loginButton = wait.until(EC.element_to_be_clickable((By.XPATH, Locators_test.loginlink_xpath)))
        while loginButton.click() is True:
            break
        time.sleep(3)
        driver.execute_script("window.scrollBy(0,300);")

        EmailField = wait.until(EC.visibility_of_element_located((By.ID, Locators_test.loginemail_id)))
        EmailField.send_keys(Locators_test.login_email)
        PasswordField = wait.until(EC.visibility_of_element_located((By.ID, Locators_test.loginpassword_id)))
        PasswordField.send_keys(Locators_test.login_password)

        ClickLogin = wait.until(EC.element_to_be_clickable((By.ID, Locators_test.clicklogin_id)))
        while ClickLogin.click() is True:
            break

        time.sleep(5)

        userName = wait.until(EC.visibility_of_element_located((By.ID, Locators_test.username_xpath)))
        print("Logged in as", userName.text)



    except StaleElementReferenceException or ElementClickInterceptedException or TimeoutException as ex:
        print(ex.message)    

def test_myaccount():
    try:
        time.sleep(3)
        myacccountbutton = wait.until(EC.element_to_be_clickable((By.XPATH, Locators_test.myaccount_xpath)))
        myacccountbutton.click()
        time.sleep(3)

        try:
            myOrders = wait.until(EC.element_to_be_clickable((By.XPATH, Locators_test.myorders_xpath))).text
            time.sleep(3)
            print("Verified my", myOrders)
            time.sleep(3)
        except NoSuchElementException:
            print("My orders not displaying")
            time.sleep(2)

        actions3 = ActionChains(driver)
        myRenewals = wait.until(EC.element_to_be_clickable((By.XPATH, Locators_test.myrenewals_xpath)))
        actions3.move_to_element(myRenewals).click().perform()
        time.sleep(3)

        windows = driver.window_handles
        driver.switch_to.window(windows[1])
        time.sleep(3)
        driver.close()
        driver.switch_to.window(windows[0])
        print("Verified My Renewals open in new tab")

        actions = ActionChains(driver)
        myOnlinceproducts = wait.until(EC.element_to_be_clickable((By.XPATH, Locators_test.myonlineproducts_xpath)))
        actions.move_to_element(myOnlinceproducts).click().perform()
        time.sleep(3)

        windows = []
        windows = driver.window_handles
        driver.switch_to.window(windows[1])
        time.sleep(3)
        driver.close()
        time.sleep(3)
        driver.switch_to.window(windows[0])
        print("Verified My Online products open in new tab")

        myWishlist = wait.until(EC.element_to_be_clickable((By.XPATH, Locators_test.wishlist_xpath)))
        # actions.move_to_element(myWishlist).click().perform()
        while myWishlist.click() is True:
            time.sleep(3)
            break

        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, Locators_test.wishlist_products))).text
            # print("Wishlist verified with products")
        except NoSuchElementException:
            print(driver.title, "verified without products")

        time.sleep(5)

    except StaleElementReferenceException or ElementClickInterceptedException or TimeoutException as ex:
        print(ex.message)
        
        
def test_Search():
    try:

        while wait.until(EC.element_to_be_clickable((By.XPATH, Locators_test.search_xpath))).click() is True:
            break
        wait.until(EC.presence_of_element_located((By.XPATH, Locators_test.search_input_xpath))).send_keys(Locators_test.search_term)
        time.sleep(2)
        selectSearchtext = wait.until(EC.element_to_be_clickable((By.XPATH, Locators_test.search_results_xpath)))
        # actions.move_to_element(selectSearchtext).click().perform()
        selectSearchtext.click()

        while wait.until(EC.element_to_be_clickable((By.XPATH, Locators_test.qtyincrement_xpath))).click() is True:
            break
        addtocart = wait.until(EC.element_to_be_clickable((By.XPATH, Locators_test.addtocart_xpath)))
        while addtocart.click() is True:
            break
        time.sleep(5)
        wait.until(EC.element_to_be_clickable((By.XPATH, Locators_test.search_page_xpath))).click()
        time.sleep(2)

        try:
            recentlyViewed = wait.until(EC.presence_of_element_located((By.XPATH, Locators_test.recentlyviewed_xpath))).text
            print(recentlyViewed, "is present")
        except NoSuchElementException:
            print(recentlyViewed, "is not present")

    except StaleElementReferenceException or ElementClickInterceptedException or TimeoutException as ex:
        print(ex.message)



def test_CartPriceRule():
    try:

        minicart = wait.until(EC.element_to_be_clickable((By.XPATH, Locators_test.minicart_xpath)))
        while minicart.click() is True:
            break
        time.sleep(5)
        gotocart = wait.until(EC.element_to_be_clickable((By.XPATH, Locators_test.gotocart_xpath)))

        while gotocart.click() is True:
            break

        time.sleep(5)

        try:
            verifyCartpricerule = wait.until(EC.visibility_of_element_located((By.XPATH, Locators_test.cartpricerule_xpath))).text
            print("Verified", verifyCartpricerule)
        except NoSuchElementException:
            print("Cart price rule not applied")

        wait.until(EC.element_to_be_clickable((By.XPATH, Locators_test.checkout_xpath))).click()
        time.sleep(5)

    except StaleElementReferenceException or ElementClickInterceptedException or TimeoutException or NoSuchElementException as ex:
        print(ex.message)


def test_loggedinship():

    try:

        shiphere = wait.until(EC.element_to_be_clickable((By.XPATH, Locators_test.shiphere_xpath)))
        shiphere.click()
        time.sleep(2)
        shippingMethods = wait.until(EC.element_to_be_clickable((By.XPATH, Locators_test.shippingradio_xpath)))
        driver.execute_script("arguments[0].scrollIntoView(true);", shippingMethods)

        while shippingMethods.click() is True:
            break

        time.sleep(2)
        nextButton = wait.until(EC.element_to_be_clickable((By.XPATH, Locators_test.shippingnext_xpath)))
        driver.execute_script("arguments[0].scrollIntoView(true);", nextButton)

        while nextButton.click() is True:
            break

        time.sleep(2)

        productPrice = wait.until(EC.visibility_of_element_located((By.XPATH, Locators_test.memberprice_xpath))).text

        if productPrice is productPrice:
            print(productPrice)
        else:
            print("product price is not member price")

    except StaleElementReferenceException or ElementClickInterceptedException or TimeoutException or NoSuchElementException as ex:
        print(ex.message)'''

