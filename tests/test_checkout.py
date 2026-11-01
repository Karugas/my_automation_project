from data.user_data import TestUsers, CheckoutInformation
from pages.login_page import LoginPage

link = "https://www.saucedemo.com/"


def test_input_information_user(browser):
    page = LoginPage(browser, link)
    page.open()
    product_page = page.login(**TestUsers.STANDARD_USER)
    # Добавляем первый товар
    product_page.add_first_product_and_get_info()
    # Переходим в корзину
    cart_page = product_page.go_to_cart()

    # Переход на Checkout
    checkout_page = cart_page.go_to_checkout()
    # Ввод данных пользователя
    checkout_page.input_information_user(**CheckoutInformation.INFORMATION)
    # Переход на экран оплаты
    checkout_page.checkout_continue()


def test_buy_product(browser):
    page = LoginPage(browser, link)
    page.open()
    product_page = page.login(**TestUsers.STANDARD_USER)
    # Добавляем первый товар запоминая название и цену
    expected_info = product_page.add_first_product_and_get_info()
    print(f"\n[Каталог] Запомнил товар: {expected_info}")

    # Переходим в корзину
    cart_page = product_page.go_to_cart()

    # Переход на Checkout
    checkout_page = cart_page.go_to_checkout()
    # Ввод данных пользователя
    checkout_page.input_information_user(**CheckoutInformation.INFORMATION)
    # Переход на экран оплаты
    checkout_page.checkout_continue()

    # Проверяем название и цену товара в корзине
    actual_info = checkout_page.check_price_and_name_overview()
    print(f"[Корзина] Видим товар: {actual_info}")
    assert actual_info["name"] == expected_info["name"], "Наименования товаров в обзоре не совпадают"
    assert actual_info["price"] == expected_info["price"], "Цены товаров в обзоре не совпадают"

    # Сверяем цену товара и итоговое значение
    item_total = float(actual_info["price"].split('$')[1])
    tax = 8.004
    tax = round(item_total * (tax / 100), 2)
    price_total = checkout_page.check_price_total()
    price_total = float(price_total.split('$')[1])
    item_total = tax + item_total
    assert price_total == item_total, f"Ошибка {price_total} отличается от {item_total}"
    print(f"Успех! Числа совпали: {price_total} == {item_total}")
    # Тап Finish
    checkout_page.overview_finish()
    # Вернуться на главную страницу
    checkout_page.tap_back_home()
    assert checkout_page.wait_for_url("https://www.saucedemo.com/inventory.html")
