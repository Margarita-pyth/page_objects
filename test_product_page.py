import pytest

from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", 
                                  marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_cart_button()
    page.adding_product_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_match_product_name_in_cart()
    page.should_be_match_the_price_in_cart()
# pytest -v --tb=line --language=en test_product_page.py
# pytest -s test_product_page.py

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.adding_product_to_cart()
    page.should_not_be_success_message()     # ????????????????, ?????? ?????????????????? ?? ???????????????????? ?? ?????????????? ??????????????????????
# pytest /page_objects/test_product_page.py::test_guest_cant_see_success_message_after_adding_product_to_basket

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
# pytest /page_objects/test_product_page.py::test_guest_cant_see_success_message

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.adding_product_to_cart()
    page.should_be_disappeared()
# pytest /page_objects/test_product_page.py::test_message_disappeared_after_adding_product_to_basket

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link() # ?????????????????? ?????????????? ???????????? ???? ??????????
# pytest /page_objects/test_product_page.py::test_guest_should_see_login_link_on_product_page

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
# pytest /page_objects/test_product_page.py::test_guest_can_go_to_login_page_from_product_page

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()                                    # ?????????????? ?? ??????????????
    page.should_not_be_message_about_adding_product_in_basket() # ?????????????????? ?????? ?????? ?????????????????? ?? ???????????????????? ???????????? ?? ??????????????
    page.should_be_message_about_empty_basket()                 # ?????????????????? ?????? ???????? ?????????????????? ?? ???????????? ??????????????

@pytest.mark.login_user
class TestUserAddToBasketFromProductPage():
    """???????????????? ?????????? ?????????? ?????? ?????????? ??????????????????????????."""
    @pytest.fixture(scope="function", autouse=True)
    def setup(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = LoginPage(browser, link) 
        page.open()
        page.go_to_login_page()                # ?????????????? ???????????????? ??????????????????????
        page.register_new_user()               # ?????????????????????? ????????????????????????
        page.should_be_authorized_user()       # ???????????????? ??????????????????????

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()     # ????????????????, ?????? ?????????????????? ?? ???????????????????? ?? ?????????????? ??????????????????????

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_to_cart_button()          # ???????????????? ?????? ???????? ???????????? ???????????????????? ?? ??????????????
        page.adding_product_to_cart()                # ?????????????? ?????????? ?? ??????????????
        page.should_be_match_product_name_in_cart()  # ?????????????????? ???????????????????????? ???????????????? ????????????????
        page.should_be_match_the_price_in_cart()     # ?????????????????? ???????????????????????? ????????
# pytest -v --tb=line --language=en -m login_user test_product_page.py
# pytest -v --tb=line --language=en -m need_review
