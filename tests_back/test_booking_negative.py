import pytest


@pytest.mark.parametrize("http_method", ["PUT", "PATCH", "DELETE"])
def test_update_user_without_token(client, http_method):
    # Обновление данных пользователя
    response = client.create_booking_user("Yaromir", "Udovkin")
    id_user = response.json()["bookingid"]

    payload = {"firstname": "Yaromir", "lastname": "Udovkin"}
    response = client.send_request_without_auth(
        method=http_method, booking_id=id_user, payload=payload
    )

    assert response.request.method == http_method, f"Методы не совпадают, должен быть: {http_method}"
    assert response.status_code == 403, f"Для метода {http_method} ожидали 403, получили {response.status_code}"
