# ========================================================
# FEEDBACK FORM AUTOMATION - OOP BASED SELENIUM FRAMEWORK
# ========================================================
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from abc import ABC, abstractmethod
import time


# =====================================
# ABSTRACTION — Base Page Interface
# =====================================
class BasePage(ABC):
    """Abstract class for all page objects"""

    def __init__(self, driver, wait):
        self._driver = driver  # protected
        self._wait = wait

    @abstractmethod
    def is_loaded(self):
        """Check if page is loaded"""
        pass


# =====================================
# ENCAPSULATION — Feedback Form Page
# =====================================
class FeedbackPage(BasePage):
    """Page Object for Feedback Form"""

    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        # Private element locators
        self.__date_field = (By.NAME, "date")
        self.__remarks_field = (By.NAME, "remarks")
        self.__submit_button = (By.NAME, "submit")

    # Helper methods (private)
    def __type_slowly(self, element, text, delay=0.2):
        for char in text:
            element.send_keys(char)
            time.sleep(delay)

    def __click_slowly(self, element, delay=0.3):
        element.click()
        time.sleep(delay)

    # Page verification
    def is_loaded(self):
        return self._wait.until(EC.presence_of_element_located(self.__date_field))

    # Fill select dropdowns
    def fill_dropdowns(self, selects):
        for name, value in selects.items():
            select_elem = self._wait.until(EC.presence_of_element_located((By.NAME, name)))
            for option in select_elem.find_elements(By.TAG_NAME, 'option'):
                if option.get_attribute('value') == value:
                    self.__click_slowly(option)
                    break

    # Fill date field
    def fill_date(self, date_value):
        date_elem = self._wait.until(EC.presence_of_element_located(self.__date_field))
        self.__type_slowly(date_elem, date_value)

    # Fill radio buttons
    def fill_radio_buttons(self, radios):
        for name, value in radios.items():
            radio_elem = self._wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, f'input[name="{name}"][value="{value}"]')
            ))
            self.__click_slowly(radio_elem)

    # Fill remarks
    def fill_remarks(self, text):
        remarks_elem = self._wait.until(EC.presence_of_element_located(self.__remarks_field))
        self.__type_slowly(remarks_elem, text, delay=0.15)

    # Submit form
    def submit_form(self):
        submit_btn = self._wait.until(EC.element_to_be_clickable(self.__submit_button))
        self.__click_slowly(submit_btn)
        print("✅ Feedback submitted successfully!")


# =====================================
# BASE TEST CLASS (INHERITANCE)
# =====================================
class BaseTest:
    """Handles driver setup and teardown"""

    def __init__(self):
        service = Service(ChromeDriverManager().install())
        options = Options()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=service, options=options)
        self.wait = WebDriverWait(self.driver, 20)

    def open_url(self, url):
        self.driver.get(url)

    def take_screenshot(self, name="screenshot.png"):
        self.driver.save_screenshot(name)
        print(f"✅ Screenshot saved as {name}")

    def close_browser(self):
        self.driver.quit()


# =====================================
# POLYMORPHISM — Specialized Feedback Test
# =====================================
class FeedbackTest(BaseTest):
    """Test case for Feedback submission"""

    # Overriding open_url() method (Polymorphism)
    def open_url(self, url="http://localhost/dbms_studentfeedback/index.php"):
        print(f"🔹 Opening Feedback Page: {url}")
        super().open_url(url)

    def test_feedback_submission(self):
        """Main test for submitting feedback form"""
        self.open_url()
        feedback_page = FeedbackPage(self.driver, self.wait)

        try:
            feedback_page.is_loaded()
            print("🔹 Filling the feedback form...")

            # Fill all fields
            selects = {
                "roll": "11",
                "year": "2024",
                "sem": "6th",
                "branch": "CSE",
                "section": "A",
                "subject": "OOPS"
            }
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

            feedback_page.fill_dropdowns(selects)
            feedback_page.fill_date("2025-10-13")
            feedback_page.fill_radio_buttons(radios)
            feedback_page.fill_remarks("Great teaching and well explained!")
            feedback_page.submit_form()

            # Take screenshot
            self.take_screenshot("feedback_submission.png")

        except Exception as e:
            print("❌ Feedback submission failed:", e)
        finally:
            print("🔹 Closing browser...")
            self.close_browser()


# =====================================
# MAIN EXECUTION
# =====================================
if __name__ == "__main__":
    test = FeedbackTest()
    test.test_feedback_submission()
