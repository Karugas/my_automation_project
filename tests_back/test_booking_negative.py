import pytest


@pytest.mark.parametrize("http_method", ["PUT", "PATCH", "DELETE"])
def test_update_user_without_token(client, http_method):
    # Обновление данных пользователя
    response = client.create_booking_user("Yaromir", "Udovkin")
    assert response.status_code == 200, f"Ожидали 200, получили {response.status_code}"
    data = response.json()
    id_user = data["bookingid"]

    # Обновляем данные пользователя (Имя, Фамилия)
    response = client.update_booking_user(id_user=id_user)
    assert response.status_code == 403, f"Для метода {http_method} ожидали 403, получили {response.status_code}"
