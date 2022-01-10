from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def add_to_basket(self):
        input1 = self.browser.find_element(*ProductPageLocators.ADD)
        input1.click()
            
    def correct_name_product(self):
        input3 = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT)
        nameP = input3.text
        print(nameP)
        input4 = self.browser.find_element(*ProductPageLocators.NAME_ALERT)
        nameA = input4.text
        assert nameP == nameA ,"Not Correct name Product"

    def correct_added(self):
        input5 = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED)
        addedP = input5.text
        print(addedP)
        assert addedP is not None,"Product NOT added"

    def correct_price(self):
        input6 = self.browser.find_element(*ProductPageLocators.PRICE_BOOK)
        priceB = input6.text
        print("price book =", priceB)
        input7 = self.browser.find_element(*ProductPageLocators.PRICE_BASKET)
        priceBAS = input7.text
        print("price basket =", priceBAS)
        assert priceB == priceBAS, "Not Correct PRICE"
        
