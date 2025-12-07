from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Open Chrome browser
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")

# Wait for 3 seconds
time.sleep(3)

# Close the browser
driver.quit()