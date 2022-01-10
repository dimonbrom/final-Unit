import pytest
from .pages.product_page import ProductPage

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
