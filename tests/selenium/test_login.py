from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://localhost/quiz-app/frontend/index.html#login")

time.sleep(2)

email_input = driver.find_element(By.ID, "email")
password_input = driver.find_element(By.ID, "password")

email_input.send_keys("farismuhovic940@gmail.com")
password_input.send_keys("faris123")
password_input.send_keys(Keys.RETURN)

time.sleep(2)

assert "Dashboard" in driver.page_source or "/dashboard" in driver.current_url

driver.quit()
