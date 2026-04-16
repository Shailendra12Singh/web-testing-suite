from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_valid_login(driver):
    url = "https://the-internet.herokuapp.com/login"

    driver.get(url)
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(2)

    print("\nWebsite:", url)
    print("Scenario: Valid Login")
    print("Username: tomsmith")
    print("Password: ********")
    print("Expected: Login Success")

    assert "Secure Area" in driver.page_source


def test_wrong_password(driver):
    url = "https://the-internet.herokuapp.com/login"

    driver.get(url)
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("wrongpass")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(2)

    print("\nWebsite:", url)
    print("Scenario: Wrong Password")
    print("Username: tomsmith")
    print("Password: ********")
    print("Expected: Password Error")

    assert "Your password is invalid!" in driver.page_source


def test_wrong_username(driver):
    url = "https://the-internet.herokuapp.com/login"

    driver.get(url)
    driver.find_element(By.ID, "username").send_keys("wronguser")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(2)

    print("\nWebsite:", url)
    print("Scenario: Wrong Username")
    print("Username: wronguser")
    print("Password: ********")
    print("Expected: Username Error")

    assert "Your username is invalid!" in driver.page_source