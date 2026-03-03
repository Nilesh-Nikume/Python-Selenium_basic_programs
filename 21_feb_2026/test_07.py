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
    elements = driver.find_elements(By.XPATH, "//*[@id='productTable']")
    for ch in elements:

        print(ch.text)
    time.sleep(5)

