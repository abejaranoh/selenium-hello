#very first try to test automation

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#open browser
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
time.sleep(3)

# Go to Web page
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(2)

# type username
username_locator = driver.find_element(By.ID, "username")
username_locator.send_keys("student")
time.sleep(2)

# type password
password_locator = driver.find_element(By.NAME, "password")
password_locator.send_keys("Password123")
time.sleep(2)

# push submit button
submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
submit_button_locator.click()
time.sleep(2)

# verifiy url
actual_url = driver.current_url
assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"


# verify text
text_locator = driver.find_element(By.TAG_NAME, "h1")
actual_text = text_locator.text
assert actual_text == "Logged In Successfully"

#verify logout button
log_out_button_locator = driver.find_element(By.LINK_TEXT, "Log out")
assert log_out_button_locator.is_displayed()
