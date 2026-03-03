import time

import pytest
import pdb
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://demo.automationtesting.in")
    driver.maximize_window()
    driver.find_element(By.ID, "btn2").click()

    Switch_To = driver.find_element(By.XPATH, "// a[normalize-space() = 'SwitchTo']")
    Alters = driver.find_element(By.XPATH, "//ul[@class='dropdown-menu']//a[normalize-space()='Alerts']")

    mouse_action = ActionChains(driver)

    mouse_action.move_to_element(Switch_To).move_to_element(Alters).click().perform()

    yield driver
    driver.quit()


def test_alert_with_ok(driver):
    assert "https://demo.automationtesting.in/Alerts.html" == driver.current_url
    driver.find_element(By.XPATH, "// button[ @class ='btn btn-danger']").click()

    alert_window = driver.switch_to.alert
    print(alert_window.text)
    alert_window.accept()


def test_alert_with_ok_and_cancel(driver):
    wait = WebDriverWait(driver, 5)

    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[@class='analystic' and normalize-space()='Alert with OK & Cancel']"))).click()

    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[normalize-space()='click the button to display a confirm box']"))).click()

    pop_up = driver.switch_to.alert
    print(pop_up.text)
    pop_up.dismiss()


def test_alert_with_textbox(driver):
    wait = WebDriverWait(driver, 5)

    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[@class='analystic' and normalize-space()='Alert with Textbox']"))).click()

    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[normalize-space()='click the button to demonstrate the prompt box']"))).click()

    pop_up = wait.until(EC.alert_is_present())
    print(pop_up.text)

    pop_up.send_keys("Nilesh")
    print("Text entered successfully")

    pop_up.accept()

    result = driver.find_element(By.ID, "demo1").text
    print("Result message:", result)

