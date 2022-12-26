from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_message_about_adding_product_in_basket(self):
        """Проверяем, что отсутствует сообщение о добавлении в корзину."""
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), \
       "Success message is presented, but should not be"

    def should_be_message_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_EMPTY_BASKET), \
        "Message about empty basket is not presented"
        #message_about_empty_basket = self.browser.find_element(*BasketPageLocators.MESSAGE_EMPTY_BASKET).text
        #message = "Your basket is empty. Continue shopping"
        #assert message_about_empty_basket == message, "Message about empty basket is not presented"

