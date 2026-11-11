import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Добавляем в pytest флаг --headless
def pytest_addoption(parser):
    parser.addoption('--headless', action='store_true', help='Run tests in headless mode')


@pytest.fixture(scope="function")
def browser(request):
    options = Options()

    options.add_experimental_option("prefs", {
        "profile.password_manager_leak_detection": False,  # Выключаем детекцию утечек паролей
        "profile.password_manager_enabled": False,  # Выключаем предложение сохранить пароль
        "credentials_enable_service": False  # Отключаем службу учетных данных
    })

    # Если запуск идет с флагом --headless (на GitHub Actions), включаем скрытый режим
    if request.config.getoption('--headless') or os.getenv("CI"):
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")

    print("\nЗапуск браузера...")
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10)

    yield browser

    print("\nЗакрытие браузера...")
    browser.quit()