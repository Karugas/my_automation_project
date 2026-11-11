# Automated Testing Framework (UI & API)

Проект по автоматизации UI и API тестирования веб-сервиса [[Swag Labs](https://www.saucedemo.com/)].

### 🧰 Используемый стек
* **Язык:** Python 3.10
* **Тестовый фреймворк:** Pytest
* **UI-автоматизация:** Selenium WebDriver (паттерн Page Object Model, разделение локаторов и логики страниц)
* **API-автоматизация:** Requests (проверка CRUD-операций, статус-кодов и схем ответов)
* **Отчетность и CI/CD:** Allure Framework, GitHub Actions, GitHub Pages

### ✅ Что покрыто тестами
* Авторизация пользователя (позитивные и негативные сценарии).
* Поиск товаров и добавление в корзину (UI).
* CRUD-операции через API (создание, изменение и удаление бронирований).


### 📊 Отчетность (Allure Report)

После каждого коммита тесты автоматически прогоняются в **GitHub Actions** (в headless-режиме), а актуальный отчет публикуется на GitHub Pages:

👉 **[Открыть интерактивный Allure Report](https://karugas.github.io/my_automation_project/)**

![Allure Report Preview](assets/allure-report.png)

---

### 📁 Структура проекта

```text
my_automation_project/
├── .github/workflows/   # Пайплайны GitHub Actions для автозапуска и деплоя отчетов
├── data/                # Тестовые данные и креды пользователей
├── locators/            # Локаторы веб-элементов, разделенные по страницам
├── pages/               # Page Object классы с методами взаимодействия со страницами
├── tests/               # UI автотесты и conftest.py с настройкой браузера
├── tests_back/          # API автотесты и HTTP-клиент
└── requirements.txt     # Зависимости проекта
```

### 🚀 Локальный запуск

1. Клонировать репозиторий:
   ```bash
   git clone https://github.com
   cd my_automation_project
   ```
2. Установить зависимости:
   ```bash
   pip install -r requirements.txt
   ```
3. Запустить все тесты:
   ```bash
   pytest
   ```
4. Запустить UI-тесты в фоновом режиме (без открытия окна браузера):
   ```bash
   pytest --headless
   ```
