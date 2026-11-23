from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome(options=options)
# Open Chrome

print("1. Opening online shop...")

driver.get(os.getenv("TEST_URL", "http://127.0.0.1:4173"))

time.sleep(2)

cart_link = driver.find_element(
    By.XPATH, "//a[@href='/cart']"
)

cart_link.click()
print("2. Going to Cart page")
time.sleep(5)


cart_product = driver.find_element(
    By.XPATH, "//h1[normalize-space()='Your cart is empty']"
)

assert cart_product.is_displayed()

print("TEST PASSED: Initially cart is empty.")
time.sleep(5)
driver.quit()