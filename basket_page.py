from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class BasketPage(BasePage):
    def cheking_that_empty_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.BASKET_CONTENT), \
               "basket NOT empty"


    def checking_that_there_text(self):
        input1 = self.browser.find_element(*ProductPageLocators.TEXT_BASKET)
        assert input1 is not None, "TEXT  disappeared"
