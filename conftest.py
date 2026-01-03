import pytest
import allure
import requests
from data import TestData
from url import Url
from api_methods import ApiMethods
from selenium import webdriver


@pytest.fixture(params=['Chrome', 'Firefox'])
def browser(request):
    if request.param == 'Chrome':
        driver = webdriver.Chrome()
    elif request.param == 'Firefox':
        driver = webdriver.Firefox()
    else:
        raise ValueError(f'Unsupported browser {request.param}')

    yield driver
    driver.quit()

@pytest.fixture
def create_and_delete_user():
    response = ApiMethods.create_account(TestData.EMAIL, TestData.PASSWORD, TestData.NAME)
    access_token = response.json().get('accessToken')
    yield access_token
    requests.delete(Url.USER_API, headers={'Authorization': access_token})

@pytest.fixture
@allure.step('Переход на главную струницу')
def open_main_page(browser):
    browser.get(Url.MAIN_PAGE)
    browser.maximize_window()

@pytest.fixture
@allure.step('Переход на страницу авторизации')
def open_login_page(browser):
    browser.get(Url.LOGIN_PAGE)
    browser.maximize_window()

@pytest.fixture
@allure.step('Переход на страницу восстановления пароля')
def open_recovery_page(browser):
    browser.get(Url.FORGOT_PASSWORD_PAGE)
    browser.maximize_window()

@pytest.fixture
@allure.step('Переход на страницу со списком заказов')
def open_order_list_page(browser):
    browser.get(Url.ORDER_LIST_PAGE)
    browser.maximize_window()
