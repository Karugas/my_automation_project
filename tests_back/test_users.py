from api_client import BookingResponseSchema


def test_health_check(client):
    # Работает ли ресурс
    response = client.health_check()
    assert response.status_code == 201, "Сервис не отвечает"


def test_get_booking_list(client):
    # Метод GET, получаем список книг
    response = client.get_booking_list()
    # Проверяем что отдаёт 200
    assert response.status_code == 200, f"Ожидали 200, получили {response.status_code}"
    # Превращаем ответ из JSON в python словарь dict
    data = response.json()
    assert {"bookingid": not None} in data, "Отсутствует id"


def test_get_booking_user(client):
    # Получаем информацию о пользователе
    response = client.get_booking_user(12)
    assert response.status_code == 200, f"Ожидали 200, получили {response.status_code}"
    data = response.json()
    BookingResponseSchema(**data), "Неверные типы данных"


def test_create_booking(client):
    # Создание пользователя
    response = client.create_booking_user("Yaromir", "Udovkin")
    assert response.status_code == 200, f"Ожидали 200, получили {response.status_code}"
    data = response.json()
    # Имя и Фамилия совпадают
    assert "bookingid" in data, "Отсутствует id"
    assert data["booking"]["firstname"] == "Yaromir"
    assert data["booking"]["lastname"] == "Udovkin"


def test_update_user_booking(client):
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


def test_patch_user_booking(client):
    # Обновление данных пользователя
    response = client.create_booking_user("Yaromir", "Udovkin")
    assert response.status_code == 200, f"Ожидали 200, получили {response.status_code}"
    data = response.json()
    id_user = data["bookingid"]

    # Создаём токен админа для PATCH
    token = client.create_token().json()
    token = token["token"]
    client.authorize(token=token)

    # Обновляем данные пользователя (Имя, Фамилия)
    response = client.patch_booking_user(id_user=id_user)
    assert response.status_code == 200, f"Ожидали 200, получили {response.status_code}"
    data = response.json()
    assert data["firstname"] == 'James', "Имя не изменилось"
    assert data["lastname"] == 'Brown', "Фамилия не изменилась"


def test_delete_user_booking(client):
    # Обновление данных пользователя
    response = client.create_booking_user("Yaromir", "Udovkin")
    assert response.status_code == 200, f"Ожидали 200, получили {response.status_code}"
    data = response.json()
    id_user = data["bookingid"]

    # Создаём токен админа для DELETE
    token = client.create_token().json()
    token = token["token"]
    client.authorize(token=token)

    # Удаляем пользователя
    response = client.delete_user(id_user=id_user)
    assert response.status_code == 201, f"Ожидали 200, получили {response.status_code}"

    # Проверяем что пользователя нет
    response = client.get_booking_user(id_user)
    assert response.status_code == 404, f"Ожидали 404, получили {response.status_code}"


def test_update_user_without_token(client):
    # Обновление данных пользователя
    response = client.create_booking_user("Yaromir", "Udovkin")
    assert response.status_code == 200, f"Ожидали 200, получили {response.status_code}"
    data = response.json()
    id_user = data["bookingid"]

    # Обновляем данные пользователя (Имя, Фамилия)
    response = client.update_booking_user(id_user=id_user)
    assert response.status_code == 403, f"Ожидали 403, получили {response.status_code}"


def test_patch_user_without_token(client):
    # Обновление данных пользователя
    response = client.create_booking_user("Yaromir", "Udovkin")
    assert response.status_code == 200, f"Ожидали 200, получили {response.status_code}"
    data = response.json()
    id_user = data["bookingid"]

    # Обновляем данные пользователя (Имя, Фамилия)
    response = client.patch_booking_user(id_user=id_user)
    assert response.status_code == 403, f"Ожидали 403, получили {response.status_code}"


def test_delete_user_without_token(client):
    # Обновление данных пользователя
    response = client.create_booking_user("Yaromir", "Udovkin")
    assert response.status_code == 200, f"Ожидали 200, получили {response.status_code}"
    data = response.json()
    id_user = data["bookingid"]

    # Удаляем пользователя
    response = client.delete_user(id_user=id_user)
    assert response.status_code == 403, f"Ожидали 403, получили {response.status_code}"


def test_filter_by_name(client):
    # Создание пользователя
    response = client.create_booking_user("YaromirTestUser", "Udovkin")
    assert response.status_code == 200, f"Ожидали 200, получили {response.status_code}"
    data = response.json()

    # Имя и Фамилия совпадают
    bookingid_create = data["bookingid"]
    print(bookingid_create)
    assert "bookingid" in data, "Отсутствует id"
    assert data["booking"]["firstname"] == "YaromirTestUser"

    response = client.filter_by_name()
    assert response.status_code == 200, f"Ожидали 200, получили {response.status_code}"
    data_filter = response.json()
    assert {"bookingid": bookingid_create} in data_filter, "id отсутствует"
