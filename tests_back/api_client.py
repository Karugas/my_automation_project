import requests
from pydantic import BaseModel


class ApiClient:
    def __init__(self):
        self.base_url = "https://restful-booker.herokuapp.com"
        self.session = requests.Session()  # Сессия сохраняет куки/заголовки между запросами

    def create_token(self, username, password):
        # Получаем токен администратора (POST-запрос)
        url = f"{self.base_url}/auth"
        payload = {
            "username": "admin",
            "password": "password123"
        }
        response = self.session.post(url, json=payload)
        return response

    def get_booking_user(self, user_id):
        url = f"{self.base_url}/booking/{user_id}"
        response = self.session.get(url)
        return response

    def get_booking_list(self):
        url = f"{self.base_url}/booking"
        response = self.session.get(url)
        return response


class BookingResponseSchema(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: object
    additionalneeds: str
