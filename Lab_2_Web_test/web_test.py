from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Selenium WebDriver
driver = webdriver.Chrome()
driver.accept_untrusted_certs = True

# Відкриваємо веб-сторінку
driver.get('https://uk.wikipedia.org')

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, 'searchInput')))

# Test 1: Перевірка заголовка головної сторінки
assert "Вікіпедія" in driver.title
print("Test 1 passed!")

# Test 2: Перевірка наявності поля пошуку
search_box = wait.until(EC.visibility_of_element_located((By.ID, "searchInput")))
assert search_box.is_displayed()
print("Test 2 passed!")

# Test 3: Виконання пошуку і перевірка результатів
search_box.send_keys("Київ")
search_box.submit()
wait.until(EC.title_contains("Київ"))
assert "Київ" in driver.title
print("Test 3 passed!")

# Test 4: Клікнути на посилання "Обговорення" у хедері
community_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Обговорення")))
community_link.click()
assert "Обговорення" in driver.title
print("Test 4 passed!")

# Test 5: Перевірка наявності посилання "Проект" у футері сторінки
footer_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Розробники")))
assert footer_link.is_displayed()
print("Test 5 passed!")
# Закриваємо веб-драйвер
driver.quit()
