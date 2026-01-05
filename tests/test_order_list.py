import allure
import pytest
from api_methods import ApiMethods
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.order_list_page import OrderListPage
from pages.profile_page import ProfilePage


class TestOrderList:
    @allure.title('Проверка открытия всплывающего окна с деталями заказа')
    @allure.description('Открывается страница ленты заказов, нажатием на первый заказ, открываются детали заказа, '
                        ' проверяется появление кнопки закрытия окна с деталями заказа (крестик)')
    def test_open_order_details(self, browser, open_order_list_page):
        order_list_page = OrderListPage(browser)
        order_list_page.wait_visibility_order_card()
        order_list_page.click_on_order_card()
        assert order_list_page.wait_visibility_close_card_button()

    @allure.title('Проверка, что заказы пользователя из «История заказов» отображаются на странице «Лента заказов»')
    @allure.description('Создаётся аккаунт, осуществляется вход, с помощью API метода создается заказ и схорняется его номер.'
                        ' Происходит переход в историю заказов, сохраняется номер последнего заказа из истории. Происходит переход в ленту заказов'
                        ' и получение номера заказа. По окончании теста проверяется совпадение всех номеров заказа')
    def test_order_in_history_and_in_order_list(self, browser, open_login_page, create_and_delete_user):
        main_page = MainPage(browser)
        login_page = LoginPage(browser)
        profile_page = ProfilePage(browser)
        order_list_page = OrderListPage(browser)
        api_methods = ApiMethods()
        access_token = create_and_delete_user
        api_methods.create_order(access_token)
        order_number_api = api_methods.get_order_number(access_token)
        login_page.login_to_account()
        main_page.wait_clickable_order_button()
        main_page.click_on_login_button()
        profile_page.wait_clickable_orders_history()
        profile_page.click_on_orders_history()
        order_list_page.wait_visibility_order_card()
        order_number_history = order_list_page.find_order_number()
        main_page.click_on_order_list()
        order_list_page.wait_visibility_counter_all_time()
        order_number_feed = order_list_page.find_order_number()
        assert order_number_history == order_number_api and order_number_feed == order_number_api

    @allure.title('Проверка, что при создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    @allure.description('Создаётся аккаунт, осуществляется вход. Производится переход к ленте заказов, сохранение текущего'
                        ' количества заказов. Создается новый заказ с помощью API метода, осуществляется проверка обновленного количества заказов.')
    def test_alltime_order_counter(self, browser, open_login_page, create_and_delete_user):
        main_page = MainPage(browser)
        login_page = LoginPage(browser)
        order_list_page = OrderListPage(browser)
        api_methods = ApiMethods()
        access_token = create_and_delete_user
        login_page.wait_visibility_of_email_field()
        login_page.login_to_account()
        main_page.wait_clickable_order_button()
        main_page.click_on_order_list()
        order_list_page.wait_visibility_counter_all_time()
        initial_counter = int(order_list_page.get_alltime_counter())
        api_methods.create_order(access_token)
        final_counter = int(order_list_page.get_alltime_counter())
        assert final_counter > initial_counter

    
    @allure.title('Проверка, что при создании нового заказа счётчик "Выполнено за сегодня" увеличивается')
    @allure.description('Создаётся аккаунт, осуществляется вход. Производится переход к ленте заказов, сохранение текущего'
                        ' количества заказов. Создается новый заказ с помощью API метода, осуществляется проверка обновленного количества заказов.')
    def test_today_order_counter(self, browser, open_login_page, create_and_delete_user):
        main_page = MainPage(browser)
        login_page = LoginPage(browser)
        order_list_page = OrderListPage(browser)
        api_methods = ApiMethods()
        access_token = create_and_delete_user
        login_page.wait_visibility_of_email_field()
        login_page.login_to_account()
        main_page.wait_clickable_order_button()
        main_page.click_on_order_list()
        order_list_page.wait_visibility_counter_all_time()
        initial_counter = int(order_list_page.get_today_counter())
        api_methods.create_order(access_token)
        final_counter = int(order_list_page.get_today_counter())
        assert final_counter > initial_counter

    @allure.title('Проверка появления заказа в столбце "В работе"')
    @allure.description('Создаётся аккаунт, осуществляется вход. Создается новый заказ с помощью API метода, сохраняется номер'
    ' созданного заказа. Происходит поиск и сохранение номера заказа из раздела в "работе", осуществялется сравнение двух полученных номеров заказа')
    def test_new_order_in_work(self, browser, open_login_page, create_and_delete_user):
        main_page = MainPage(browser)
        login_page = LoginPage(browser)
        order_list_page = OrderListPage(browser)
        api_methods = ApiMethods()
        access_token = create_and_delete_user
        login_page.wait_visibility_of_email_field()
        login_page.login_to_account()
        main_page.wait_clickable_order_button()
        main_page.click_on_order_list()
        order_list_page.wait_visibility_order_card()
        api_methods.create_order(access_token)
        order_number_api = api_methods.get_order_number(access_token)        
        order_list_page.wait_visibility_in_work()
        order_number_in_work = int(order_list_page.get_order_number_in_work())
        assert order_number_api == order_number_in_work
    
