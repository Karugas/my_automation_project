def test_health_check(client):
    # Работает ли ресурс
    response = client.health_check()
    assert response.status_code == 201, "Сервис не отвечает"
