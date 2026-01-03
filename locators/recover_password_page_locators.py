from selenium.webdriver.common.by import By


class RecoverPasswordPageLocators:
    EMAIL_FIELD_INPUT = [By.NAME, 'name']
    PASSWORD_FIELD_INPUT = [By.NAME, 'Введите новый пароль']
    RECOVERY_PASSWORD_BUTTON = [By.XPATH, './/button[text() = "Восстановить"]']
    SHOW_PASSWORD_BUTTON = [By.CSS_SELECTOR, '.input__icon-action']
    PASSWORD_FIELD_ACTIVE = [By.CSS_SELECTOR, '.input_status_active']
