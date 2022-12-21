import pytest

from .pages.base_page import BasePage
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


# pytest -v --tb=line --language=en test_product_page.py
# pytest -s test_product_page.py