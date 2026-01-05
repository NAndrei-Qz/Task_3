import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.action_chains import ActionChains

class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.locators = MainPageLocators()

    @allure.step('Ожидание кликабельности кнопки "Личный кабинет"')
    def wait_clickable_login_button(self):
        return self.wait_clickable_element(MainPageLocators.ACCOUNT_BUTTON)

    @allure.step('Нажатие на кнопку "Личный кабинет"')
    def click_on_login_button(self):
        self.click_on_element(MainPageLocators.ACCOUNT_BUTTON, self.browser)

    @allure.step('Ожидание кликабельности кнопки "Конструктор"')
    def wait_clickable_constructor_button(self):
        return self.wait_clickable_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Нажатие на кнопку "Конструктор"')
    def click_on_constructor_button(self):
        self.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON, self.browser)

    @allure.step('Ожидание кликабельности кнопки "Оформить заказ"')
    def wait_clickable_order_button(self):
        return self.wait_clickable_element(MainPageLocators.CREATE_ORDER_BUTTON)

    @allure.step('Нажатие на кнопку "Оформить заказ"')
    def click_on_order_button(self):
        self.click_on_element(MainPageLocators.CREATE_ORDER_BUTTON, self.browser)

    @allure.step('Ожидание кликабельности кнопки "Лента Заказов"')
    def wait_clickable_order_list(self):
        return self.wait_clickable_element(MainPageLocators.ORDER_LIST_BUTTON)

    @allure.step('Нажатие на кнопку "Лента Заказов"')
    def click_on_order_list(self):
        self.click_on_element(MainPageLocators.ORDER_LIST_BUTTON, self.browser)

    @allure.step('Ожидание кликабельности изображения ингредиента')
    def wait_clickable_ingredient(self):
        return self.wait_clickable_element(MainPageLocators.CRATOR_BUN_BUTTON)

    @allure.step('Открытие карточки ингредиента путём нажатия на ингредиент')
    def click_on_ingredient_card(self):
        self.click_on_element(MainPageLocators.CRATOR_BUN_BUTTON, self.browser)

    @allure.step('Ожидание кликабельности кнопки закрытия карточки ингредиента')
    def wait_clickable_close_symbol(self):
        return self.wait_clickable_element(MainPageLocators.CLOSE_BUN_DETAILS_BUTTON)

    @allure.step('Нажатие на кнопку "Крестик" в деталях ингредиента')
    def click_close_symbol(self):
        self.click_on_element(MainPageLocators.CLOSE_BUN_DETAILS_BUTTON, self.browser)
    
    @allure.step('Ожидание кликабельности кнопки закрытия карточки ингредиента')
    def wait_clickable_sauce_button(self):
        return self.wait_clickable_element(MainPageLocators.SAUCE_BUTTON)
    
    @allure.step('Ожидание невидимости надписи "Соберите бургер"')
    def wait_invisibility_order_button(self):
        return self.wait_invisibility_of_element(MainPageLocators.CREATE_BURGER_TITLE)
    
    @allure.step('Ожидание кликабельности ингредиента')
    def wait_clickable_ingredient(self):
        return self.wait_clickable_element(MainPageLocators.CRATOR_BUN_BUTTON)
    
    @allure.step('Ожидание видимости деталей ингредиента')
    def wait_visibility_ingredients_card(self):
        return self.wait_visibility_of_element(MainPageLocators.INGREDIENT_DETAILS_TITLE)
    
    @allure.step('Ожидание видимости окна с номером заказа')
    def wait_visibility_orders_window(self):
        return self.wait_visibility_of_element(MainPageLocators.ORDER_COOKING_TITLE)
    
    @allure.step('Получение счетчика ингредиента')
    def get_ingredient_counter(self):
        return self.get_text(MainPageLocators.BUN_COUNTER)
    
    @allure.step('Перетаскивание ингредиента')
    def drag_and_drop_ingredient(self):
        action = ActionChains(self.browser)
        source_element = self.wait_visibility_of_element(MainPageLocators.CRATOR_BUN_BUTTON)
        target_element = self.wait_visibility_of_element(MainPageLocators.DROP_FIELD)
        if 'chrome' in str(self.browser):
            action.drag_and_drop(source_element, target_element).perform()
        elif 'firefox' in str(self.browser):
            self.browser.execute_script(
                "function createEvent(typeOfEvent) { " +
                "var event = document.createEvent('CustomEvent'); " +
                "event.initCustomEvent(typeOfEvent, true, true, null); " +
                "event.dataTransfer = { " +
                "data: {}, " +
                "setData: function(key, value) { this.data[key] = value; }, " +
                "getData: function(key) { return this.data[key]; } " +
                "}; " +
                "return event; " +
                "} " +
                "function dispatchEvent(element, typeOfEvent, event) { " +
                "if (element.dispatchEvent) { " +
                "element.dispatchEvent(event); " +
                "} else if (element.fireEvent) { " +
                "element.fireEvent('on' + typeOfEvent, event); " +
                "} " +
                "} " +
                "function simulateHTML5DragAndDrop(element, destination) { " +
                "var dragStartEvent = createEvent('dragstart'); " +
                "dispatchEvent(element, 'dragstart', dragStartEvent); " +
                "var dropEvent = createEvent('drop'); " +
                "dispatchEvent(destination, 'drop', dropEvent); " +
                "var dragEndEvent = createEvent('dragend'); " +
                "dispatchEvent(element, 'dragend', dragEndEvent); " +
                "} " +
                "simulateHTML5DragAndDrop(arguments[0], arguments[1]);",
                source_element,
                target_element
            )             
    