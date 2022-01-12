import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage

@pytest.mark.parametrize('direct', ["offer0","offer1","offer2","offer3","offer4","offer5","offer6",pytest.param("offer7", marks=pytest.mark.xfail),"offer8","offer9"])


def test_guest_can_add_product_to_basket(browser, direct):

    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={direct}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.correct_name_product()
    page.correct_added()
    page.correct_price()

@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()



def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_dissapear_of_success_message()

@pytest.mark.prosmotr
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.perehod
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    


@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/"
    page = BasketPage (browser, link)
    page.open()
    page.go_to_basket()
    page.cheking_that_empty_basket()
    page.checking_that_there_text()
    

