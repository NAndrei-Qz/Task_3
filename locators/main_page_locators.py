from selenium.webdriver.common.by import By


class MainPageLocators:
    ACCOUNT_BUTTON = [By.XPATH, './/a[@href="/account"]']
    ORDER_LIST_BUTTON = [By.XPATH, './/a[@href="/feed"]']
    CONSTRUCTOR_BUTTON = [By.XPATH, './/p[text()="Конструктор"]']
    CRATOR_BUN_BUTTON = [By.XPATH, './/a[@href="/ingredient/61c0c5a71d1f82001bdaaa6c"]']
    CLOSE_BUN_DETAILS_BUTTON = [By.CSS_SELECTOR, '.Modal_modal__close__TnseK']
    SAUCE_BUTTON = [By.XPATH, './/span[text() = "Соусы"]']
    CREATE_ORDER_BUTTON = [By.XPATH, './/button[text() = "Оформить заказ"]']
    CREATE_BURGER_TITLE = [By.XPATH, './/h1[text() = "Соберите бургер"]']
    INGREDIENT_DETAILS_TITLE = [By.XPATH, './/h2[text() = "Детали ингредиента"]']
    BUN_COUNTER = [By.XPATH, './/a[@href="/ingredient/61c0c5a71d1f82001bdaaa6c"]//div[@class="counter_counter__ZNLkj counter_default__28sqi"]']
    DROP_FIELD = [By.CSS_SELECTOR, '.BurgerConstructor_basket__29Cd7']
    ORDER_COOKING_TITLE = [By.XPATH, './/p[text()="Ваш заказ начали готовить"]']
    
