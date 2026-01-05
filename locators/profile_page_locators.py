from selenium.webdriver.common.by import By


class ProfilePageLocators:
    LOGOUT_BUTTON = [By.XPATH, './/button[text() = "Выход"]']
    ORDER_HISTORY_BUTTON = [By.XPATH, './/a[@href="/account/order-history"]']
