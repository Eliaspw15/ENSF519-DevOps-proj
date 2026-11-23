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


# -----------------------------------
# TEST DATA
# -----------------------------------


TEST_EMAIL = "selenium@test.com"
TEST_PASSWORD = "Test1234!"


# -----------------------------------
# OPEN THE WEBSITE
# -----------------------------------


print("1. Opening website...")
driver.get(os.getenv("TEST_URL", "http://127.0.0.1:4173"))
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