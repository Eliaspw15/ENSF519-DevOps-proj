from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# -----------------------------------
# TEST DATA
# -----------------------------------


TEST_EMAIL = "selenium@test.com"
TEST_PASSWORD = "Test1234!"


# -----------------------------------
# OPEN THE WEBSITE
# -----------------------------------

driver = webdriver.Chrome()

print("1. Opening website...")
driver.get("http://localhost:5173/")
time.sleep(2)


# -----------------------------------
# SETUP: CREATE A TEST ACCOUNT
# -----------------------------------

print("2. Opening authentication page...")

driver.find_element(
    By.LINK_TEXT, "Get Started"
).click()

time.sleep(5)

print("4. Signing in with invalid account...")

driver.find_element(
    By.ID, "email"
).send_keys(TEST_EMAIL)

driver.find_element(
    By.ID, "password"
).send_keys(TEST_PASSWORD)


print("8. Clicking Log In...")

driver.find_element(
    By.XPATH, "//form//button[@type='submit']"
).click()

time.sleep(2)

print("9. Checking whether login was successful...")
logout_icons = driver.find_elements(
    By.CSS_SELECTOR, "svg[aria-label='Logout']"
)

assert not logout_icons, "Login unexpectedly succeeded."

assert "Invalid email or password." in driver.find_element(
    By.TAG_NAME, "body"
).text, "Expected login error was not shown."

print("TEST PASSED: Invalid credentials were rejected.")
time.sleep(5)
driver.quit()