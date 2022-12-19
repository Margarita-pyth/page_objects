from .pages.login_page import LoginPage
from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.should_be_login_link()      # проверка из MainPage
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина (MainPage)
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page() # все три проверки из login_page.py

# pytest -v --tb=line --language=en test_main_page.py
