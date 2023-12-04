import pytest
import logging
from appium import webdriver
from appium.options.android import UiAutomator2Options

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='com.ajaxsystems',
    appActivity='com.ajaxsystems.ui.activity.LauncherActivity',
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4723'

capabilities_options = UiAutomator2Options().load_capabilities(capabilities)


@pytest.fixture(scope='session')
def driver():
    app_driver = webdriver.Remote(command_executor=appium_server_url, options=capabilities_options)
    yield app_driver
