from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from Locator.Locator_OrangeHRM import Locators

class Logout:

    def logout(self):

        wait = WebDriverWait(self.driver, 20)
        # Log out of the OrangeHRM application
        try:
            profile_icon = wait.until(EC.presence_of_element_located((By.XPATH,Locators.profile_icon)))
            time.sleep(2)
            profile_icon.click()
            logout_button = wait.until(EC.presence_of_element_located((By.XPATH,Locators.logout_button)))
            time.sleep(2)
            logout_button.click()
            print("Logged out successfully")

        except Exception as e:
            print(f"Failed to log out: {e}")
            self.driver.save_screenshot('logout_error_screenshot.png')  # Save a screenshot for debugging
            raise

