import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://practice.expandtesting.com/")
    driver.maximize_window()
    yield driver
    driver.quit()


def test_go_to_locator_page(driver):
    wait = WebDriverWait(driver, 10)
    # driver.find_element(By.XPATH, "(//a[normalize-space()='Xpath / Css'])[1]").click()
    # driver.find_element(By.XPATH, "//*[text() = 'Xpath / Css']").click()
    # Locator_page = wait.until(EC.presence_of_element_located(By.XPATH, "//*[text()='Locators Page']"))
    Locator_page = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[text()='Locators Page']")
        )
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", Locator_page)
    Locator_page.click()

    try:
        popup_close = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='dismiss-button']/div/span"))
        )
        popup_close.click()
    except:
        print("Popup did not appear")

    drop_down = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='countrySelect']")))
    driver.execute_script("arguments[0].scrollIntoView(true);", drop_down)

    drop_down.click()
    countries = driver.find_elements(By.XPATH, "//*[@id='countrySelect']")
    country = []
    for c in countries:
        country.append(c.text)
        print("Country ares-->",country)
        # c.text
