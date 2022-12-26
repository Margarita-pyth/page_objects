from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage): 
    def adding_product_to_cart(self):
        """Добавление продукта в корзину."""
        login_link = self.browser.find_element(*ProductPageLocators.CART_BUTTON)
        login_link.click()

    def should_be_add_to_cart_button(self):
        """Проверка на наличие кнопки добавления в корзину."""
        assert self.is_element_present(*ProductPageLocators.CART_BUTTON), "Cart Button is not presented"

    def should_be_match_product_name_in_cart(self):
        """Проверяем, что присутствует сообщение о добавлении в корзину."""
        assert self.is_element_present(
            *ProductPageLocators.MESSAGE_ABOUT_ADING_TO_BASKET), "Message about adding to cart is not presented"
        """Проверяем,что имя товара идентично."""
        product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text
        assert product == product_in_message, "The name of the added product is different!"

    def should_be_match_the_price_in_cart(self):
        """Проверяем, что присутствует блок с ценой."""
        assert self.is_element_present(
            *ProductPageLocators.MESSAGE_WITH_PRICE), "Message about price is not presented"
        """Проверяем,что цена товара идентична."""
        price = self.browser.find_element(*ProductPageLocators.PRICE_IN_THE_CART).text
        price_in_message = self.browser.find_element(*ProductPageLocators.PRICE_IN_MESSAGE).text
        assert price == price_in_message, "The price of the added item is different!"

    def should_not_be_success_message(self):
        """Проверяем, что отсутствует сообщение о добавлении в корзину."""
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADING_TO_BASKET), \
       "Success message is presented, but should not be"

    def should_be_disappeared(self):
        """Проверяем, что элемент исчезает."""
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ABOUT_ADING_TO_BASKET), \
       "The element is not disappeared!"
