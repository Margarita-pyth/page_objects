from selenium.webdriver.common.by import By


class BasketPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a")
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, ".content p")
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".row:nth-child(1) h2")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

#class MainPageLocators():
#    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_BUTTON = (By.ID, "login_form")
    REGISTRATION_BUTTON = (By.ID, "register_form")

class ProductPageLocators():
    CART_BUTTON = (By.CLASS_NAME, "add-to-basket")
    MESSAGE_ABOUT_ADING_TO_BASKET = (By.CLASS_NAME, "alertinner")
    MESSAGE_WITH_PRICE = (By.CSS_SELECTOR, '.alertinner p')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, '.alertinner strong') # div.alert:nth-child(1) strong
    PRICE_IN_THE_CART = (By.CSS_SELECTOR, '.product_main p') # .price_color:nth-child(2)
    PRICE_IN_MESSAGE = (By.CSS_SELECTOR, '.alertinner p strong') # div.alert:nth-child(3) strong
