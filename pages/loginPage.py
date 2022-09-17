from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as con

import chromedriver_autoinstaller

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()


def open_login_screen(url):
    driver.get(url)
    driver.maximize_window()


def login_function(name, password):
    element = driver.find_element(By.ID, "user-name")
    element.click()
    element.send_keys(Keys.CONTROL, "a", Keys.BACKSPACE)
    element.send_keys(name)
    element = driver.find_element(By.ID, "password")
    element.click()
    element.send_keys(Keys.CONTROL, "a", Keys.BACKSPACE)
    element.send_keys(password)
    element = driver.find_element(By.ID, "login-button")
    wait = WebDriverWait(driver, 10).until(con.element_to_be_clickable(element))
    wait.click()


def validate_login(title):
    get_title = driver.title
    driver.close()
    return title in get_title


