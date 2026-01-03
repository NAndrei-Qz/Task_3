from selenium.webdriver.common.by import By


class OrderListPageLocators:
    CLOSE_ORDER_DETAILS_BUTTON = [By.XPATH, '//section[(@class = "Modal_modal_opened__3ISw4 Modal_modal__P3_V5")]//button[(@class = "Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK")]']
    IN_WORK_NUMBER = [By.XPATH, '//*[contains(@class,"orderListReady")]//li[contains(@class,"digits-default")]']
    ALL_ORDERS_COUNTER = [By.XPATH, ".//p[text()='Выполнено за все время:']/following-sibling::p[contains(@class, 'OrderFeed_number__2MbrQ')]"]
    TODAY_ORDERS_COUNTER = [By.XPATH, ".//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, 'OrderFeed_number__2MbrQ')]"]
    ORDER_CARD = [By.XPATH, '//*[contains(@class,"OrderHistory_textBox__3lgbs mb-6")]']
    