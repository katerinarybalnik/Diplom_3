from selenium import webdriver

from main_page import MainPage
from urls import BASE_URL

def test_click_order_feed_firefox():
    driver = webdriver.Firefox()

    driver.get(BASE_URL)
    page = MainPage(driver)
    page.click_order_feed()

    assert driver.current_url == BASE_URL + "/feed"

    driver.quit()


def test_ingredient_details_open_firefox():
    driver = webdriver.Firefox()

    driver.get(BASE_URL)
    page = MainPage(driver)
    page.click_ingredient()

    assert page.is_ingredient_details_displayed()

    driver.quit()

def test_ingredient_details_close_firefox():
    driver = webdriver.Firefox()

    driver.get(BASE_URL)
    page = MainPage(driver)
    page.click_ingredient()
    page.close_ingredient_details()
    page.wait_ingredient_details_close()

    assert not page.is_ingredient_details_displayed()

    driver.quit()

