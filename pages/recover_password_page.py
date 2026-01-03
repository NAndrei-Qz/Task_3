import allure
from data import TestData
from pages.base_page import BasePage
from locators.recover_password_page_locators import RecoverPasswordPageLocators

class RecoverPasswordPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.locators = RecoverPasswordPageLocators()

    @allure.step('Ожидание видимости кнопки "Восстановить"')
    def wait_visibility_of_recovery_password_button(self):
        return self.wait_visibility_of_element(RecoverPasswordPageLocators.RECOVERY_PASSWORD_BUTTON)
    
    @allure.step('Нажатие на кнопку "Восстановить"')
    def click_on_recovery_password_button(self):
        return self.click_on_element(RecoverPasswordPageLocators.RECOVERY_PASSWORD_BUTTON, self.browser)
    
    @allure.step('Ожидание видимости поля "Пароль"')
    def wait_visibility_of_password_field(self):
        return self.wait_clickable_element(RecoverPasswordPageLocators.PASSWORD_FIELD_INPUT)
    
    @allure.step('Нажатие на кнопку "Скрыть/показать пароль"')
    def click_on_show_password_button(self):
        return self.click_on_element(RecoverPasswordPageLocators.SHOW_PASSWORD_BUTTON, self.browser)
    
    @allure.step('Ожидание видимости введенного пароля')
    def wait_visibility_password_field_is_active(self):
        return self.wait_visibility_of_element(RecoverPasswordPageLocators.PASSWORD_FIELD_ACTIVE)
    
    @allure.step('Заполнение поля "Email"')
    def input_email_for_recovery(self):
        return self.send_keys_to_input(RecoverPasswordPageLocators.EMAIL_FIELD_INPUT, TestData.EMAIL)
    
    @allure.step('Заполнение поля "Пароль"')
    def input_password_for_recovery(self):
        return self.send_keys_to_input(RecoverPasswordPageLocators.PASSWORD_FIELD_INPUT, TestData.PASSWORD)

    @allure.step('Получение значения из поля "Email"')
    def get_email_field_value(self):
        return self.get_attribute(RecoverPasswordPageLocators.EMAIL_FIELD_INPUT)
    
    