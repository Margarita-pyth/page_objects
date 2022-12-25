import pytest

from .pages.basket_page import BasketPage
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
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                              # открываем страницу
    page.should_be_add_to_cart_button()      # проверка что есть кнопка добавления в корзину
    page.adding_product_to_cart()            # добавим товар в корзину
    page.solve_quiz_and_get_code()           # решаем мат. задачку и вписываем ответ
    page.should_be_match_product_name_in_cart()  # проверяем идентичность названия продукта
    page.should_be_match_the_price_in_cart()     # проверяем идентичность цены
    #page.should_be_disappeared()

# pytest -v --tb=line --language=en test_product_page.py
# pytest -s test_product_page.py

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()
    page.adding_product_to_cart()            # добавим товар в корзину
    page.should_not_be_success_message()     # проверка, что сообщение о добавлении в корзину отсутствует
    
# pytest /page_objects/test_product_page.py::test_guest_cant_see_success_message_after_adding_product_to_basket

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()
    page.should_not_be_success_message()     # проверка, что сообщение о добавлении в корзину отсутствует

# pytest /page_objects/test_product_page.py::test_guest_cant_see_success_message

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()
    page.adding_product_to_cart()            # добавим товар в корзину
    page.should_be_disappeared()             # проверяем, что нет сообщения об успехе
    
# pytest /page_objects/test_product_page.py::test_message_disappeared_after_adding_product_to_basket

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link() # проверяем наличие ссылки на логин

# pytest /page_objects/test_product_page.py::test_guest_should_see_login_link_on_product_page

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

# pytest /page_objects/test_product_page.py::test_guest_can_go_to_login_page_from_product_page

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()           # переход в корзину
    page.should_not_be_message_about_adding_product_in_basket() # проверяем что нет сообщения о добавлении товара в корзину
    page.should_be_message_about_empty_basket() # проверяем что есть сообщение о пустой корзине
