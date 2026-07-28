"""
Page Object for Simple Form Demo page - DEBUGGED LOCATORS
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import logging
import time

logger = logging.getLogger(__name__)


class SimpleFormPage(BasePage):
    """
    Page object for Simple Form Demo page.
    """
    
    # ============================================================
    # LOCATORS
    # ============================================================
    MESSAGE_INPUT = (By.ID, "user-message")
    SUBMIT_BUTTON = (By.ID, "showInput") 
    
    # ============================================================
    # PAGE ACTIONS
    # ============================================================
    
    def enter_message(self, text):
        """Enter text in the message input field."""
        logger.info(f"Entering message: '{text}'")
        # Ensure we type into the input field, not the display div
        elements = self.driver.find_elements(By.ID, "user-message")
        for el in elements:
            if el.tag_name == "input":
                el.clear()
                el.send_keys(text)
                time.sleep(0.5)
                return self
        return self
    
    def click_submit(self):
        """Click the Submit button."""
        logger.info("Clicking submit button")
        button = self.wait_for_element_clickable(self.SUBMIT_BUTTON)
        self.scroll_to_element(button)
        self.click_using_js(button)
        time.sleep(1)
        return self
    
    def get_displayed_message(self):
        """
        Get the displayed message text and clean formatting.
        """
        time.sleep(1)
        try:
            # Fallback to parsing user-message divs based on your debug log
            elements = self.driver.find_elements(By.ID, "user-message")
            for el in elements:
                # Look for the div, not the input
                if el.tag_name != "input":
                    text = el.text
                    if "Your Message:" in text:
                        return text.replace("Your Message:", "").strip()
            return ""
        except:
            return ""