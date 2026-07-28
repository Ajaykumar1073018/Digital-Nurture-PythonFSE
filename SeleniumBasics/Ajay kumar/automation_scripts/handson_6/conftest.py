"""
================================================================================
HANDS-ON 6: pytest Configuration & Fixtures
================================================================================
This file contains shared fixtures and hooks for all pytest tests.
"""

import pytest
import os
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


# ============================================================
# FIXTURE: Browser Driver (Function Scope)
# ============================================================
@pytest.fixture(scope='function')
def driver():
    """
    Setup WebDriver before each test and teardown after test.
    
    Scope: function - new browser instance for each test
    - Setup: Initialize ChromeDriver
    - Yield: Provide driver to test
    - Teardown: Close browser after test
    """
    print("\n🔧 Setting up WebDriver...")
    
    # Configure Chrome options
    options = Options()
    # options.add_argument('--headless')  # Uncomment for headless mode
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1080')
    
    # Initialize driver
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    driver.implicitly_wait(5)
    
    # Yield driver to test
    yield driver
    
    # Teardown: Close browser after test
    print("\n🧹 Cleaning up WebDriver...")
    driver.quit()


# ============================================================
# FIXTURE: Base URL (Session Scope)
# ============================================================
@pytest.fixture(scope='session')
def base_url():
    """Base URL for all tests - shared across all tests"""
    return "https://www.lambdatest.com/selenium-playground"


# ============================================================
# FIXTURE: Test Data (Session Scope)
# ============================================================
@pytest.fixture(scope='session')
def test_messages():
    """Test data for parameterized tests"""
    return [
        "Hello Selenium",
        "Automation Testing",
        "1234567890",
        "Special @#$%^&*()",
        "Test with spaces"
    ]


# ============================================================
# HOOK: Screenshot on Test Failure
# ============================================================
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Capture screenshot when a test fails.
    
    This hook runs after each test and checks if it failed.
    If failed, takes a screenshot and saves it in the reports folder.
    """
    # Execute the test
    outcome = yield
    report = outcome.get_result()
    
    # Check if test failed
    if report.when == "call" and report.failed:
        try:
            # Get the driver fixture from the test
            driver = item.funcargs.get('driver')
            
            if driver:
                # Create reports directory if it doesn't exist
                reports_dir = os.path.join(os.path.dirname(__file__), 'reports')
                os.makedirs(reports_dir, exist_ok=True)
                
                # Generate filename with timestamp
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                test_name = item.name.replace('[', '_').replace(']', '_').replace('/', '_')
                filename = f"{test_name}_{timestamp}.png"
                filepath = os.path.join(reports_dir, filename)
                
                # Take screenshot
                driver.save_screenshot(filepath)
                print(f"\n📸 Screenshot saved: {filepath}")
                
        except Exception as e:
            print(f"\n⚠️ Could not capture screenshot: {e}")


# ============================================================
# HOOK: pytest Configuration
# ============================================================
def pytest_configure(config):
    """
    Configure pytest with custom markers and settings.
    """
    # Add custom markers
    config.addinivalue_line(
        "markers",
        "smoke: Mark test as smoke test"
    )
    config.addinivalue_line(
        "markers",
        "regression: Mark test as regression test"
    )
    config.addinivalue_line(
        "markers",
        "slow: Mark test as slow running"
    )