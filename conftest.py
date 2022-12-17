import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome", # настройки для браузера
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en", # настройки языка
                     help="Choose language")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name") # считываем имя браузера с CMD
    user_language = request.config.getoption("language")  # считываем язык заданный в CMD
    browser = None
    if browser_name == "chrome": # сценарий для Chrome
        print("\nstart chrome browser for test..")
        options = Options() 
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox": # сценарий для Firefox
        print("\nstart firefox browser for test..")
        options_firefox = OptionsFirefox()
        options_firefox.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options=options_firefox)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
