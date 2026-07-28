"""
pytest Configuration and Fixtures
"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import os
from datetime import datetime
import logging
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.fixture(scope="function")
def driver():
    """Function-scoped fixture for WebDriver."""
    logger.info("🚀 Setting up WebDriver...")
    
    options = Options()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--disable-notifications')
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(5)
    
    yield driver
    
    logger.info("🧹 Cleaning up WebDriver...")
    driver.quit()


@pytest.fixture(scope="session")
def base_url():
    """Session-scoped fixture for base URL."""
    return "https://www.lambdatest.com/selenium-playground/"


@pytest.fixture(scope="function")
def screenshot_on_failure(request, driver):
    """Fixture that captures screenshot on test failure."""
    yield
    if hasattr(request.node, 'rep_call') and request.node.rep_call.failed:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        test_name = request.node.name.replace("[", "_").replace("]", "_")
        filename = f"screenshots/{test_name}_{timestamp}.png"
        os.makedirs("screenshots", exist_ok=True)
        driver.save_screenshot(filename)
        logger.info(f"📸 Screenshot saved: {filename}")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture test result for screenshot on failure."""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)