from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from Locator.Locator_OrangeHRM import Locators


class LoginPage:
    def login(self):
        self.driver.get(Locators.url_login)
        wait = WebDriverWait(self.driver, 10)

        try:
            # Locate and fill the username field
            username_field = wait.until(EC.presence_of_element_located((By.NAME, Locators.username_field)))
            username_field.send_keys('Admin')
            time.sleep(1)

            # Locate and fill the password field
            password_field = wait.until(EC.presence_of_element_located((By.NAME, Locators.password_field)))
            password_field.send_keys('admin123')
            time.sleep(1)

            # Locate and click the login button
            login_button = wait.until(EC.element_to_be_clickable((By.XPATH, Locators.login_button)))
            login_button.click()

            # Check for error message
            error_message = wait.until(EC.presence_of_element_located((By.XPATH, Locators.error_message)))
            print("Error Message:", error_message.text)

        except:
            print("Login is successful")
            time.sleep(2)