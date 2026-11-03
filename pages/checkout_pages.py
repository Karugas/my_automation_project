from .base_page import BasePage
from locators.checkout_locators import CheckoutLocators


class CheckoutPage(BasePage):
    def input_information_user(self, first_name, last_name, postal_code):
        self.find_element(CheckoutLocators.FIRST_NAME).send_keys(first_name)
        self.find_element(CheckoutLocators.LAST_NAME).send_keys(last_name)
        self.find_element(CheckoutLocators.ZIP_CODE).send_keys(postal_code)

    def checkout_continue(self):
        self.find_element(CheckoutLocators.BUTTON_CONTINUE).click()

    def overview_finish(self):
        self.find_element(CheckoutLocators.BUTTON_FINISH).click()

    def tap_back_home(self):
        self.find_element(CheckoutLocators.BUTTON_BACK_HOME).click()

    def check_price_and_name_overview(self) -> dict:
        # Находим все продукты
        all_cards = self.find_elements(CheckoutLocators.CHECKOUT_LIST)
        target_cards = all_cards[:1]

        selected_name = []
        selected_price = []

        for card in target_cards:
            # Получаем название и цену
            product_name = card.find_element(*CheckoutLocators.CHECKOUT_NAME)
            selected_name.append(product_name.text)

            product_price = card.find_element(*CheckoutLocators.CHECKOUT_PRICE)
            selected_price.append(product_price.text)

        # Возвращаем данные что нашли
        return {"name": selected_name, "price": selected_price}

    def check_many_prices_and_names_overview(self) -> dict:
        # Находим все продукты и оставляем 4
        all_cards = self.find_elements(CheckoutLocators.CHECKOUT_LIST)
        target_cards = all_cards[:4]

        selected_name = []
        selected_price = []

        for card in target_cards:
            # Получаем название и цену
            product_name = card.find_element(*CheckoutLocators.CHECKOUT_NAME)
            selected_name.append(product_name.text)

            product_price = card.find_element(*CheckoutLocators.CHECKOUT_PRICE)
            selected_price.append(product_price.text)

        # Возвращаем данные что нашли
        return {"name": selected_name, "price": selected_price}

    def check_price_total(self):
        return self.find_element(CheckoutLocators.TOTAL_PRICE).text
