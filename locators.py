from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM =(By.CSS_SELECTOR, "#register_form")
    

class ProductPageLocators():
    ADD = (By. CSS_SELECTOR, "#add_to_basket_form>.btn")
    NAME_PRODUCT=(By. CSS_SELECTOR, ".product_main>h1")
    NAME_ALERT = (By. CSS_SELECTOR, "div.alertinner strong")
    PRODUCT_ADDED =(By. CSS_SELECTOR, "#messages>.alert>div.alertinner")
    PRICE_BOOK = (By. CSS_SELECTOR, ".product_main>.price_color")
    PRICE_BASKET = (By. CSS_SELECTOR, ".alertinner>p>strong")
    SUCCESS_MESSAGE = (By. CSS_SELECTOR, "#messages>.alert>div.alertinner")
    BASKET_CONTENT = (By. CSS_SELECTOR, ".basket_summary")
    TEXT_BASKET = (By. CSS_SELECTOR, "#content_inner>p")
    

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_BASKET = (By.CSS_SELECTOR, ".btn-group>.btn")
    
