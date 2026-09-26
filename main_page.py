from locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from urls import BASE_URL


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def click_constructor(self):
        WebDriverWait(self.driver, 10).until(lambda driver: not driver.find_element(*MainPageLocators.MODAL_OVERLAY).is_displayed())
        self.driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()

    def click_order_feed(self):
        self.driver.find_element(*MainPageLocators.ORDER_FEED_BUTTON).click()

    def click_ingredient(self):
        self.driver.find_element(*MainPageLocators.INGREDIENT).click()

    def close_ingredient_details(self):
        self.driver.find_element(*MainPageLocators.CLOSE_MODAL_BUTTON).click()

    def wait_ingredient_details_close(self):
        WebDriverWait(self.driver, 5).until(lambda driver: not driver.find_element(*MainPageLocators.INGREDIENT_DETAILS).is_displayed())

    def is_ingredient_details_displayed(self):
        return self.driver.find_element(*MainPageLocators.INGREDIENT_DETAILS).is_displayed()

    def get_ingredient_counter(self):
        return self.driver.find_element(*MainPageLocators.INGREDIENT_COUNTER).text

    def drag_ingredient(self):
        ingredient = self.driver.find_element(*MainPageLocators.INGREDIENT)
        drop_area = self.driver.find_element(*MainPageLocators.BUN_DROP_AREA)

        ActionChains(self.driver) \
            .move_to_element(ingredient) \
            .click_and_hold() \
            .pause(1) \
            .move_to_element(drop_area) \
            .pause(1) \
            .release() \
            .perform()

    def get_total_orders(self):
        WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(*MainPageLocators.TOTAL_ORDERS_COUNTER).text != "")
        return self.driver.find_element(*MainPageLocators.TOTAL_ORDERS_COUNTER).text

    def get_orders_in_progress(self):
        WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(*MainPageLocators.ORDERS_IN_PROGRESS).is_displayed())
        return self.driver.find_element(*MainPageLocators.ORDERS_IN_PROGRESS).text

    def click_create_order(self):
        self.driver.find_element(*MainPageLocators.CREATE_ORDER_BUTTON).click()

    def get_order_number(self):
        return self.driver.find_element(*MainPageLocators.ORDER_NUMBER).text

    def set_email(self, email):
        self.driver.find_element(*MainPageLocators.EMAIL_INPUT).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(*MainPageLocators.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        self.driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()

    def login(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_login()

    def wait_login(self):
        WebDriverWait(self.driver, 5).until(lambda driver: driver.current_url == BASE_URL + "/")

    def wait_order_number(self):
        WebDriverWait(self.driver, 20).until(lambda driver:driver.find_element(*MainPageLocators.ORDER_NUMBER).text != "" and driver.find_element(*MainPageLocators.ORDER_NUMBER).text != "9999")

    def get_today_orders(self):
        WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(*MainPageLocators.TODAY_ORDERS_COUNTER).text != "")
        return self.driver.find_element(*MainPageLocators.TODAY_ORDERS_COUNTER).text

    
    