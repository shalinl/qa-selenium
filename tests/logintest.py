from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Open browser
driver = webdriver.Chrome()

# Go to login page
driver.get("https://www.saucedemo.com/")

# Enter username
driver.find_element(By.ID, "user-name").send_keys("$$$$$")

# Enter password
driver.find_element(By.ID, "password").send_keys("")

# Click login button
driver.find_element(By.ID, "login-button").click()

# Wait 3 seconds to see result
time.sleep(3)

# Close browser
driver.quit()