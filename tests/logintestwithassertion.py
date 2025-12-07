from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from report_helper import write_result
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

time.sleep(3)


# Assertion: Check page title or URL
if "inventory" in driver.current_url:
    print("Login successful ✅")
    write_result("TC01", "Valid Login","Login","Enter valid id/pwd and click login","standard_user/secret_sauce","Login Successful","Login Successful","PASS")
else:
    print("Login failed ❌")
    write_result("TC01", "Valid Login","Login","Enter valid id/pwd and click login","standard_user/secret_sauce","Login Successful","Login Failed","Failed")

driver.quit()