import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from orangehrm.orangehrm import OrangeHRM

@pytest.fixture(scope="module")
def driver():
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def orangehrm(driver):
    return OrangeHRM(driver)

def test_login(orangehrm):
    orangehrm.login("Admin", "admin123")

def test_add_employee(orangehrm):
    orangehrm.add_employee("Saraniya", "Chennai", "Palani", "1410")

def test_fill_personal_details(orangehrm):
    orangehrm.fill_personal_details("67890", "A1234567", "2030-12-31", "1990-01-01", "Married", "Male", "Indian")

def test_edit_employee(orangehrm):
    orangehrm.edit_employee("1410", "Magesh", "324288")

def test_delete_employee(orangehrm):
    orangehrm.delete_employee("Saraniya")

def test_logout(orangehrm):
    orangehrm.logout()
