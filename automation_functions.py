from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def type_slowly(element, text, delay=0.2):
    for char in text:
        element.send_keys(char)
        time.sleep(delay)

def admin_login(email, password):
    service = Service(ChromeDriverManager().install())
    options = Options()
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("http://localhost/dbms_studentfeedback/index.php")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    
    try:
        email_input = wait.until(EC.visibility_of_element_located((By.NAME, "email")))
        type_slowly(email_input, email)

        password_input = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
        type_slowly(password_input, password)

        login_btn = wait.until(EC.element_to_be_clickable((By.NAME, "login")))
        time.sleep(1)
        login_btn.click()

        time.sleep(2)
        print("✅ Admin login successful")
        return True
    except Exception as e:
        print("❌ Admin login failed:", e)
        return False
    finally:
        driver.quit()

def signup_user(email, first_name, last_name, password):
    service = Service(ChromeDriverManager().install())
    options = Options()
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("http://localhost/dbms_studentfeedback/index.php")  # signup handled in same page
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    
    try:
        email_input = wait.until(EC.visibility_of_element_located((By.NAME, "email")))
        type_slowly(email_input, email)
        
        first_input = wait.until(EC.visibility_of_element_located((By.NAME, "first_name")))
        type_slowly(first_input, first_name)

        last_input = wait.until(EC.visibility_of_element_located((By.NAME, "last_name")))
        type_slowly(last_input, last_name)

        password_input = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
        type_slowly(password_input, password)

        submit_btn = wait.until(EC.element_to_be_clickable((By.NAME, "submit")))
        submit_btn.click()
        
        time.sleep(2)
        print("✅ Signup successful")
        return True
    except Exception as e:
        print("❌ Signup failed:", e)
        return False
    finally:
        driver.quit()
