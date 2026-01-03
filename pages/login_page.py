import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from data import TestData


class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.locators = LoginPageLocators()

    @allure.step('Ожидание кликабельности кнопки "Войти"')
    def wait_clickable_enter_button(self):
        return self.wait_clickable_element(LoginPageLocators.LOGIN_BUTTON)
    
    @allure.step('Ожидание видимости поля "Email"')
    def wait_visibility_of_email_field(self):
        return self.wait_clickable_element(LoginPageLocators.EMAIL_INPUT)
    
    @allure.step('Ожидание видимости кнопки "Войти"')
    def wait_visibility_enter_button(self):
        return self.wait_visibility_of_element(LoginPageLocators.LOGIN_BUTTON)
    
    @allure.step('Нажатие на кнопку "Восстановить пароль"')
    def click_on_recovery_password_button(self):
        return self.click_on_element(LoginPageLocators.FORGOT_PASSWORD_BUTTON, self.browser)
    
    allure.step('Вход в аккаунт')
    def login_to_account(self):
        self.send_keys_to_input(LoginPageLocators.EMAIL_INPUT, TestData.EMAIL)
        self.send_keys_to_input(LoginPageLocators.PASSWORD_INPUT, TestData.PASSWORD)
        self.click_on_element(LoginPageLocators.LOGIN_BUTTON, self.browser)

    
    
