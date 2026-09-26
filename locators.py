from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, ".//p[text()='Лента Заказов']")
    INGREDIENT = (By.XPATH, ".//p[text()='Флюоресцентная булка R2-D3']")
    INGREDIENT_DETAILS = (By.XPATH, ".//h2[text()='Детали ингредиента']")
    CLOSE_MODAL_BUTTON = (By.CSS_SELECTOR, "button[class*='Modal_modal__close']")
    INGREDIENT_COUNTER = (By.XPATH, ".//p[text()='Флюоресцентная булка R2-D3']/ancestor::a//div[contains(@class, 'counter_counter')]")
    BUN_DROP_AREA = (By.XPATH, ".//span[text()='Перетяните булочку сюда (верх)']")
    TOTAL_ORDERS_COUNTER = (By.XPATH, ".//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY_ORDERS_COUNTER = (By.XPATH, ".//p[text()='Выполнено за сегодня:']/following-sibling::p")
    ORDERS_IN_PROGRESS = (By.XPATH, ".//p[text()='В работе:']/following-sibling::ul[1]")
    CREATE_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")
    ORDER_NUMBER = (By.XPATH, ".//p[text()='идентификатор заказа']/preceding-sibling::h2")
    EMAIL_INPUT = (By.NAME, "name")
    PASSWORD_INPUT = (By.NAME, "Пароль")
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")
    MODAL_OVERLAY = (By.CSS_SELECTOR, "div[class*='Modal_modal_overlay']")