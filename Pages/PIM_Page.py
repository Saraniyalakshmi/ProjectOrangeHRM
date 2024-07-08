from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from Locator.Locator_OrangeHRM import Locators


class PIM_Page_Elements:

    def navigate_to_pim_module(self):
        wait = WebDriverWait(self.driver, 10)

        # Navigate to the PIM module
        try:
            pim_module = wait.until(EC.element_to_be_clickable((By.XPATH,Locators.pim_module)))
            pim_module.click()
            time.sleep(5)
        except Exception as e:
            print(f"Failed to navigate to PIM module: {e}")
            time.sleep(2)

    def delete_employee(self):
        wait = WebDriverWait(self.driver, 10)
        # Delete an employee based on the provided name
        try:
            # Search for the employee
            search_box = wait.until(EC.element_to_be_clickable((By.XPATH,Locators.search_box)))
            search_box.clear()
            search_box.send_keys('Saraniyalakshmi')
            time.sleep(1)

            search_button = wait.until(EC.element_to_be_clickable((By.XPATH,Locators.search_button)))
            search_button.click()
            time.sleep(2)

            try:
                # Select the employee checkbox and delete
                employee_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH,Locators.employee_checkbox)))
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", employee_checkbox)
                employee_checkbox.click()

                delete_button = wait.until(EC.element_to_be_clickable((By.XPATH,Locators.delete_button)))
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", delete_button)
                time.sleep(2)
                delete_button.click()

                confirm_delete_button = wait.until(EC.element_to_be_clickable((By.XPATH,Locators.confirm_delete_button)))
                time.sleep(2)
                confirm_delete_button.click()
                print("Employee deleted successfully")

            except Exception as e:
                print("Employee  not present, hence could not be deleted.")


        except Exception as e:
            print(f"Failed to delete employee: {e}")



    def add_employee(self):
        wait = WebDriverWait(self.driver, 10)
        # Add a new employee with the provided details
        try:

            # Click the add employee button
            add_employee_button = wait.until(EC.element_to_be_clickable((By.XPATH,Locators.add_employee_button)))
            add_employee_button.click()
            time.sleep(2)

                # Fill in the employee details
            first_name_field = wait.until(EC.presence_of_element_located((By.NAME,Locators.first_name_field)))
            first_name_field.send_keys('Saraniyalakshmi')
            time.sleep(2)

            middle_name_field = wait.until(EC.presence_of_element_located((By.NAME, Locators.middle_name_field)))
            middle_name_field.send_keys('Chennai')
            time.sleep(2)

            last_name_field = wait.until(EC.presence_of_element_located((By.NAME, Locators.last_name_field)))
            last_name_field.send_keys('Palani')
            time.sleep(2)

            employee_id_field = wait.until(EC.presence_of_element_located((By.XPATH, Locators.employee_id_field)))
            employee_id_field.send_keys(Keys.CONTROL, 'a')
            employee_id_field.send_keys(Keys.BACKSPACE)
            employee_id_field.send_keys(1410)
            time.sleep(2)
            # Save the new employee
            save_button = wait.until(EC.presence_of_element_located((By.XPATH, Locators.save_button)))
            save_button.click()
            time.sleep(5)
            print("New employee added successfully")

        except Exception as e:
            print(f"Failed to add employee: {e}")
            time.sleep(2)

    def fill_personal_details(self):
        wait = WebDriverWait(self.driver, 20)
        try:
            wait.until(EC.presence_of_element_located((By.XPATH,Locators.personal_details_header)))
            time.sleep(5)
            other_id_field = wait.until(EC.presence_of_element_located((By.XPATH,Locators.other_id_field)))
            other_id_field.send_keys('1212')

            license_number_field =wait.until(EC.presence_of_element_located((By.XPATH,Locators.license_number_field)))
            license_number_field.send_keys('343434')

            license_expiry_field =wait.until(EC.presence_of_element_located((By.XPATH,Locators.license_expiry_field)))
            license_expiry_field.send_keys('2030-12-31')

            dob_field = wait.until(EC.presence_of_element_located((By.XPATH,Locators.dob_field)))
            dob_field.send_keys('2000-12-31')

            marital_status_element = wait.until(EC.presence_of_element_located((By.XPATH,Locators.marital_status)))
            marital_status_element.click()
            time.sleep(2)

            marital_status_option = wait.until(EC.presence_of_element_located((By.XPATH,Locators.marital_status_option)))
            marital_status_option.click()
            time.sleep(2)

            gender_element = wait.until(EC.presence_of_element_located((By.XPATH,Locators.gender_female)))
            gender_element.click()
            time.sleep(2)

            nationality_element = wait.until(EC.presence_of_element_located((By.XPATH,Locators.nationality)))
            nationality_element.click()
            time.sleep(2)

            nationality_option = wait.until(EC.presence_of_element_located((By.XPATH,Locators.nationality_option)))
            nationality_option.click()
            time.sleep(2)

            save_button = wait.until(EC.presence_of_element_located((By.XPATH,Locators.save_button)))
            save_button.click()
            time.sleep(2)
            print("Personal details entered successfully for the record created")

            self.driver.execute_script("window.scrollTo(0, 0);")

        except Exception as e:
            print(f"Failed to fill personal details: {e}")
            raise


    def edit_employee(self):
        wait = WebDriverWait(self.driver, 10)
        try:
            # Edit an employee's details
            id_input_box = wait.until(EC.presence_of_element_located((By.XPATH,Locators.id_input_box)))
            id_input_box.clear()
            id_input_box.send_keys(1410)
            time.sleep(1)

            search_button = wait.until(EC.presence_of_element_located((By.XPATH,Locators.search_button)))
            search_button.click()
            time.sleep(2)

            employee_checkbox = wait.until(EC.presence_of_element_located((By.XPATH,Locators.employee_checkbox)))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", employee_checkbox)
            employee_checkbox.click()

            # Click the edit button for the employee
            edit_button = wait.until(EC.presence_of_element_located((By.XPATH,Locators.edit_button)))
            edit_button.click()
            time.sleep(2)

            last_name = wait.until(EC.presence_of_element_located((By.NAME,Locators.last_name_field)))
            last_name.send_keys(Keys.CONTROL, 'a')
            last_name.send_keys(Keys.BACKSPACE)
            last_name.send_keys('Magesh')
            time.sleep(3)

            license_number = wait.until(EC.presence_of_element_located((By.XPATH,Locators.license_number_field)))
            license_number.send_keys(Keys.CONTROL, 'a')
            license_number.send_keys(Keys.BACKSPACE)
            license_number.send_keys(324288)
            time.sleep(3)

            save_button = wait.until(EC.presence_of_element_located((By.XPATH,Locators.save_button)))
            save_button.click()
            time.sleep(3)
            print("Existing records updated successfully")

        except Exception as e:
            print("Employee not present, hence could not be edited.")
            time.sleep(2)


