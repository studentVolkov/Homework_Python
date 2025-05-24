import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    return driver


def test_fill_and_submit_form(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    driver.find_element(By.CSS_SELECTOR, "input[name=first-name]").send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR, "input[name=last-name]").send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR, "input[name=address").send_keys("Ленина, 55-3")
    driver.find_element(By.CSS_SELECTOR, "input[name=e-mail]").send_keys("test@skypro.com")
    driver.find_element(By.CSS_SELECTOR, "input[name=phone]").send_keys("+7985899998787")
    driver.find_element(By.CSS_SELECTOR, "input[name=zip-code]").send_keys("")
    driver.find_element(By.CSS_SELECTOR, "input[name=city]").send_keys("Москва")
    driver.find_element(By.CSS_SELECTOR, "input[name=country]").send_keys("Россия")
    driver.find_element(By.CSS_SELECTOR, "input[name=job-position]").send_keys("QA")
    driver.find_element(By.CSS_SELECTOR, "input[name=company]").send_keys("SkyPro")

    submit_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn.btn-outline-primary.mt-3"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    driver.execute_script("arguments[0].click();", submit_button)

    zip_code_field = driver.find_element(By.CSS_SELECTOR, "div#zip-code")
    assert "alert-danger" in zip_code_field.get_attribute("class")

    green_highlighted_fields = driver.find_elements(By.CSS_SELECTOR, "div.alert.py-2.alert-success")
    assert len(green_highlighted_fields)

    driver.quit()
