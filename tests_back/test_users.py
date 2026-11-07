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
    # Создание пользователя
    response = client.create_booking_user("Yaromir", "Udovkin")
    assert response.status_code == 200, f"Ожидали 200, получили {response.status_code}"
    data = response.json()
    # Имя и Фамилия совпадают
    assert "bookingid" in data, "Отсутствует id"
    assert data["booking"]["firstname"] == "Yaromir"
    assert data["booking"]["lastname"] == "Udovkin"
    print(123)

def test_update_user_booking():
    # Обновление данных пользователя
    response = client.create_booking_user("Yaromir", "Udovkin")
    assert response.status_code == 200, f"Ожидали 200, получили {response.status_code}"
    data = response.json()
    id_user = data["bookingid"]

    # Создаём токен админа для UPDATE
    token = client.create_token().json()
    token = token["token"]
    client.authorize(token=token)

    # Обновляем данные пользователя (Имя, Фамилия)
    response = client.update_booking_user(id_user=id_user)
    assert response.status_code == 200, f"Ожидали 200, получили {response.status_code}"
    data = response.json()
    assert data["firstname"] == 'Test', "Имя не изменилось"
    assert data["lastname"] == 'Test', "Фамилия не изменилась"
