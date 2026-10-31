import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Добавляем в pytest флаг --headless
def pytest_addoption(parser):
    parser.addoption('--headless', action='store_true', help='Run tests in headless mode')


@pytest.fixture(scope="function")
def browser(request):
    options = Options()

    # Если запуск идет с флагом --headless (на GitHub Actions), включаем скрытый режим
    if request.config.getoption('--headless'):
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