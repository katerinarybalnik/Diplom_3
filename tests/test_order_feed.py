from selenium import webdriver

from main_page import MainPage
from urls import BASE_URL
from data import create_user

def test_total_orders_counter_increases():
    driver = webdriver.Chrome()

    driver.get(BASE_URL + "/feed")
    page = MainPage(driver)
    counter_before = int(page.get_total_orders())

    user = create_user()
    driver.get(BASE_URL + "/login")
    page.login(user["email"], user["password"])
    page.wait_login()

    page.drag_ingredient()
    page.click_create_order()
    page.wait_order_number()

    driver.get(BASE_URL + "/feed")
    counter_after = int(page.get_total_orders())

    assert counter_after > counter_before
    driver.quit()

def test_today_orders_counter_increases():
    driver = webdriver.Chrome()

    driver.get(BASE_URL + "/feed")
    page = MainPage(driver)
    counter_before = int(page.get_today_orders())

    user = create_user()
    driver.get(BASE_URL + "/login")
    page.login(user["email"], user["password"])
    page.wait_login()

    page.drag_ingredient()
    page.click_create_order()
    page.wait_order_number()

    driver.get(BASE_URL + "/feed")
    counter_after = int(page.get_today_orders())

    assert counter_after > counter_before
    driver.quit()

def test_order_number_in_progress():
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

    driver.get(BASE_URL + "/feed")
    orders_in_progress = page.get_orders_in_progress()

    assert order_number in orders_in_progress
    driver.quit()