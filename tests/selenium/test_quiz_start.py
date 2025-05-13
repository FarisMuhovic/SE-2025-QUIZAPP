from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("http://localhost/quiz-app/frontend/index.html#login")
time.sleep(2)

driver.find_element(By.ID, "email").send_keys("farismuhovic940@gmail.com")
driver.find_element(By.ID, "password").send_keys("faris123")
driver.find_element(By.ID, "password").send_keys(Keys.RETURN)
time.sleep(2)

driver.get("http://localhost/quiz-app/frontend/index.html#quizSearch")
time.sleep(2)

driver.execute_script("window.scrollBy(0, 500);") 
time.sleep(1)

quiz_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "section.quiz-banner:nth-child(2) > a:nth-child(3)"))
)
quiz_link.click()
time.sleep(2)

timer_element = driver.find_element(By.CLASS_NAME, "time")
timer_text = timer_element.text.strip()

assert timer_text != "00:00", "Quiz did not start or timer is zero"

print("Quiz has successfully started with time:", timer_text)

driver.quit()
