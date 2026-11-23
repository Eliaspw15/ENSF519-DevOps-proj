
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

URL = os.getenv("TEST_URL", "http://127.0.0.1:4173")

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

try:
    driver.get(URL)

    WebDriverWait(driver, 15).until(
        lambda d: d.execute_script(
            "return document.readyState"
        ) == "complete"
    )

    assert driver.find_element(
        "tag name", "body"
    ).text.strip(), "Page body is empty"

    print("Selenium test passed!")

finally:
    driver.quit()
