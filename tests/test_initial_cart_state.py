from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Open Chrome
driver = webdriver.Chrome()

print("1. Opening online shop...")

driver.get("http://localhost:5173/")

time.sleep(2)

cart_link = driver.find_element(
    By.XPATH, "//a[@href='/cart']"
)

cart_link.click()

time.sleep(5)


cart_product = driver.find_element(
    By.XPATH, "//h1[normalize-space()='Your cart is empty']"
)

assert cart_product.is_displayed()

print("TEST PASSED: Initially cart is empty.")
time.sleep(5)
driver.quit()