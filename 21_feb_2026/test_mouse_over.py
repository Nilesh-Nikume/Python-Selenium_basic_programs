import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def test_mouse_over():
    driver = webdriver.Chrome()
    driver.get("https://www.irctc.co.in/nget/train-search")
    driver.maximize_window()
    # alert = driver.switch_to.alert
    # alert.accept()
    driver.find_element(By.XPATH, "//button[@class ='btn btn-primary']").click()
    time.sleep(5)

    trains = driver.find_element(By.XPATH, "//a[@aria-label='Menu Train']//strong[normalize-space()='TRAINS']")
    train_booking = driver.find_element(By.XPATH, "//span[@class='list_text' and normalize-space() = 'IRCTC TRAINS']")
    group_booking = driver.find_element(By.XPATH, "//span[@class='list_text' and normalize-space() = 'Group Booking']")

    mouse_over_action = ActionChains(driver)

    mouse_over_action.move_to_element(trains).move_to_element(train_booking).move_to_element(
        group_booking).click().perform()
    # print(driver.current_url)

    assert "https://www.irctc.co.in/nget/train-search" in driver.current_url
    time.sleep(4)
