import webbrowser

import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nЗапуск браузера...")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nЗакрытие браузера...")
    browser.quit()