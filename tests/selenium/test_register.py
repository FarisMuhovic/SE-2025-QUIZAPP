from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import random

driver = webdriver.Chrome()
driver.get("http://localhost/quiz-app/frontend/index.html#register")  

time.sleep(2)

random_email = f"testuser{random.randint(1000, 9999)}@example.com"

driver.find_element(By.ID, "firstName").send_keys("Test")
driver.find_element(By.ID, "lastName").send_keys("User")
driver.find_element(By.ID, "email").send_keys(random_email)
driver.find_element(By.ID, "password").send_keys("test1234")

select = Select(driver.find_element(By.ID, "userType"))
select.select_by_value("student")

driver.find_element(By.CLASS_NAME, "form-submit-btn").click()

time.sleep(3)

assert "login" in driver.current_url.lower() or "success" in driver.page_source.lower()

driver.quit()
