import allure
from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators

class ProfilePage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.locators = ProfilePageLocators()

    @allure.step('Ожидание видимости кнопки "Выход"')
    def wait_visibility_exit_button(self):
        return self.wait_visibility_of_element(ProfilePageLocators.LOGOUT_BUTTON)
    
    @allure.step('Нажатие на кнопку "Выход"')
    def click_on_exit_button(self):
        self.click_on_element(ProfilePageLocators.LOGOUT_BUTTON, self.browser)
    
    @allure.step('Ожидание кликабельности кнопки "История заказов"')
    def wait_clickable_orders_history(self):
        return self.wait_clickable_element(ProfilePageLocators.ORDER_HISTORY_BUTTON)
    
    @allure.step('Нажатие на кнопку "История заказов"')
    def click_on_orders_history(self):
        self.click_on_element(ProfilePageLocators.ORDER_HISTORY_BUTTON, self.browser)
    
    