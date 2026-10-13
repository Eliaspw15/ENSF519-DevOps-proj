from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


TEST_NAME = "Selenium Checkout User"
TEST_EMAIL = "checkout@test.com"
TEST_PASSWORD = "Test1234!"

driver = webdriver.Chrome()


print("1. Opening online shop...")
driver.get("http://localhost:5173/")
time.sleep(2)


print("2. Opening authentication page...")
driver.find_element(By.LINK_TEXT, "Get Started").click()
time.sleep(1)

print("3. Switching to Sign Up...")

sign_up_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[text()='Sign Up']")
    )
)

driver.execute_script(
    "arguments[0].scrollIntoView({block: 'center'});",
    sign_up_button
)

time.sleep(1)
sign_up_button.click()

time.sleep(1)


print("4. Creating test account...")

driver.find_element(By.ID, "name").send_keys(TEST_NAME)
driver.find_element(By.ID, "email").send_keys(TEST_EMAIL)
driver.find_element(By.ID, "password").send_keys(TEST_PASSWORD)

driver.find_element(
    By.XPATH, "//form//button[@type='submit']"
).click()

time.sleep(2)


print("5. Selecting Wireless Headphones...")

product = driver.find_element(
    By.XPATH, "//*[contains(text(), 'Wireless Headphones')]"
)

product.click()
time.sleep(2)


print("6. Adding Wireless Headphones to cart...")

driver.find_element(
    By.XPATH, "//button[contains(., 'Add to Cart')]"
).click()

time.sleep(2)


print("7. Opening shopping cart...")

driver.find_element(
    By.XPATH, "//a[@href='/cart']"
).click()

time.sleep(2)


print("8. Proceeding to checkout...")

checkout_link = driver.find_element(
    By.XPATH, "//a[@href='/checkout']"
)

checkout_link.click()
time.sleep(2)

print("9. Filling in checkout information...")

driver.find_element(By.ID, "address").send_keys(
    "123 Test Street, Calgary, AB"
)

driver.find_element(By.ID, "phone").send_keys(
    "4035551234"
)

driver.find_element(By.ID, "notes").send_keys(
    "Selenium automated checkout test."
)

time.sleep(2)

print("10. Placing the order...")

place_order_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(., 'Place Order')]")
    )
)

driver.execute_script(
    "arguments[0].scrollIntoView({block: 'center'});",
    place_order_button
)

time.sleep(1)

place_order_button.click()

time.sleep(2)

print("11. Verifying order completion...")

page_text = driver.find_element(By.TAG_NAME, "body").text

assert "order complete" in page_text.lower()

print("TEST PASSED: Checkout completed and order was placed successfully.")

driver.quit()