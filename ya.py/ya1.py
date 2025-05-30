# зайти на лабиринт
# найти книги по Phython
# Собрать все карточки товара
# вывести в консоль информацию ; название, автор , цена

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
# Зайти на сайт лабиринт
driver.get("https://www.labirint.ru/")

search_locator = "#search-field"
search_input = driver.find_element(By.CSS_SELECTOR, search_locator)
search_input.send_keys("Python")
search_input.send_keys(Keys.RETURN)

book_locator = "div.product"
books = driver.find_elements(By.CSS_SELECTOR, "div.product")
print(len(books))




