from api_client import ApiClient, BookingResponseSchema


# Инициализируем нашего API-клиента
client = ApiClient()


def test_get_booking_list():
    # Метод GET, получаем список книг
    response = client.get_booking_list()
    # Проверяем что отдаёт 200
    assert response.status_code == 200, f"Ожидали 200, получили {response.status_code}"
    # Превращаем ответ из JSON в python словарь dict
    data = response.json()
    assert {'bookingid': 1} in data


def test_get_booking_user():
    # Получаем информацию о пользователе
    response = client.get_booking_user(12)
    assert response.status_code == 200, f"Ожидали 200, получили {response.status_code}"
    data = response.json()
    assert BookingResponseSchema(**data), "Неверные типы данных"


def test_create_booking():
    response = client.create_booking_user("Yaromir", "Udovkin")
    assert response.status_code == 200, f"Ожидали 200, получили {response.status_code}"
    data = response.json()
    assert "bookingid" in data, "Отсутствует id"
    assert data["booking"]["firstname"] == "Yaromir"
    assert data["booking"]["lastname"] == "Udovkin"

