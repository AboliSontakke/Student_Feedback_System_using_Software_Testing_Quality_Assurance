from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Function for slow typing (optional for textarea)
def type_slowly(element, text, delay=0.2):
    for char in text:
        element.send_keys(char)
        time.sleep(delay)

# Function to click with small delay
def click_slowly(element, delay=0.3):
    element.click()
    time.sleep(delay)

# Setup Chrome
service = Service(ChromeDriverManager().install())
options = Options()
driver = webdriver.Chrome(service=service, options=options)
driver.get("http://localhost/dbms_studentfeedback/index.php")
wait = WebDriverWait(driver, 20)

try:
    driver.maximize_window()
    print("🔹 Filling the feedback form ...")

    # Fill select inputs
    selects = {
        "roll": "11",
        "year": "2024",
        "sem": "6th",
        "branch": "CSE",
        "section": "A",
        "subject": "OOPS"
    }
    for name, value in selects.items():
        select_elem = wait.until(EC.presence_of_element_located((By.NAME, name)))
        for option in select_elem.find_elements(By.TAG_NAME, 'option'):
            if option.get_attribute('value') == value:
                click_slowly(option)
                break

    # Fill date
    date_elem = wait.until(EC.presence_of_element_located((By.NAME, "date")))
    type_slowly(date_elem, "2025-10-13")

    # Fill radio buttons
    radios = {
        "ques1": "5",
        "ques-2i": "5",
        "ques-2ii": "4",
        "ques-2iii": "5",
        "ques-2iv": "4",
        "ques-2v": "5",
        "ques3": "5",
        "ques4": "4"
    }

    for name, value in radios.items():
        radio_elem = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, f'input[name="{name}"][value="{value}"]')
        ))
        click_slowly(radio_elem)

    # Fill textarea
    remarks_elem = wait.until(EC.presence_of_element_located((By.NAME, "remarks")))
    type_slowly(remarks_elem, "Great teaching and well explained!", delay=0.15)

#     # Click Submit
    submit_btn = wait.until(EC.element_to_be_clickable((By.NAME, "submit")))
    click_slowly(submit_btn)
    print("✅ Feedback submitted successfully!")

    # Screenshot
    driver.save_screenshot("feedback_submission.png")
    print("✅ Screenshot saved")

except Exception as e:
    print("❌ Feedback submission failed:", e)

finally:
    print("🔹 Closing browser...")
    driver.quit()
