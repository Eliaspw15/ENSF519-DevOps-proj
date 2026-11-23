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
# -----------------------------------
# TEST DATA
# -----------------------------------

TEST_NAME = "Selenium Test User"
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

time.sleep(1)


print("3. Switching to Sign Up...")

driver.find_element(
    By.XPATH, "//button[text()='Sign Up']"
).click()

time.sleep(1)


print("4. Creating test account...")

# Enter the user's name
driver.find_element(
    By.ID, "name"
).send_keys(TEST_NAME)

# Enter the email
driver.find_element(
    By.ID, "email"
).send_keys(TEST_EMAIL)

# Enter the password
driver.find_element(
    By.ID, "password"
).send_keys(TEST_PASSWORD)

# Click the Sign Up submit button
driver.find_element(
    By.XPATH, "//form//button[@type='submit']"
).click()

time.sleep(2)


# -----------------------------------
# LOG OUT AFTER ACCOUNT CREATION
# -----------------------------------

print("5. Account created. Logging out...")

# Find the logout icon
logout_icon = driver.find_element(
    By.CSS_SELECTOR, "svg[aria-label='Logout']"
)

# The actual clickable button is the parent
# element of the SVG logout icon.
logout_button = logout_icon.find_element(
    By.XPATH, ".."
)

logout_button.click()

time.sleep(2)


# -----------------------------------
# ACTUAL LOGIN TEST
# -----------------------------------

print("6. Opening login page...")

driver.find_element(
    By.LINK_TEXT, "Get Started"
).click()

time.sleep(1)


print("7. Entering login credentials...")

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

logout_icon = driver.find_element(
    By.CSS_SELECTOR, "svg[aria-label='Logout']"
)

assert logout_icon.is_displayed()

print("TEST PASSED: User logged in successfully.")

driver.quit()