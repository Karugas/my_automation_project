import requests
from pydantic import BaseModel


class BookingResponseSchema(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: object
    additionalneeds: str


class ApiClient:
    def __init__(self):
        self.base_url = "https://restful-booker.herokuapp.com"
        self.session = requests.Session()  # Сессия сохраняет куки/заголовки между запросами

    def create_token(self):
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

    def create_booking_user(self, firstname, lastname):
        url = f"{self.base_url}/booking"
        payload = {
        "firstname": firstname,
        "lastname": lastname,
        "totalprice": 111,
        "depositpaid": "true",
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2026-10-01"
        },
        "additionalneeds": "Breakfast"
        }
        response = self.session.post(url, json=payload)
        return response

    def update_booking_user(self, id_user):
        url = f"{self.base_url}/booking/{id_user}"

        payload = {
            "firstname": "Test",
            "lastname": "Test",
            "totalprice": 111,
            "depositpaid": "true",
            "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2027-10-01"
            },
            "additionalneeds": "Breakfast"
            }
        response = self.session.put(url, json=payload)
        return response

    def authorize(self, token):
        self.session.headers.update({
            "Cookie": f"token={token}"})

    def witch_out_authorize(self):
        self.session.headers.update({
            "Cookie": f"token=123"})

    def patch_booking_user(self, id_user):
        url = f"{self.base_url}/booking/{id_user}"

        payload = {
            "firstname": "James",
            "lastname": "Brown",
            }
        response = self.session.patch(url, json=payload)
        return response

    def delete_user(self, id_user):
        url = f"{self.base_url}/booking/{id_user}"
        response = self.session.delete(url)
        return response

    def health_check(self):
        url = f"{self.base_url}/ping"
        response = self.session.get(url)
        return response

    def filter_by_name(self):
        url = f"{self.base_url}/booking?firstname=YaromirTestUser"
        response = self.session.get(url)
        return response
