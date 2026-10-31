from pages.login_page import LoginPage
from data.user_data import TestUsers


link = "https://www.saucedemo.com/"


def test_login_standard_user(browser):
    page = LoginPage(browser, link)
    page.open()
    page.login(**TestUsers.STANDARD_USER)
    assert "inventory" in browser.current_url, "Не удалось войти!"


def test_login_invalid_password(browser):
    page = LoginPage(browser, link)
    page.open()
    page.login(**TestUsers.STANDARD_USER_INVALID)
    message_error = page.get_error_message()
    assert "Username and password do not match any user" in message_error, \
        f"Пароль должен был быть неверный, отдало: '{message_error}'"


def test_locked_out_user(browser):
    page = LoginPage(browser, link)
    page.open()
    page.login(**TestUsers.LOCKED_OUT_USER)
    message_error = page.get_error_message()
    assert "Sorry, this user has been locked out." in message_error, \
        f"Ожидали ошибку блокировки, но выдало '{message_error}'"
