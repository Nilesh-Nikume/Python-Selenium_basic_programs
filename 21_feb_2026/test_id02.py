import time
from selenium.webdriver.common.by import By
from selenium import webdriver


def test_open_url():
    driver = webdriver.Chrome()
    driver.get("https://practice.expandtesting.com/")
    driver.maximize_window()

    # print("page title", driver.title)
    page_title = driver.title
    # assert driver.title == "Automation Testing Practice Website for QA and Developers | UI and API" ,
    assert driver.title == page_title, "Page title is not match"
    # driver.find_element(By.XPATH, "(//a[normalize-space()='Xpath / Css'])[1]").click()
    driver.find_element(By.XPATH, "//*[@class='btn btn-success py-sm-2 px-sm-3 rounded-pill']").click()
    time.sleep(10)
    driver.quit()

