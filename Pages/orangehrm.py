from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


class OrangeHRM:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def get_element(self, identifier):
        # Define the elements and their locators
        elements = {
            "url_login": "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login",
            "username_field": (By.NAME, "username"),
            "password_field": (By.NAME, "password"),
            "login_button": (By.XPATH, "//button[@type='submit']"),
            "error_message": (By.XPATH, "//p[contains(@class, 'oxd-alert-content-text')]"),
            "pim_module": (By.XPATH, "//span[text()='PIM']/ancestor::a[@href='/web/index.php/pim/viewPimModule']"),
            "search_box": (By.XPATH,
                           "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input"),
            "search_button": (By.XPATH, "//button[@type='submit']"),
            "employee_checkbox": (
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[1]/div/div[1]/div/label/span"),
            "delete_button": (By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div/button"),
            "confirm_delete_button": (By.XPATH, "//button[text()=' Yes, Delete ']"),
            "add_employee_button": (By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button"),
            "first_name_field": (By.NAME, "firstName"),
            "middle_name_field": (By.NAME, "middleName"),
            "last_name_field": (By.NAME, "lastName"),
            "employee_id_field": (By.XPATH, "//label[text()='Employee Id']/following::input[1]"),
            "save_button": (By.XPATH, "//button[@type='submit']"),
            "personal_details_header": (By.XPATH, "//h6[text()='Personal Details']"),
            "other_id_field": (By.XPATH, "//label[text()='Other Id']/ancestor::div[1]/following-sibling::div/input"),
            "license_number_field": (By.XPATH,
                                     "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input"),
            "license_expiry_field": (By.XPATH, "//label[text()='License Expiry Date']/following::input[1]"),
            "dob_field": (By.XPATH, "//label[text()='Date of Birth']/following::input[1]"),
            "marital_status": (By.XPATH,
                               "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div"),
            "marital_status_option": (By.XPATH, "//span[text()='Married']"),
            "gender_male": (
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div"),
            "gender_female": (
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div"),
            "nationality": (
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div"),
            "nationality_option": (By.XPATH, "//span[text()='Indian']"),
            "id_input_box": (
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input"),
            "edit_button": (
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[2]"),
            "profile_icon": (By.XPATH, "//p[@class='oxd-userdropdown-name']"),
            "logout_button": (By.XPATH, "//a[text()='Logout']")
        }
        return elements[identifier]

    def login(self, username, password):
        # Navigate to the login page
        self.driver.get(self.get_element("url_login"))

        try:
            # Locate and fill the username field
            username_field = self.wait.until(EC.presence_of_element_located(self.get_element("username_field")))
            username_field.send_keys(username)
            time.sleep(1)

            # Locate and fill the password field
            password_field = self.wait.until(EC.presence_of_element_located(self.get_element("password_field")))
            password_field.send_keys(password)
            time.sleep(1)

            # Locate and click the login button
            login_button = self.wait.until(EC.element_to_be_clickable(self.get_element("login_button")))
            login_button.click()

            # Check for error message
            error_message = self.wait.until(
                EC.presence_of_element_located(self.get_element("error_message"))
            )
            print("Error Message:", error_message.text)
        except Exception as e:
            print("Login is successful")
            time.sleep(2)

    def navigate_to_pim_module(self):
        # Navigate to the PIM module
        try:
            pim_module = self.wait.until(
                EC.element_to_be_clickable(self.get_element("pim_module"))
            )
            pim_module.click()
            time.sleep(2)
        except Exception as e:
            print(f"Failed to navigate to PIM module: {e}")
            time.sleep(2)

    def delete_employee(self, employee_name):
        # Delete an employee based on the provided name
        try:
            self.navigate_to_pim_module()

            # Search for the employee
            search_box = self.wait.until(
                EC.presence_of_element_located(self.get_element("search_box"))
            )
            search_box.clear()
            search_box.send_keys(employee_name)
            time.sleep(1)

            search_button = self.driver.find_element(*self.get_element("search_button"))
            search_button.click()
            time.sleep(2)

            try:
                # Select the employee checkbox and delete
                employee_checkbox = self.wait.until(
                    EC.presence_of_element_located(self.get_element("employee_checkbox"))
                )
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", employee_checkbox)
                employee_checkbox.click()
                time.sleep(1)

                delete_button = self.driver.find_element(*self.get_element("delete_button"))
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", delete_button)
                delete_button.click()
                time.sleep(1)

                confirm_delete_button = self.wait.until(
                    EC.presence_of_element_located(self.get_element("confirm_delete_button"))
                )
                confirm_delete_button.click()
                time.sleep(2)
                print("Employee deleted successfully")

            except Exception as e:
                print(f"Employee '{employee_name}' not present, hence could not be deleted.")
                time.sleep(2)

        except Exception as e:
            print(f"Failed to delete employee: {e}")
            time.sleep(2)

    def add_employee(self, first_name, middle_name, last_name, employee_id):
        # Add a new employee with the provided details
        try:
            self.navigate_to_pim_module()

            # Click the add employee button
            add_employee_button = self.wait.until(
                EC.element_to_be_clickable(self.get_element("add_employee_button"))
            )
            add_employee_button.click()
            time.sleep(2)

            # Fill in the employee details
            first_name_field = self.wait.until(EC.presence_of_element_located(self.get_element("first_name_field")))
            first_name_field.send_keys(first_name)
            time.sleep(1)

            middle_name_field = self.wait.until(EC.presence_of_element_located(self.get_element("middle_name_field")))
            middle_name_field.send_keys(middle_name)
            time.sleep(1)

            last_name_field = self.driver.find_element(*self.get_element("last_name_field"))
            last_name_field.send_keys(last_name)
            time.sleep(1)

            employee_id_field = self.driver.find_element(*self.get_element("employee_id_field"))
            employee_id_field.send_keys(Keys.CONTROL, 'a')
            employee_id_field.send_keys(Keys.BACKSPACE)
            employee_id_field.send_keys(employee_id)
            time.sleep(1)

            # Save the new employee
            save_button = self.driver.find_element(*self.get_element("save_button"))
            save_button.click()
            time.sleep(2)
            print("New employee added successfully")

        except Exception as e:
            print(f"Failed to add employee: {e}")
            time.sleep(2)

    def fill_personal_details(self, other_id, license_number, license_expiry, dob, marital_status, gender, nationality):
        # Fill in the additional details
        try:
            self.wait.until(
                EC.presence_of_element_located(self.get_element("personal_details_header"))
            )
            time.sleep(1)

            other_id_field = self.driver.find_element(*self.get_element("other_id_field"))
            license_number_field = self.driver.find_element(*self.get_element("license_number_field"))
            license_expiry_field = self.driver.find_element(*self.get_element("license_expiry_field"))
            dob_field = self.driver.find_element(*self.get_element("dob_field"))

            other_id_field.send_keys(other_id)
            time.sleep(1)
            license_number_field.send_keys(license_number)
            time.sleep(1)
            license_expiry_field.send_keys(license_expiry)
            time.sleep(1)
            dob_field.send_keys(dob)
            time.sleep(1)

            marital_status_element = self.driver.find_element(*self.get_element("marital_status"))
            marital_status_element.click()
            time.sleep(1)
            marital_status_option = self.driver.find_element(*self.get_element("marital_status_option"))
            marital_status_option.click()
            time.sleep(1)

            gender_element = self.driver.find_element(
                *self.get_element("gender_male" if gender.lower() == 'male' else "gender_female"))
            gender_element.click()
            time.sleep(2)

            nationality_element = self.driver.find_element(*self.get_element("nationality"))
            nationality_element.click()
            time.sleep(2)
            nationality_option = self.driver.find_element(*self.get_element("nationality_option"))
            nationality_option.click()
            time.sleep(1)

            save_button = self.driver.find_element(*self.get_element("save_button"))
            save_button.click()
            time.sleep(2)
            print("Personal details entered successfully for the record created")

            self.driver.execute_script("window.scrollTo(0, 0);")

        except Exception as e:
            print(f"Failed to fill personal details: {e}")
            time.sleep(2)

    def edit_employee(self, employee_id, new_last_name, new_license_number):
        # Edit an employee's details
        try:
            self.navigate_to_pim_module()
            # Search for the employee

            id_input_box = self.wait.until(
                EC.presence_of_element_located(self.get_element("id_input_box"))
            )
            id_input_box.clear()
            id_input_box.send_keys(employee_id)
            time.sleep(1)

            search_button = self.driver.find_element(*self.get_element("search_button"))
            search_button.click()
            time.sleep(2)

            try:
                employee_checkbox = self.wait.until(
                    EC.presence_of_element_located(self.get_element("employee_checkbox"))
                )
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", employee_checkbox)
                employee_checkbox.click()
                time.sleep(1)
                # Click the edit button for the employee
                edit_button = self.wait.until(EC.presence_of_element_located(self.get_element("edit_button")))
                edit_button.click()
                time.sleep(2)

                last_name = self.driver.find_element(*self.get_element("last_name_field"))
                last_name.send_keys(Keys.CONTROL, 'a')
                last_name.send_keys(Keys.BACKSPACE)
                last_name.send_keys(new_last_name)
                time.sleep(3)

                license_number = self.driver.find_element(*self.get_element("license_number_field"))
                license_number.send_keys(Keys.CONTROL, 'a')
                license_number.send_keys(Keys.BACKSPACE)
                license_number.send_keys(new_license_number)
                time.sleep(3)

                save_button = self.driver.find_element(*self.get_element("save_button"))
                save_button.click()
                time.sleep(3)
                print("Existing records updated successfully")

            except Exception as e:
                print(f"Employee '{employee_id}' not present, hence could not be edited.")
                time.sleep(2)

        except Exception as e:
            print(f"Failed to edit employee: {e}")
            time.sleep(2)

    def logout(self):
        # Log out of the OrangeHRM application
        try:
            profile_icon = self.wait.until(
                EC.presence_of_element_located(self.get_element("profile_icon"))
            )
            profile_icon.click()
            time.sleep(1)

            logout_button = self.wait.until(
                EC.presence_of_element_located(self.get_element("logout_button"))
            )
            logout_button.click()
            time.sleep(2)
            print("Logged out successfully")

        except Exception as e:
            print(f"Failed to log out: {e}")
            time.sleep(2)
