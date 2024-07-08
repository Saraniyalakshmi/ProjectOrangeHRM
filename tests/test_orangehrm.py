
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Pages.LoginPage import LoginPage
from Pages.PIM_Page import PIM_Page_Elements
from Pages.LogoutPage import Logout
from Locator.Locator_OrangeHRM import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class Test_Orangehrm:
    @pytest.fixture
    def boot(self):
        # Setup method for initializing the WebDriver with Chrome options
        self.options = Options()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.options)
        yield
        # Teardown method to close the browser after test execution
        self.driver.close()
        self.driver.quit()

    def test_OrangeHRM(self, boot):
        # Login to the application
        LoginPage.login(self,boot)

        # Navigate to PIM module
        PIM_Page_Elements.navigate_to_pim_module(self)

        # Add a new employee
        PIM_Page_Elements.add_employee(self)

        # Fill in personal details for the newly added employee
        PIM_Page_Elements.fill_personal_details(self)

        # Navigate back to PIM module
        PIM_Page_Elements.navigate_to_pim_module(self)

        # Edit details of an existing employee
        PIM_Page_Elements.edit_employee(self)

        # Navigate back to PIM module again
        PIM_Page_Elements.navigate_to_pim_module(self)

        # Delete an employee
        PIM_Page_Elements.delete_employee(self)

        # Logout from the application
        Logout.logout(self)











