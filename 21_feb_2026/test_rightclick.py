import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
    driver.maximize_window()
    yield driver
    driver.quit()

def test_right_click(driver):
    rc = driver.find_element(By.XPATH, "//span[text()='right click me']")
    Action = ActionChains(driver)
    Action.context_click(rc).perform()
    time.sleep(5)

