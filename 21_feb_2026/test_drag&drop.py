import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()
    yield driver
    driver.quit()


def test_drag_and_drop(driver):
    source = driver.find_element(By.XPATH, "//div[@id='draggable']")
    destination = driver.find_element(By.XPATH, "//div[@id='droppable']")

    Action = ActionChains(driver)
    Action.drag_and_drop(source, destination).perform()
    time.sleep(5)
