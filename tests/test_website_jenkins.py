from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
options = Options()
# Required/recommended for headless CI environments
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)
# Website running locally on the Jenkins server
url = os.getenv("TEST_URL", "http://127.0.0.1:4173")
try:
    driver.get(url)

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
