import pytest
from api_client import ApiClient


@pytest.fixture(scope="function")
def client():
    # Создаём чистый клиент для сессии
    client = ApiClient()
    yield client
