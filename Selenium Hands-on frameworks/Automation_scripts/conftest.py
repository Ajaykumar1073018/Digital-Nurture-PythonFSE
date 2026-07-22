import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Task 2, Step 48: Session-scoped fixture for base URL
@pytest.fixture(scope='session')
def base_url():
    return 'https://www.lambdatest.com/selenium-playground/'

# Task 1, Step 41: Function-scoped fixture for WebDriver
@pytest.fixture(scope='function')
def driver():
    # ADVANCED FIX: Anti-Bot Detection Chrome Options
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    
    # Yield splits the fixture into setup (above) and teardown (below)
    yield driver 
    
    driver.quit()

# Task 2, Step 46: Hook to capture a screenshot on test failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    # Check if the test failed during the 'call' phase
    if report.when == 'call' and report.failed:
        # Access the driver from the test's fixtures to take the screenshot
        if 'driver' in item.fixturenames:
            web_driver = item.funcargs['driver']
            test_name = item.name
            web_driver.save_screenshot(f'{test_name}_failure.png')