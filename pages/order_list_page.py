import allure
from pages.base_page import BasePage
from locators.order_list_page import OrderListPageLocators

class OrderListPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.locators = OrderListPageLocators()

    @allure.step('Ожидание видимости номера заказа под надписью "В работе"')
    def wait_visibility_in_work(self):
        return self.wait_visibility_of_element(OrderListPageLocators.IN_WORK_NUMBER)
    
    @allure.step('Ожидание видимости карточки заказа')
    def wait_visibility_order_card(self):
        return self.wait_visibility_of_element(OrderListPageLocators.ORDER_CARD)
    
    @allure.step('Ожидание видимости счетчика "Выполнено за все время"')
    def wait_visibility_counter_all_time(self):
        return self.wait_visibility_of_element(OrderListPageLocators.ALL_ORDERS_COUNTER)
    
    @allure.step('Получение номер заказа под надписью "В работе"')
    def get_order_number_in_work(self):
        return self.get_text(OrderListPageLocators.IN_WORK_NUMBER)
    
    @allure.step('Поиск номера у карточки заказа')
    def find_order_number(self):
        num = self.find_of_element(OrderListPageLocators.ORDER_CARD).text.replace('\n', ' ').split(' ')
        return int(num[0].replace('#', ''))
    
    @allure.step('Нажатие на карточку заказа')
    def click_on_order_card(self):
        self.click_on_element(OrderListPageLocators.ORDER_CARD, self.browser)
    
    @allure.step('Ожидание видимости кнопки закрытия карточки заказа')
    def wait_visibility_close_card_button(self):
        return self.wait_visibility_of_element(OrderListPageLocators.CLOSE_ORDER_DETAILS_BUTTON)
    
    @allure.step('Получение счетчика "За всё время"')
    def get_alltime_counter(self):
        return self.get_text(OrderListPageLocators.ALL_ORDERS_COUNTER)
    
    @allure.step('Получение счетчика "За сегодня"')
    def get_today_counter(self):
        return self.get_text(OrderListPageLocators.TODAY_ORDERS_COUNTER)
    
    
    