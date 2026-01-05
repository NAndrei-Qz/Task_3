import requests
import allure
import random
from data import TestData
from url import Url

class ApiMethods:
    @staticmethod
    @allure.step('Регистрация пользователя')
    def create_account(email: str, password: str, name: str):
        return requests.post(url=Url.REGISTRATION_API, json={"email": email, "password": password, "name": name})

    @allure.step('Создание заказа')
    def create_order(self, access_token: str):
        response = requests.get(Url.INGREDIENTS_API)
        ingredients_data = response.json()['data']
        ingredients = {'ingredients': ingredients_data[random.randint(0, len(ingredients_data) - 1)]['_id']}
        return requests.post(Url.ORDERS_API, json=ingredients, headers={'Authorization': access_token})

    @allure.step('Получение номера заказа')
    def get_order_number(self, access_token):
        response = requests.get(Url.ORDERS_API, headers={'Authorization': access_token})
        return response.json()['orders'][0]['number']
    