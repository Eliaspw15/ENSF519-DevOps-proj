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


try:
    print("1. Opening online shop")
    driver.get(os.getenv("TEST_URL", "http://127.0.0.1:4173"))
    time.sleep(2)

    assert driver.find_element(By.TAG_NAME, "html").get_attribute("data-theme") == "light"

    print("2. Clicking the header theme button to switch to dark mode...")
    driver.find_element(
        By.CSS_SELECTOR, "button[aria-label='Switch to Light mode']"
    ).click()
    time.sleep(2)


    assert driver.find_element(By.TAG_NAME, "html").get_attribute("data-theme") == "light"
    assert driver.execute_script("return localStorage.getItem('ebx-theme');") == "light"
    print("TEST PASSED: Header theme button switched to light mode.")

    print("3. Refreshing to verify light mode is saved...")
    driver.refresh()
    time.sleep(2)

    assert driver.find_element(By.TAG_NAME, "html").get_attribute("data-theme") == "light"
    print("TEST PASSED: Light mode remained selected after refreshing.")
    
    print("4. Clicking the header theme button to switch to dark mode...")
    driver.find_element(
        By.CSS_SELECTOR, "header button[aria-label='Switch to Dark mode']"
    ).click()
    time.sleep(2)

    assert driver.find_element(By.TAG_NAME, "html").get_attribute("data-theme") == "dark"
    assert driver.execute_script("return localStorage.getItem('ebx-theme');") == "dark"
    print("TEST PASSED: Header theme button switched to dark mode.")

    print("5. Refreshing to verify dark mode is saved...")
    driver.refresh()
    time.sleep(2)
    
    assert driver.find_element(By.TAG_NAME, "html").get_attribute("data-theme") == "dark"
    print("TEST PASSED: Dark mode remained selected after refreshing.")

    print("ALL TESTS PASSED!")
except Exception as error:
    print(f"TEST FAILED: {type(error).__name__}: {error}")
    raise
finally:
    driver.quit()
