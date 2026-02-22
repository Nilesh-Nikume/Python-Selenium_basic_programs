import time

from selenium import webdriver


def test_open_url():
    driver = webdriver.Chrome()
    driver.get("https://practice.expandtesting.com/")
    driver.maximize_window()
    time.sleep(10)
    # print("page title", driver.title)
    page_title = driver.title
    # assert driver.title == "Automation Testing Practice Website for QA and Developers | UI and API" ,
    assert driver.title == page_title, ("Page title is not match")
    driver.quit()

