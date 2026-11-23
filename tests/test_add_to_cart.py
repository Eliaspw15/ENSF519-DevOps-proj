from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


# Open Chrome
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)

print("1. Opening online shop...")

driver.get(os.getenv("TEST_URL", "http://127.0.0.1:4173"))

time.sleep(2)


# Find the product
print("2. Finding Wireless Headphones...")

product = driver.find_element(
    By.XPATH, "//*[contains(text(), 'Wireless Headphones')]"
)


# Click the product
print("3. Clicking Wireless Headphones...")

product.click()

time.sleep(2)

print("4. Adding Wireless Headphones to cart...")

add_to_cart_button = driver.find_element(
    By.XPATH, "//button[contains(., 'Add to Cart')]"
)

add_to_cart_button.click()

time.sleep(2)


cart_link = driver.find_element(
    By.XPATH, "//a[@href='/cart']"
)

cart_link.click()

time.sleep(2)


cart_product = driver.find_element(
    By.XPATH, "//*[contains(text(), 'Wireless Headphones')]"
)

assert cart_product.is_displayed()

print("TEST PASSED: Wireless Headphones were successfully added to the cart.")

driver.quit()