import time
import pdb
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_windows_handler():
    driver = webdriver.Chrome()
    driver.get("https://demo.automationtesting.in/Windows.html")
    # driver.maximize_window()
    # print(driver.title)

    # pdb.set_trace()
    driver.find_element(By.XPATH,
                        "//a[@target='_blank']/button[@class='btn btn-info' and normalize-space() = 'click']").click()
    time.sleep(5)
    select_window = driver.window_handles
    print("Total windows", list(select_window))

    for windows in select_window:
        driver.switch_to.window(windows)
        print(driver.title)
        driver.switch_to.window(select_window[0])
    # print(driver.title)

    # driver.switch_to.window(select_window[1])
    # print(driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/h3[1]").text)
    #
    #
    # driver.switch_to.window(select_window[0])
    # print(driver.find_element(By.XPATH, "//*[normalize-space()='Opening a new window']").text)
    #
    driver.quit()
