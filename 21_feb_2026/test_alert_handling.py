import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import pdb

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.maximize_window()
    yield driver
    driver.quit()

    pdb.set_trace()
def test_alert(driver):
    driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()


