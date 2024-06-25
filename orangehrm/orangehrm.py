#import os
import time
#from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class OrangeHRM:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)  # Increased wait time to 20 seconds

    def login(self, username, password):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        # self.driver.maximize_window()

        try:
            # Adding explicit waits
            username_field = self.wait.until(EC.presence_of_element_located((By.NAME, "username")))
            username_field.send_keys(username)

            password_field = self.wait.until(EC.presence_of_element_located((By.NAME, "password")))
            password_field.send_keys(password)

            login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
            login_button.click()

            # Check for login success
            error_message = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//p[contains(@class, 'oxd-alert-content-text')]"))
            )
            print("Error Message:", error_message.text)
        except Exception as e:
            print("Login is successful")

    def navigate_to_pim_module(self):
        pim_module = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[text()='PIM']/ancestor::a[@href='/web/index.php/pim/viewPimModule']"))
        )
        pim_module.click()



    def delete_employee(self, employee_name):
        self.navigate_to_pim_module()

        search_box = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input"))
        )
        search_box.clear()
        search_box.send_keys(employee_name)
        search_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        search_button.click()
        time.sleep(2)

        try:
            employee_checkbox = self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[1]/div/div[1]/div/label/span"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", employee_checkbox)
            time.sleep(2)
            employee_checkbox.click()
            time.sleep(2)

            delete_button = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div/button")
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", delete_button)
            time.sleep(2)
            delete_button.click()
            time.sleep(2)

            confirm_delete_button = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//button[text()=' Yes, Delete ']"))
            )
            confirm_delete_button.click()
            time.sleep(2)
            print("Employee deleted successfully")

        except Exception as e:
            print(f"Employee '{employee_name}' not present, hence could not be deleted.")

    def add_employee(self, first_name, middle_name, last_name, employee_id):
        # marital_status,gender,nationality):
        self.navigate_to_pim_module()

        add_employee_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button"))
        )
        add_employee_button.click()

        first_name_field = self.wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
        first_name_field.send_keys(first_name)

        middle_name_field = self.wait.until(EC.presence_of_element_located((By.NAME, "middleName")))
        middle_name_field.send_keys(middle_name)

        last_name_field = self.driver.find_element(By.NAME, "lastName")
        last_name_field.send_keys(last_name)

        employee_id_field = self.driver.find_element(By.XPATH, "//label[text()='Employee Id']/following::input[1]")
        employee_id_field.send_keys(Keys.CONTROL, 'a')
        employee_id_field.send_keys(Keys.BACKSPACE)
        employee_id_field.send_keys(employee_id)


        # # Save the details
        time.sleep(5)
        save_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        save_button.click()
        print("New employee added successfully")

    def fill_personal_details(self, other_id, license_number, license_expiry, dob, marital_status, gender, nationality):
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//h6[text()='Personal Details']"))
        )
        time.sleep(5)
        other_id_field = self.driver.find_element(By.XPATH,
                                                  "//label[text()='Other Id']/ancestor::div[1]/following-sibling::div/input")
        license_number_field = self.driver.find_element(By.XPATH,
                                                        "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input")
        license_expiry_field = self.driver.find_element(By.XPATH,
                                                        "//label[text()='License Expiry Date']/following::input[1]")
        dob_field = self.driver.find_element(By.XPATH, "//label[text()='Date of Birth']/following::input[1]")

        other_id_field.send_keys(other_id)
        license_number_field.send_keys(license_number)
        license_expiry_field.send_keys(license_expiry)
        dob_field.send_keys(dob)
        marital_status = self.driver.find_element(By.XPATH,
                                             "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div")
        marital_status.click()
        time.sleep(1)
        marital_status_option = self.driver.find_element(By.XPATH, "//span[text()='Married']")
        marital_status_option.click()
        time.sleep(2)
        gender_female = self.driver.find_element(By.XPATH,
                                            "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div")
        gender_male = self.driver.find_element(By.XPATH,
                                          "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]")
        gender_male.click()
        time.sleep(2)
        nationality = self.driver.find_element(By.XPATH,
                                          "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div")
        nationality.click()
        time.sleep(1)
        nationality_option = self.driver.find_element(By.XPATH, "//span[text()='Indian']")
        nationality_option.click()
        time.sleep(2)

        save_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        save_button.click()
        time.sleep(5)
        print("Personal details entered successfully for the record created")

        # # Scroll to the top of the page
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(5)

    def edit_employee(self, employee_id, new_last_name, new_license_number):
        self.navigate_to_pim_module()

        id_input_box = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input"))
        )
        id_input_box.clear()
        id_input_box.send_keys(employee_id)
        search_button = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]")
        search_button.click()
        time.sleep(2)

        try:
            employee_checkbox = self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[1]/div/div[1]/div/label/span"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", employee_checkbox)
            time.sleep(2)
            employee_checkbox.click()
            time.sleep(2)

            edit_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[2]")))
            edit_button.click()
            time.sleep(5)

            last_name = self.driver.find_element(By.NAME, "lastName")
            last_name.send_keys(Keys.CONTROL, 'a')
            last_name.send_keys(Keys.BACKSPACE)
            last_name.send_keys('new_last_name')
            time.sleep(5)

            # #add license number,License Expiry Date,Date of Birth
            license_number = self.driver.find_element(By.XPATH,
                                                 "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input")
            license_number.send_keys(Keys.CONTROL, 'a')
            license_number.send_keys(Keys.BACKSPACE)
            license_number.send_keys(new_license_number)
            time.sleep(5)


            save_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
            save_button.click()
            time.sleep(5)
            print("Existing records updated successfully")

        except Exception as e:
            print(f"Employee '{employee_id}' not present, hence could not be edited.")

    def logout(self):
        try:
            profile_icon = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//p[@class='oxd-userdropdown-name']"))
            )
            profile_icon.click()
            time.sleep(5)

            logout_button = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//a[text()='Logout']"))
            )
            logout_button.click()
            time.sleep(5)
            print("Logged out successfully")

        except Exception as e:
            print(f"Failed to log out: {e}")
