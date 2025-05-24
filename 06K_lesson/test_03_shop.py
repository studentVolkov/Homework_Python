import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    return driver

def test_shop(driver):
    driver.get("https://www.saucedemo.com/")
    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")
    login_button.click()

    backpack_add_button = driver.find_element(By.XPATH,"//div[@class='inventory_item' and .//div[contains(text(), 'Sauce Labs Backpack')]]//button")
    tshirt_add_button = driver.find_element(By.XPATH,"//div[@class='inventory_item' and .//div[contains(text(), 'Sauce Labs Bolt T-Shirt')]]//button")
    onesie_add_button = driver.find_element(By.XPATH,"//div[@class='inventory_item' and .//div[contains(text(), 'Sauce Labs Onesie')]]//button")

    backpack_add_button.click()
    tshirt_add_button.click()
    onesie_add_button.click()

    cart_link = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_link.click()

    checkout_button = driver.find_element(By.ID, "checkout")
    checkout_button.click()

    first_name_field = driver.find_element(By.CSS_SELECTOR, "#first-name")
    first_name_field.send_keys('Sergei')
    last_name_field = driver.find_element(By.CSS_SELECTOR, "#last-name")
    last_name_field.send_keys('Volkov')
    postal_code_field = driver.find_element(By.CSS_SELECTOR, "#postal-code")
    postal_code_field.send_keys('12345')

    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()

    total = driver.find_element(By.CSS_SELECTOR, 'div.summary_total_label').text
    print(total)
    assert total == 'Total: $58.29'
    driver.quit()
