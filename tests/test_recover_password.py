import allure
from url import Url
from data import TestData
from pages.login_page import LoginPage
from pages.recover_password_page import RecoverPasswordPage


class TestRecoverPassword:
    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль»')
    @allure.description('Открывается страница авторизации в личный кабинет, осуществляется переход на страницу восстановления нажатием. '
    'По окончании теста проверяется, что текущий url соответствует странице восстановления пароля')
    def test_click_button_forgot_redirect_to_recover(self, browser, open_login_page):
        login_page = LoginPage(browser)
        recover_password_page = RecoverPasswordPage(browser)
        login_page.wait_visibility_enter_button()
        login_page.click_on_recovery_password_button()
        recover_password_page.wait_visibility_of_recovery_password_button()
        current_url = recover_password_page.get_current_url()
        assert current_url == Url.FORGOT_PASSWORD_PAGE

    @allure.title('Проверка ввода почты для восстановления и работоспособности кнопки «Восстановить»')
    @allure.description('Открывается страница восстановления пароля, в поле "Email" вводится почтовый адрес, значение поля Email сохраняется в переменную,'
                        ' осуществляется клик по кнопке "Восстановить". По окончании теста проверяется, что поле Email было заполнено верно и'
                        ' текущий url соответствует странице ввода нового пароля')
    def test_input_email_and_recover(self, browser, open_recovery_page):
        recover_password_page = RecoverPasswordPage(browser)
        recover_password_page.wait_visibility_of_recovery_password_button()
        recover_password_page.input_email_for_recovery()
        email_field_value = recover_password_page.get_email_field_value()
        recover_password_page.click_on_recovery_password_button()
        recover_password_page.wait_visibility_of_password_field()
        current_url = recover_password_page.get_current_url()
        assert current_url == Url.RESET_PASSWORD_PAGE and email_field_value == TestData.EMAIL

    @allure.title('Проверка работоспособности кнопки показать/скрыть пароль')
    @allure.description('Осуществляется переход на страницу ввода нового пароля, нажимается кнопка показать/скрыть пароль,'
                        ' проверяется активное состоянрие поля, и видимость пароля')
    def test_click_and_activation_field(self, browser, open_recovery_page):
        recover_password_page = RecoverPasswordPage(browser)
        recover_password_page.wait_visibility_of_recovery_password_button()
        recover_password_page.input_email_for_recovery()
        recover_password_page.click_on_recovery_password_button()
        recover_password_page.wait_visibility_of_password_field()
        recover_password_page.input_password_for_recovery()
        recover_password_page.click_on_show_password_button()
        assert recover_password_page.wait_visibility_password_field_is_active()

