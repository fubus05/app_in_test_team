import time
import logging
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException

logger = logging.getLogger(__name__)

auth_data = [
    {
        'email': 'qa.ajax.app.automation',
        'password': 'qa_automation',
        'expected_message': 'Invalid email format',
        'final_email': 'qa.ajax.app.automation@gmail.com',
        'final_password': 'qa_automation_password'
    },
]


@pytest.mark.parametrize("test_case", auth_data)
def test_user_login(user_login_fixture, test_case):
    logger.info("\nStart case of testing login")
    user_login_fixture.click_allow_button_if_present(by=AppiumBy.ID, value='com.android.permissioncontroller:id/permission_allow_button')

    user_login_fixture.find_component(by=AppiumBy.XPATH, value='(//android.widget.Button[@class="android.widget.Button"])[1]').click()

    logger.info("Entering wrong case")

    email_field = user_login_fixture.find_component(by=AppiumBy.XPATH, value='(//android.widget.EditText[@resource-id="defaultAutomationId"])[1]')
    email_field.send_keys(test_case['email'])

    password_field = user_login_fixture.find_component(by=AppiumBy.XPATH, value='(//android.widget.EditText[@resource-id="defaultAutomationId"])[2]')
    password_field.send_keys(test_case['password'])

    max_attempts = 3
    attempts = 0

    logger.info("Entering correct data for success case")

    while attempts < max_attempts:
        try:
            login_button = user_login_fixture.find_component(by=AppiumBy.XPATH, value='(//android.widget.Button[@class="android.widget.Button"])[2]')
            login_button.click()
            time.sleep(2)

            snack = user_login_fixture.find_component(by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.ajaxsystems:id/snackbar_text"]')

            if snack.text == test_case['expected_message']:
                email_field.clear()
                email_field.send_keys(test_case['final_email'])
                time.sleep(5)
            elif snack.text == 'Wrong login or password':
                password_field.clear()
                password_field.send_keys(test_case['final_password'])
                time.sleep(5)
            else:
                break

        except NoSuchElementException:
            attempts += 1
