import allure
from url import Url
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.main_page import MainPage

class TestAccount:
    @allure.title('Проверка перехода на страницу авторизации по клику на «Личный кабинет»')
    @allure.description('Проверяется переход с главной страницы на страницу авторизации в аккаунт по нажатию кнопки'
                        ' "Личный кабинет", по окончании теста проверяется url страницы авторизации')
    def test_click_button_account_redirect_to_login(self, browser, open_main_page):
        main_page = MainPage(browser)
        login_page = LoginPage(browser)
        main_page.wait_clickable_login_button()
        main_page.click_on_login_button()
        login_page.wait_clickable_enter_button()
        current_url = login_page.get_current_url()
        assert current_url == Url.LOGIN_PAGE

    @allure.title('Проверка перехода на страницу профиля по клику на «Личный кабинет»')
    @allure.description('Создается пользователь. Проверяется переход с главной страницы на страницу личного кабинета по нажатию кнопки'
                        ' "Личный кабинет", по окончании теста проверяется url страницы личного кабинета')
    def test_click_button_account_redirect_to_profile(self, create_and_delete_user, browser, open_main_page):
        main_page = MainPage(browser)
        login_page = LoginPage(browser)
        profile_page = ProfilePage(browser)
        main_page.wait_clickable_login_button()
        main_page.click_on_login_button()
        login_page.wait_visibility_of_email_field()
        login_page.login_to_account()
        main_page.wait_clickable_order_button()
        main_page.click_on_login_button()
        profile_page.wait_visibility_exit_button()
        current_url = profile_page.get_current_url()
        assert current_url == Url.PROFILE_PAGE

    @allure.title('Проверка перехода из личного кабинета в раздел «История заказов»')
    @allure.description('Создается пользователь, открывается личный кабинет. Проверяется нажатие кнопки "История заказов,"'
                        ' по окончании теста проверяется url страницы "История заказов".')
    def test_open_order_history(self, create_and_delete_user, browser, open_login_page):
        main_page = MainPage(browser)
        login_page = LoginPage(browser)
        profile_page = ProfilePage(browser)
        login_page.wait_visibility_of_email_field()
        login_page.login_to_account()
        main_page.wait_clickable_order_button()
        main_page.click_on_login_button()
        profile_page.wait_clickable_orders_history()
        profile_page.click_on_orders_history()
        current_url = profile_page.get_current_url()
        assert current_url == Url.ORDER_HISTORY_PAGE

    @allure.title('Проверка выхода из аккаунта')
    @allure.description('Создается пользователь, открывается личный кабинет. Проверяется нажатие кнопки "Выход,"'
                        ' по окончании теста проверяется url страницы "Авторизация".')
    def test_exit_from_account(self, create_and_delete_user, browser, open_login_page):
        main_page = MainPage(browser)
        login_page = LoginPage(browser)
        profile_page = ProfilePage(browser)
        login_page.wait_visibility_of_email_field()
        login_page.login_to_account()
        main_page.wait_clickable_order_button()
        main_page.click_on_login_button()
        profile_page.wait_visibility_exit_button()
        profile_page.click_on_exit_button()
        login_page.wait_visibility_enter_button()
        current_url = login_page.get_current_url()
        assert current_url == Url.LOGIN_PAGE
