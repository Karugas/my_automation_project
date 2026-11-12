def test_filter_by_name(client):
    # Создание пользователя
    response = client.create_booking_user("YaromirTestUser", "Udovkin")
    assert response.status_code == 200, f"Ожидали 200, получили {response.status_code}"
    data = response.json()

    # Имя и Фамилия совпадают
    bookingid_create = data["bookingid"]
    assert "bookingid" in data, "Отсутствует id"
    assert data["booking"]["firstname"] == "YaromirTestUser"

    response = client.filter_by_name()
    assert response.status_code == 200, f"Ожидали 200, получили {response.status_code}"
    data_filter = response.json()
    assert {"bookingid": bookingid_create} in data_filter, "id отсутствует"
