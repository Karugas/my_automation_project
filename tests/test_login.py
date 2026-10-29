from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


def test_login_standard_user(browser):
    link = "https://www.saucedemo.com/"
    page = LoginPage(browser, link)

    page.open()
    page.login("secret_sauce", "standard_user")

    assert "inventory" in browser.current_url, "Не удалось войти!"

#def test_locked_out_user(browser):