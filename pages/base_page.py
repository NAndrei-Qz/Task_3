import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    @allure.step('Поиск элемента "{locator}" на странице')
    def find_of_element(self, locator):
        return self.browser.find_element(*locator)

    @allure.step('Клик по элементу "{locator}"')
    def click_on_element(self, locator, browser_name):
        if 'chrome' in str(browser_name):
            self.browser.find_element(*locator).click()
        elif 'firefox' in str(browser_name):
            element = self.browser.find_element(*locator)
            return self.browser.execute_script("arguments[0].click();", element)

    @allure.step('Ввод данных в поле "{locator}": {keys}')
    def send_keys_to_input(self, locator, keys):
        return self.browser.find_element(*locator).send_keys(keys)

    @allure.step('Скроллинг страницы до элемента "{locator}"')
    def scrolling_to_element(self, locator):
        element = self.wait_visibility_of_element(locator)
        self.browser.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Ожидание появления элемента "{locator}" на странице')
    def wait_visibility_of_element(self, locator):
        return WebDriverWait(self.browser, 10).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Ожидание кликабельности элемента "{locator}"')
    def wait_clickable_element(self, locator):
        return WebDriverWait(self.browser, 10).until(expected_conditions.element_to_be_clickable(locator))

    @allure.step('Ожидание исчезновения элемента "{locator}" со страницы')
    def wait_invisibility_of_element(self, locator):
        return WebDriverWait(self.browser, 10).until(expected_conditions.invisibility_of_element_located(locator))

    @allure.step('Получение текста элемента "{locator}"')
    def get_text(self, locator):
        return self.browser.find_element(*locator).text

    @allure.step('Получение атрибута элемента "{locator}"')
    def get_attribute(self, locator):
        return self.browser.find_element(*locator).get_attribute("value")

    @allure.step('Получение url текущей страницы')
    def get_current_url(self):
        return self.browser.current_url
