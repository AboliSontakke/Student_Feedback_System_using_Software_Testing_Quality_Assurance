# =====================================
# IMPORTS
# =====================================
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
    """Abstract Base Class for all page objects"""

    def __init__(self, driver, wait):
        self._driver = driver        # Protected member
        self._wait = wait

    @abstractmethod
    def is_loaded(self):
        """Each page must define its own load verification"""
        pass


# =====================================
# ENCAPSULATION — Login Page Class
# =====================================
class LoginPage(BasePage):
    """Page Object for Login functionality"""

    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        # Private locators (Encapsulation)
        self.__email_field = (By.NAME, "email")
        self.__password_field = (By.NAME, "password")
        self.__login_button = (By.NAME, "login")

    def __type_slowly(self, element, text, delay=0.2):
        """Private helper method to simulate slow typing"""
        for char in text:
            element.send_keys(char)
            time.sleep(delay)

    def is_loaded(self):
        """Verify page is loaded"""
        return self._wait.until(EC.visibility_of_element_located(self.__email_field))

    # POLYMORPHISM — method can be redefined for different user types
    def login(self, email, password):
        """Perform login action"""
        print("Logging in as a general user...")
        email_input = self._wait.until(EC.visibility_of_element_located(self.__email_field))
        self.__type_slowly(email_input, email)

        password_input = self._wait.until(EC.visibility_of_element_located(self.__password_field))
        self.__type_slowly(password_input, password)

        login_btn = self._wait.until(EC.element_to_be_clickable(self.__login_button))
        login_btn.click()
        time.sleep(2)


# =====================================
# POLYMORPHISM — Admin Page (Overrides Login)
# =====================================
class AdminLoginPage(LoginPage):
    """Specialized Login for Admin"""

    def login(self, email, password):
        print("Logging in as Admin...")
        super().login(email, password)  # Call parent method


# =====================================
# BASE TEST CLASS — INHERITANCE
# =====================================
class BaseTest:
    """Handles WebDriver setup and teardown"""

    def __init__(self):
        service = Service(ChromeDriverManager().install())
        options = Options()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=service, options=options)
        self.wait = WebDriverWait(self.driver, 10)

    def open_url(self, url):
        """Open given URL"""
        self.driver.get(url)

    def close_browser(self):
        """Close the browser"""
        self.driver.quit()


# =====================================
# TEST CLASS — Inherits from BaseTest
# =====================================
class TestLogin(BaseTest):
    """Test case class implementing login test"""

    # OVERRIDING (POLYMORPHISM)
    def open_url(self, url="http://localhost/dbms_studentfeedback/index.php"):
        print(f"Opening test URL: {url}")
        super().open_url(url)

    def test_admin_login(self):
        """Test case to verify Admin login"""
        self.open_url()  # overridden method
        login_page = AdminLoginPage(self.driver, self.wait)

        try:
            login_page.is_loaded()
            login_page.login("aboli@admin.com", "aboli")
            print("✅ Admin login test passed.")
        except Exception as e:
            print("❌ Login test failed:", e)
        finally:
            self.close_browser()


# =====================================
# MAIN EXECUTION
# =====================================
if __name__ == "__main__":
    test = TestLogin()
    test.test_admin_login()
