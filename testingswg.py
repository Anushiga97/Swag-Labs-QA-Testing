import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.saucedemo.com/inventory.html")
driver.maximize_window()

username = "standard_user"
password = "secret_sauce"
login_url = "https://www.saucedemo.com/inventory.html"
driver.get(login_url)

username_field = driver.find_element(By.ID,value="user-name")
password_field = driver.find_element(By.ID,value="password")
login_button = driver.find_element(By.ID, 'login-button')
username_field.send_keys('standard_user')
password_field.send_keys('secret_sauce')
login_button.click()

reset_app_state_button = driver.find_element(By.ID, 'reset_sidebar_link')
reset_app_state_button.click()

element_after_reset = driver.find_element(By.ID, 'element_after_reset')
expected_state = 'default'
actual_state = element_after_reset.text

if expected_state == actual_state:
    print('Test Passed: The application state was successfully reset.')
else:
    print('Test Failed: The application state was not reset.')


print(" Error ")



time.sleep(7)
driver.close()
driver.quit()

print("done")

