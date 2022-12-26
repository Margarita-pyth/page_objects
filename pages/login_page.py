import faker

from .base_page import BasePage
from .locators import BasePageLocators, LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "There is no Login substring in the current url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login Form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_BUTTON), "Registration Form is not presented"

    def register_new_user(self):
        """Регистрация нового пользователя."""
        f = faker.Faker()
        random_email = f.email()
        default_password = "glorY1Asop856"
        email = self.browser.find_element(*BasePageLocators.INPUT_EMAIL)
        email.send_keys(random_email)
        password = self.browser.find_element(*BasePageLocators.INPUT_PASSWORD)
        password.send_keys(default_password)
        repeat_password = self.browser.find_element(*BasePageLocators.INPUT_REPEAT_PASSWORD)
        repeat_password.send_keys(default_password)
        button = self.browser.find_element(*BasePageLocators.REGISTRATION_SUBMIT)
        button.click()

