import time

import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()
    yield driver
    driver.quit()


def test_open_url(driver):
    # make_appointment_button = driver.find_element(By.ID, "btn-make-appointment") # find element by ID

    # find element by LINK_TEXT
    ''' <a id="btn-make-appointment"
    href="./profile.php#login"
    class="btn btn-dark btn-lg">
    Make Appointment</a>'''
    ''' 1. it work only with anchor tag (a)
        2. if multiple link available then it take first one'''

    make_appointment_button = driver.find_element(By.LINK_TEXT, "Make Appointment")
    make_appointment_button.click()

    # find element by Name
    Enter_UserName = driver.find_element(By.NAME, "username")
    Enter_UserName.send_keys("admin") # Enter the text in text box

    Enter_Password = driver.find_element(By.NAME, "password")
    Enter_Password.send_keys("admin") # Enter the text in text box

    # find element by Xpath
    Click_Login_Button = driver.find_element(By.XPATH, "//button[@id='btn-login']")
    Click_Login_Button.click()
    time.sleep(5)