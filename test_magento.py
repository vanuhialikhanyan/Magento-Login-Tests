import allure
import pytest
from selenium.webdriver.common.by import By
import time


LOGIN_URL = "https://magento.softwaretestingboard.com/customer/account/login/"
ACCOUNT_URL = "https://magento.softwaretestingboard.com/customer/account/"
EMAIL = "van3@mailinator.com"
PASSWORD = "qaz123abc*"
NEW_PASSWORD = "qaz123abc*"


@allure.feature('Login Feature')
@allure.suite('Login Tests')
@allure.title('Test Invalid Login')
@allure.description('This test verifies that an error message is shown when trying to log in with invalid credentials.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_invalid_login(driver):

    with allure.step("Open the login page"):
        driver.get(LOGIN_URL)

    with allure.step("Enter invalid email and password"):
        email_input = driver.find_element(By.ID, "email")
        email_input.send_keys("invalidemail@gmail.com")
        password_input = driver.find_element(By.ID, "pass")
        password_input.send_keys("invalidpassword")

    with allure.step("Click on the login button"):
        login_button = driver.find_element(By.ID, "send2")
        login_button.click()

    with allure.step("Wait for the error message to appear"):
        time.sleep(3)

    with allure.step("Verify the error message"):
        error_message = driver.find_element(By.XPATH, "//div[contains(@class, 'message-error')]")
        assert "Please wait and try again later" in error_message.text, "Error message did not match"


@allure.feature('User Authentication')
@allure.suite('Login Tests')
@allure.title('Valid Login Test')
@allure.description('Test the login functionality with valid email and password.')
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.smoke
@pytest.mark.regression
def test_login(driver):

    with allure.step("Open the login page"):
        driver.get(LOGIN_URL)

    with allure.step("Enter valid email"):
        email_input = driver.find_element(By.ID, "email")
        email_input.send_keys(EMAIL)

    with allure.step("Enter valid password"):
        password_input = driver.find_element(By.ID, "pass")
        password_input.send_keys(PASSWORD)

    with allure.step("Click on the login button"):
        login_button = driver.find_element(By.ID, "send2")
        login_button.click()

    with allure.step("Wait for page to load and verify redirection to the account page"):
        time.sleep(3)
        assert driver.current_url == ACCOUNT_URL, "Failed to login with valid credentials"


@allure.feature('Account Management')
@allure.suite('Change Password Tests')
@allure.title('Change Password with Incorrect Current Password')
@allure.description('Verify that an error message is displayed while changing the password with an incorrect current password.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_change_password_incorrect_current(driver):

    with allure.step("Navigate to the account page"):
        driver.get(ACCOUNT_URL)

    with allure.step("Click on 'Change Password' link"):
        change_password_link = driver.find_element(By.LINK_TEXT, "Change Password")
        change_password_link.click()

    with allure.step("Enter incorrect current password"):
        current_password_input = driver.find_element(By.ID, "current-password")
        current_password_input.send_keys("incorrectpassword")

    with allure.step("Enter new password"):
        new_password_input = driver.find_element(By.ID, "password")
        new_password_input.send_keys(NEW_PASSWORD)

    with allure.step("Confirm new password"):
        confirm_password_input = driver.find_element(By.ID, "password-confirmation")
        confirm_password_input.send_keys(NEW_PASSWORD)

    with allure.step("Click the 'Save' button"):
        save_button = driver.find_element(By.XPATH, "//button[@title='Save']")
        save_button.click()

    with allure.step("Verify error message for incorrect current password"):
        time.sleep(3)
        error_message = driver.find_element(By.XPATH, "//div[contains(@class, 'message-error')]")
        assert "The password doesn't match this account." in error_message.text, "Expected error message not found"


@allure.feature('Account Security')
@allure.suite('Change Password Functionality')
@allure.title('Change Password Mismatch Test')
@allure.description('Verify that an error message is displayed when the new password and confirmation password do not match.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_change_password_mismatch(driver):

    with allure.step("Navigate to the account page"):
        driver.get(ACCOUNT_URL)

    with allure.step("Click on 'Change Password' link"):
        change_password_link = driver.find_element(By.LINK_TEXT, "Change Password")
        change_password_link.click()

    with allure.step("Enter the current valid password"):
        current_password_input = driver.find_element(By.ID, "current-password")
        current_password_input.send_keys(PASSWORD)

    with allure.step("Enter a new password"):
        new_password_input = driver.find_element(By.ID, "password")
        new_password_input.send_keys(NEW_PASSWORD)

    with allure.step("Enter a mismatched password in the confirmation field"):
        confirm_password_input = driver.find_element(By.ID, "password-confirmation")
        confirm_password_input.send_keys("mismatchedpassword")

    with allure.step("Click the 'Save' button"):
        save_button = driver.find_element(By.XPATH, "//button[@title='Save']")
        save_button.click()

    with allure.step("Verify the error message for password mismatch"):
        time.sleep(3)  # Wait for the page to load
        error_message = driver.find_element(By.ID, "password-confirmation-error")
        assert "Please enter the same value again." in error_message.text, "Expected mismatch error message not found"

@allure.feature('Account Management')
@allure.suite('Password Management Tests')
@allure.title('Change Password Successfully')
@allure.description('Verify that a user can change their password successfully with the correct current password and matching new passwords.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_change_password(driver):

    with allure.step("Navigate to the account page"):
        driver.get(ACCOUNT_URL)

    with allure.step("Click on 'Change Password' link"):
        change_password_link = driver.find_element(By.LINK_TEXT, "Change Password")
        change_password_link.click()

    with allure.step("Enter the current valid password"):
        current_password_input = driver.find_element(By.ID, "current-password")
        current_password_input.send_keys(PASSWORD)

    with allure.step("Enter a new password"):
        new_password_input = driver.find_element(By.ID, "password")
        new_password_input.send_keys(NEW_PASSWORD)

    with allure.step("Confirm the new password"):
        confirm_password_input = driver.find_element(By.ID, "password-confirmation")
        confirm_password_input.send_keys(NEW_PASSWORD)

    with allure.step("Click the 'Save' button to submit the password change"):
        save_button = driver.find_element(By.XPATH, "//button[@title='Save']")
        save_button.click()

    with allure.step("Verify success message for password change"):
        success_message = driver.find_element(By.XPATH, "//div[contains(@class, 'message-success')]")
        assert "You saved the account information." in success_message.text, "Expected success message not found"