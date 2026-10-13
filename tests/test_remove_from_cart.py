from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

print("1. Opening online shop...")
driver.get("http://localhost:5173/")
time.sleep(2)


print("2. Selecting Wireless Headphones...")

product = driver.find_element(
    By.XPATH, "//*[contains(text(), 'Wireless Headphones')]"
)

product.click()
time.sleep(2)


print("3. Adding Wireless Headphones to cart...")

add_to_cart_button = driver.find_element(
    By.XPATH, "//button[contains(., 'Add to Cart')]"
)

add_to_cart_button.click()
time.sleep(2)


print("4. Opening shopping cart...")

cart_link = driver.find_element(
    By.XPATH, "//a[@href='/cart']"
)

cart_link.click()
time.sleep(2)


print("5. Removing Wireless Headphones from cart...")

remove_button = driver.find_element(
    By.CSS_SELECTOR, "button[aria-label='Remove item']"
)

remove_button.click()
time.sleep(2)

print("6. Verifying the cart is empty...")

page_text = driver.find_element(By.TAG_NAME, "body").text

assert "cart is empty" in page_text.lower()

print("TEST PASSED: Wireless Headphones were successfully removed from the cart.")

driver.quit()