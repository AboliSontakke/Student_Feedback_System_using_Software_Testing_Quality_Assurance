from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Function for slow typing
def type_slowly(element, text, delay=0.2):
    for char in text:
        element.send_keys(char)
        time.sleep(delay)

# Setup Chrome
service = Service(ChromeDriverManager().install())
options = Options()
driver = webdriver.Chrome(service=service, options=options)
driver.get("http://localhost/dbms_studentfeedback/index.php")  # admin login page
driver.maximize_window()
wait = WebDriverWait(driver, 10)

try:
    # Admin login
    email_input = wait.until(EC.visibility_of_element_located((By.NAME, "email")))
    type_slowly(email_input, "aboli@admin.com")

    password_input = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
    type_slowly(password_input, "aboli")

    login_btn = wait.until(EC.element_to_be_clickable((By.NAME, "login")))
    time.sleep(1)
    login_btn.click()

    # Open feedback report page (update locator if needed)
    view_feedback_btn = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "View Feedback")))
    time.sleep(1)
    view_feedback_btn.click()

    time.sleep(2)
    print("✅ Admin can view feedback report")
    driver.save_screenshot("admin_report.png")

except Exception as e:
    print("❌ Admin report view failed:", e)

finally:
    driver.quit()
