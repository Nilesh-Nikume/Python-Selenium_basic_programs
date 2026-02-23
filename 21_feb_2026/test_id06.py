import time

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.idrive.com/endpoint-backup/")
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.description("Verify Idriver360 URL")
@allure.title("TC01- Verify ULR is working or not")
def test_open_url(driver):
    click_sign_in_option = driver.find_element(By.LINK_TEXT, "Sign In")
    click_sign_in_option.click()
    time.sleep(5)
    heading = driver.find_element(By.CLASS_NAME, "id-maincnt-title")
    actual_text = heading.text
    expected_text = "Sign in to IDrive 360"
    allure.attach(driver.get_screenshot_as_png(), name="before-login-page", attachment_type=allure.attachment_type.PNG)

    assert actual_text == expected_text, f"Heading Text mismatch ! Expected {expected_text} but found {actual_text}"


@allure.title("TC02- Verify Credentials is working or not")
def test_enter_email_and_password(driver):
    click_sign_in_option = driver.find_element(By.LINK_TEXT, "Sign In")
    click_sign_in_option.click()
    time.sleep(5)

    enter_email = driver.find_element(By.XPATH, "//input[@id='username']")
    enter_email.send_keys("augtest_040823@idrive.com")

    enter_password = driver.find_element(By.XPATH, "//input[@id='password']")
    enter_password.send_keys("123456")

    Click_Sign_In_button = driver.find_element(By.XPATH, "//button[@id='frm-btn']")
    Click_Sign_In_button.click()

    time.sleep(30)

    Flag_message = driver.find_element(By.XPATH, "//h5[@class='id-card-title']")

    allure.attach(driver.get_screenshot_as_png(), name="After-login-page", attachment_type=allure.attachment_type.PNG)
    assert Flag_message.text == "Your free trial has expired!", "We get wrong flag message"
