import allure
from url import Url
from pages.login_page import LoginPage
from pages.main_page import MainPage

class TestMainFunctionality:
    @allure.title('Проверка перехода на главную страницу по клику на «Конструктор»')
    @allure.description('Осуществляется переход на страницу авторизации, нажимается кнопка "Конструктор",'
                        ' по окончании теста проверяется url главной страницы')
    def test_redirect_to_constructor(self, browser, open_login_page):
        main_page = MainPage(browser)
        login_page = LoginPage(browser)
        main_page.wait_clickable_login_button()
        main_page.click_on_login_button()
        login_page.wait_clickable_enter_button()
        main_page.click_on_constructor_button()
        assert browser.current_url == Url.MAIN_PAGE

    @allure.title('Проверка перехода на страницу с заказами по клику на «Лента заказов»')
    @allure.description('Осуществляется переход на страницу авторизации, нажимается кнопка "Лента заказов",'
                        ' по окончании теста проверяется url страницы с заказами')
    def test_redirect_to_order_list(self, browser, open_login_page):
        main_page = MainPage(browser)
        login_page = LoginPage(browser)
        main_page.wait_clickable_login_button()
        main_page.click_on_login_button()
        login_page.wait_clickable_enter_button()
        main_page.click_on_order_list()
        assert browser.current_url == Url.ORDER_LIST_PAGE

    @allure.title('Проверка открытия всплывающего окна с деталями ингредиента')
    @allure.description('Осуществляется переход на главную страницу, происходит нажатие на ингредиент "Краторная булка N-200i",'
                        ' проверяется видимость окна с деталями об ингредиенте')
    def test_ingredient_details(self, browser, open_main_page):
        main_page = MainPage(browser)
        main_page.wait_clickable_ingredient()
        main_page.click_on_ingredient_card()
        assert main_page.wait_visibility_ingredients_card()

    @allure.title('Проверка закрытия всплывающего окна с деталями ингредиента')
    @allure.description('Осуществляется переход на главную страницу, происходит нажатие на ингредиент "Краторная булка N-200i",'
                        ' проверяется кликабельность кнопки закрытия деталей, осуществляется нажатие на "крестик", проверяется кликабельность'
                        ' кнопки "Соусы" для подтверждения закрытия окна с деталями ингредиента')
    def test_close_ingredient_details(self, browser, open_main_page):
        main_page = MainPage(browser)
        main_page.wait_clickable_ingredient()
        main_page.click_on_ingredient_card()
        main_page.wait_clickable_close_symbol()
        main_page.click_close_symbol()
        assert main_page.wait_clickable_sauce_button()

    @allure.title('Проверка увеличения счетчика ингредиента при добавлении его в заказ')
    @allure.description('Осуществляется переход на главную страницу, считывается начальный счетчик булки, перетаскивается'
                        ' краторная булка, проверяется увеличение счетчика на 2')
    def test_increase_ingredient_counter(self, browser, open_main_page):
        main_page = MainPage(browser)
        main_page.wait_clickable_ingredient()
        initial_counter = int(main_page.get_ingredient_counter())
        main_page.drag_and_drop_ingredient()
        final_counter = int(main_page.get_ingredient_counter())
        assert final_counter == initial_counter + 2

    @allure.title('Проверка возможности оформить заказ для авторизованного пользователя')
    @allure.description('Осуществляется регистрация и вход в аккаунт. В заказ добавляются ингредиенты, '
        'далее нажимается кнопка "Оформить заказ", проверяется открытие окна с номером заказа.')
    def test_create_order_with_auth(self, browser, open_login_page, create_and_delete_user):
        main_page = MainPage(browser)
        login_page = LoginPage(browser)
        login_page.wait_visibility_of_email_field()
        login_page.login_to_account()
        main_page.wait_clickable_order_button()
        main_page.drag_and_drop_ingredient()
        main_page.click_on_order_button()
        assert main_page.wait_visibility_orders_window()


