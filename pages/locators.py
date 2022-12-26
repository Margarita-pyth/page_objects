from selenium.webdriver.common.by import By


class BasketPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a")
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, ".content p")
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".row:nth-child(1) h2")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    INPUT_EMAIL = (By.ID, "id_registration-email")
    INPUT_PASSWORD = (By.ID, "id_registration-password1")
    INPUT_REPEAT_PASSWORD = (By.ID,"id_registration-password2")
    REGISTRATION_SUBMIT = (By.NAME, "registration_submit")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    LOGIN_BUTTON = (By.ID, "login_form")
    REGISTRATION_BUTTON = (By.ID, "register_form")

class ProductPageLocators():
    CART_BUTTON = (By.CLASS_NAME, "add-to-basket")
    MESSAGE_ABOUT_ADING_TO_BASKET = (By.CLASS_NAME, "alertinner")
    MESSAGE_WITH_PRICE = (By.CSS_SELECTOR, '.alertinner p')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, '.alertinner strong')
    PRICE_IN_THE_CART = (By.CSS_SELECTOR, '.product_main p')
    PRICE_IN_MESSAGE = (By.CSS_SELECTOR, '.alertinner p strong')
