import time
import allure
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def driver():
    chrome_options = Options()
    # Disable password manager popup
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }

    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Verify URL")
@allure.description("TC#1 Check Verify and Login functionality")
@pytest.mark.smoketest
def test_open_url(driver):
    # make_appointment_button = driver.find_element(By.ID, "btn-make-appointment") # find element by ID

    # find element by LINK_TEXT
    ''' <a id="btn-make-appointment"
    href="./profile.php#login"
    class="btn btn-dark btn-lg">
    Make Appointment</a>'''
    ''' 1. it work only with anchor tag (a)
        2. if multiple link available then it take first one'''

    # make_appointment_button = driver.find_element(By.LINK_TEXT, "Make Appointment")

    # find element by PARTIAL_LINK_TEXT
    ''' <a id="btn-make-appointment"
    href="./profile.php#login"
    class="btn btn-dark btn-lg">
    Make Appointment</a>'''
    ''' 1. it work only with anchor tag (a)
        2. if multiple link available then it take first one
        3. It work for Appointment
        4. It work for Make
        5. It work for Appointment
        6. It work for App
        7. It work for ment'''

    # make_appointment_button = driver.find_element(By.PARTIAL_LINK_TEXT, "point")
    # by Tag_Name
    list_of_tag_a = driver.find_elements(By.TAG_NAME, "a")
    make_appointment_button = list_of_tag_a[5]  # make appointment button with tag a at 5th position
    make_appointment_button.click()
    # print(driver.current_url)
    allure.attach(driver.get_screenshot_as_png(),name="appointment-Screenshot", attachment_type= "Attachment.png")
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login", "Error 01 Login URL not match"

    # find element by Name
    Enter_UserName = driver.find_element(By.NAME, "username")
    Enter_UserName.send_keys("John Doe")  # Enter the text in text box

    Enter_Password = driver.find_element(By.NAME, "password")
    Enter_Password.send_keys("ThisIsNotAPassword")  # Enter the text in text box
    allure.attach(driver.get_screenshot_as_png(),name="appointment-Screenshot", attachment_type= "Attachment.png")

    # find element by Xpath
    Click_Login_Button = driver.find_element(By.XPATH, "//button[@id='btn-login']")
    Click_Login_Button.click()
    time.sleep(5)
    print(driver.current_url)

    allure.attach(driver.get_screenshot_as_png(),name="appointment-Screenshot", attachment_type= "Attachment.png")

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment", ("Error 02 After Login URL "
                                                                                          "not"
                                                                                          "match")
    time.sleep(5)
