from selenium import webdriver

from main_page import MainPage
from urls import BASE_URL
from data import create_user


def test_click_order_feed(driver):
    driver.get(BASE_URL)
    page = MainPage(driver)
    page.click_order_feed()
    assert driver.current_url == BASE_URL + "/feed"


def test_click_constructor(driver):
    driver.get(BASE_URL + "/feed")
    page = MainPage(driver)
    page.click_constructor()
    assert driver.current_url == BASE_URL + "/"

def test_ingredient_details_open(driver):
    driver.get(BASE_URL)
    page = MainPage(driver)
    page.click_ingredient()
    assert page.is_ingredient_details_displayed()

def test_ingredient_details_close(driver):
    driver.get(BASE_URL)
    page = MainPage(driver)
    page.click_ingredient()
    page.close_ingredient_details()
    page.wait_ingredient_details_close()
    assert not page.is_ingredient_details_displayed()

def test_ingredient_counter_increases(driver):
    driver.get(BASE_URL)
    page = MainPage(driver)
    counter_before = page.get_ingredient_counter()
    page.drag_ingredient()
    counter_after = page.get_ingredient_counter()
    assert int(counter_after) > int(counter_before)

def test_login():
    driver = webdriver.Chrome()
    user = create_user()
    driver.get(BASE_URL + "/login")
    page = MainPage(driver)
    page.login(user["email"], user["password"])
    page.wait_login()
    assert driver.current_url == BASE_URL + "/"
    driver.quit()

def test_create_order():
    driver = webdriver.Chrome()
    user = create_user()
    driver.get(BASE_URL + "/login")
    page = MainPage(driver)
    page.login(user["email"], user["password"])
    page.wait_login()
    page.drag_ingredient()
    page.click_create_order()
    page.wait_order_number()
    order_number = page.get_order_number()
    assert order_number != ""
    driver.quit()

def test_get_today_orders():
    driver = webdriver.Chrome()
    driver.get(BASE_URL + "/feed")
    page = MainPage(driver)
    today_orders = page.get_today_orders()
    assert today_orders != ""
    driver.quit()

def test_get_total_orders():
    driver = webdriver.Chrome()
    driver.get(BASE_URL + "/feed")
    page = MainPage(driver)
    total_orders = page.get_total_orders()
    assert total_orders != ""
    driver.quit()

