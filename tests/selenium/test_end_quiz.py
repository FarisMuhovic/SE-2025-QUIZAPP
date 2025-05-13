from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

driver = webdriver.Chrome()

# Step 1: Log in
driver.get("http://localhost/quiz-app/frontend/index.html#login")
time.sleep(2)

driver.find_element(By.ID, "email").send_keys("farismuhovic940@gmail.com")
driver.find_element(By.ID, "password").send_keys("faris123")
driver.find_element(By.ID, "password").send_keys(Keys.RETURN)
time.sleep(2)

# Step 2: Navigate to quiz search
driver.get("http://localhost/quiz-app/frontend/index.html#quizSearch")
time.sleep(2)

# Scroll down to make quiz link clickable
driver.execute_script("window.scrollBy(0, 500);") 
time.sleep(1)

# Step 3: Click the quiz
quiz_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "section.quiz-banner:nth-child(2) > a:nth-child(3)"))
)
quiz_link.click()
time.sleep(2)

# Step 4: Select the answer for the first question
answer_input = driver.find_element(By.CSS_SELECTOR, "section.question:nth-child(1) > div:nth-child(2) > label:nth-child(1) > input:nth-child(1)")
answer_input.click()
time.sleep(2)
driver.execute_script("window.scrollBy(0, 55500);") 
time.sleep(2)
# Step 6: Click the submit button after completing the quiz
submit_button = driver.find_element(By.CSS_SELECTOR, "#questions-container-form > button:nth-child(11)")
submit_button.click()
time.sleep(2)

# Step 7: Verify the result (score) on the page
result_text = driver.page_source  # Get the full page source

# Verify if the result contains the score, e.g., "Score: 1/10 (10%)"
assert "Score: 1/10" in result_text, f"Expected score 'Score: 1/10', but got: {result_text}"

print("Quiz submitted successfully and score verified!")

driver.quit()
