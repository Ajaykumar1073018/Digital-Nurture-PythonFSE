"""
Base Page class - UPDATED with better element location
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
import logging
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BasePage:
    """Base page class that all page objects inherit from."""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.driver.implicitly_wait(5)
        logger.info(f"Initialized {self.__class__.__name__}")
    
    def navigate_to(self, url):
        logger.info(f"Navigating to: {url}")
        self.driver.get(url)
        return self
    
    def get_title(self):
        return self.driver.title
    
    def get_current_url(self):
        return self.driver.current_url
    
    def wait_for_element(self, locator, timeout=10):
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.visibility_of_element_located(locator))
            logger.info(f"Element found: {locator}")
            return element
        except TimeoutException:
            logger.error(f"Element not found: {locator}")
            raise
    
    def wait_for_element_clickable(self, locator, timeout=10):
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.element_to_be_clickable(locator))
            logger.info(f"Element is clickable: {locator}")
            return element
        except TimeoutException:
            logger.error(f"Element not clickable: {locator}")
            raise
    
    def wait_for_element_presence(self, locator, timeout=10):
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.presence_of_element_located(locator))
            logger.info(f"Element present: {locator}")
            return element
        except TimeoutException:
            logger.error(f"Element not present: {locator}")
            raise
    
    def scroll_to_element(self, element):
        # UPDATED: Scroll to center to avoid sticky headers blocking clicks
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(0.5)  # Small pause after scroll
        logger.info("Scrolled to element")
        return self
    
    def click_using_js(self, element):
        """Click element using JavaScript."""
        self.driver.execute_script("arguments[0].click();", element)
        logger.info("Clicked element using JavaScript")
        return self
    
    def take_screenshot(self, filename):
        self.driver.save_screenshot(filename)
        logger.info(f"Screenshot saved: {filename}")
        return self
    
    def find_element_by_text(self, tag, text):
        """Find element by its text content."""
        try:
            elements = self.driver.find_elements(By.TAG_NAME, tag)
            for element in elements:
                if text in element.text:
                    return element
            return None
        except:
            return None