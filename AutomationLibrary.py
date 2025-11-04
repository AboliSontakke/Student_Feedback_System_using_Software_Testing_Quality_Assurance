from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


def type_slowly(self, element, text, delay=0.2):
    element.clear()  # <-- clear any existing text
    for char in text:
        element.send_keys(char)
        time.sleep(delay)

class AutomationLibrary:
    ROBOT_LIBRARY_SCOPE = "TEST SUITE"

    def type_slowly(self, element, text, delay=0.2):
        for char in text:
            element.send_keys(char)
            time.sleep(delay)

    def admin_login(self, email, password):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=Options())
        self.driver.get("http://localhost/dbms_studentfeedback/index.php")
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 10)

        try:
            email_input = wait.until(EC.visibility_of_element_located((By.NAME, "email")))
            self.type_slowly(email_input, email)

            password_input = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
            self.type_slowly(password_input, password)

            login_btn = wait.until(EC.element_to_be_clickable((By.NAME, "login")))
            time.sleep(1)
            login_btn.click()

            time.sleep(2)
            return True
        except Exception as e:
            print("❌ Admin login failed:", e)
            return False

    def signup_user(self, email, first_name, last_name, password):
        self.driver.get("http://localhost/dbms_studentfeedback/index.php")  # same page
        wait = WebDriverWait(self.driver, 10)

        try:
            email_input = wait.until(EC.visibility_of_element_located((By.NAME, "email")))
            self.type_slowly(email_input, email)

            first_input = wait.until(EC.visibility_of_element_located((By.NAME, "first_name")))
            self.type_slowly(first_input, first_name)

            last_input = wait.until(EC.visibility_of_element_located((By.NAME, "last_name")))
            self.type_slowly(last_input, last_name)

            password_input = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
            self.type_slowly(password_input, password)

            submit_btn = wait.until(EC.element_to_be_clickable((By.NAME, "submit")))
            submit_btn.click()
            time.sleep(2)
            return True
        except Exception as e:
            print("❌ Signup failed:", e)
            return False

    def close_browser(self):
        try:
            self.driver.quit()
        except:
            pass
