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


def test_double_click(driver):
    double_click = driver.find_element(By.XPATH, "//button[text()='Copy Text']")
    Action = ActionChains(driver)
    Action.double_click(double_click).perform()
    time.sleep(5)
