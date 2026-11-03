from data.user_data import TestUsers
from pages.login_page import LoginPage

link = "https://www.saucedemo.com/"


# Добавляем 1 товар в корзину
def test_add_product_to_cart(browser):
    # Авторизация
    page = LoginPage(browser, link)
    page.open()
    product_page = page.login(**TestUsers.STANDARD_USER)

    # Добавляем первый товар запоминая название и цену
    expected_info = product_page.add_first_product_and_get_info()
    print(f"\n[Каталог] Запомнил товар: {expected_info}")

    # Корзина заполнилась на +1
    cart = product_page.item_in_cart()
    assert int(cart) == 1, f"В корзине должен быть 1 товар, а их {int(cart)}"
    print(f"Товаров в корзине {int(cart)}")

    # Переходим в корзину
    cart_page = product_page.go_to_cart()

    # Проверяем название и цену товара в корзине
    actual_info = cart_page.check_price_and_name()
    print(f"[Корзина] Видим товар: {actual_info}")

    assert actual_info["name"] == expected_info["name"], "Наименования товаров в корзине не совпадают"
    assert actual_info["price"] == expected_info["price"], "Цены товаров в корзине не совпадают"


# Добавляем 4 товар в корзину
def test_add_products_to_cart(browser):
    # Авторизация
    page = LoginPage(browser, link)
    page.open()
    product_page = page.login(**TestUsers.STANDARD_USER)

    # Добавляем первый товар запоминая название и цену
    expected_info = product_page.add_products_and_get_info()
    print(f"\n[Каталог] Запомнил товар: {expected_info}")

    # Корзина заполнилась на +4
    cart = product_page.item_in_cart()
    assert int(cart) == 4, f"В корзине должен быть 4 товар, а их {int(cart)}"
    print(f"Товаров в корзине {int(cart)}")

    # Переходим в корзину
    cart_page = product_page.go_to_cart()

    # Проверяем название и цену товара в корзине
    actual_info = cart_page.check_price_and_name()
    print(f"[Корзина] Видим товар: {actual_info}")

    assert actual_info["name"] == expected_info["name"], "Наименования товаров в корзине не совпадают"
    assert actual_info["price"] == expected_info["price"], "Цены товаров в корзине не совпадают"


# Удаляем товар из корзины
def test_delete_product_in_cart(browser):
    # Авторизация
    page = LoginPage(browser, link)
    page.open()
    product_page = page.login(**TestUsers.STANDARD_USER)

    # Добавляем первый товар в корзину
    product_page.add_first_product_and_get_info()

    # Переходим в корзину
    cart_page = product_page.go_to_cart()

    # Удаляем товар
    cart_page.remove_item_in_cart()
    print("\nТовар удалён")

    # Корзина -1
    empty_cart = cart_page.empty_cart()
    assert empty_cart == "Cart, empty", "Корзина не очистилась"


# Удаляем товар на экране товаров
def test_delete_product(browser):
    # Авторизация
    page = LoginPage(browser, link)
    page.open()
    product_page = page.login(**TestUsers.STANDARD_USER)

    # Добавляем первый товар в корзину
    product_page.add_first_product_and_get_info()

    # Корзина заполнилась на +1
    cart = product_page.item_in_cart()
    assert int(cart) == 1, f"В корзине должен быть 1 товар, а их {int(cart)}"
    print(f"\nТоваров в корзине {int(cart)}")

    # Удаляем продукт
    product_page.delete_item()

    # "Delete" -> "Add to cart"
    product_page.check_switch_delete_on_add_to_cart()
    print("Товар удалён")

    # Корзина -1
    empty_cart = product_page.empty_cart()
    assert empty_cart == "Cart, empty", "Корзина не очистилась"


# Сортировка Low to High
def test_sorted_product_low_to_high(browser):
    # Авторизация
    page = LoginPage(browser, link)
    page.open()
    product_page = page.login(**TestUsers.STANDARD_USER)

    # Получаем все ценники на экране
    price_list = product_page.price_all_products()
    print(f"\nЦенники до сортировки: {price_list}")

    # Сортируем по low_to_high
    product_page.sort_products_low_to_high()
    price_list_after = product_page.price_all_products()
    print(f"Ценники после сортировки: {price_list_after}")
    assert sorted(price_list) == price_list_after, \
        f"Сортировка не верна, отдаёт {price_list}, вместо {price_list_after}"


# Сортировка High to Low
def test_sorted_product_high_to_low(browser):
    # Авторизация
    page = LoginPage(browser, link)
    page.open()
    product_page = page.login(**TestUsers.STANDARD_USER)

    # Получаем все ценники на экране
    price_list = product_page.price_all_products()
    print(f"\nЦенники до сортировки: {price_list}")

    # Сортируем по low_to_high
    product_page.sort_products_high_to_low()
    price_list_after = product_page.price_all_products()
    print(f"Ценники после сортировки: {price_list_after}")
    assert sorted(price_list, reverse=True) == price_list_after, \
        f"Сортировка не верна, отдаёт {price_list}, вместо {price_list_after}"
