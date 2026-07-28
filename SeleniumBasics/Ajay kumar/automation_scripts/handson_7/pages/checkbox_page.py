"""
Page Object for Checkbox Demo page - CORRECT LOCATORS
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import logging
import time

logger = logging.getLogger(__name__)


class CheckboxPage(BasePage):
    """
    Page object for Checkbox Demo page.
    """
    
    # ============================================================
    # LOCATORS
    # ============================================================
    ALL_CHECKBOXES = (By.XPATH, "//input[@type='checkbox']")
    
    # ============================================================
    # PAGE ACTIONS
    # ============================================================
    
    def get_checkbox(self):
        """Get the first checkbox on the page"""
        checkboxes = self.driver.find_elements(*self.ALL_CHECKBOXES)
        for cb in checkboxes:
            if cb.is_displayed():
                return cb
        return checkboxes[0] if checkboxes else None
    
    def click_checkbox(self):
        """Click the checkbox to toggle state"""
        logger.info("Clicking checkbox")
        checkbox = self.get_checkbox()
        if checkbox:
            self.scroll_to_element(checkbox)
            self.click_using_js(checkbox)
            time.sleep(0.5)
        return self
    
    def is_checkbox_selected(self):
        """Check if checkbox is selected"""
        checkbox = self.get_checkbox()
        return checkbox.is_selected() if checkbox else False
    
    def check_checkbox(self):
        """Check the checkbox if not already checked"""
        if not self.is_checkbox_selected():
            self.click_checkbox()
            logger.info("Checkbox checked")
        else:
            logger.info("Checkbox already checked")
        return self
    
    def uncheck_checkbox(self):
        """Uncheck the checkbox if checked"""
        if self.is_checkbox_selected():
            self.click_checkbox()
            logger.info("Checkbox unchecked")
        else:
            logger.info("Checkbox already unchecked")
        return self
    
    def get_display_message(self):
        """Get the display message text"""
        try:
            # LambdaTest single checkbox message typically uses ID 'txtAge'
            try:
                element = self.driver.find_element(By.ID, "txtAge")
                if element.is_displayed():
                    return element.text
            except:
                pass
            
            # Fallback to searching the DOM for text variations
            elements = self.driver.find_elements(By.XPATH, "//*[contains(translate(text(), 'CHECKED', 'checked'), 'checked')]")
            for el in elements:
                if el.is_displayed():
                    return el.text
            return ""
        except:
            return ""
    
    def is_checked_message_displayed(self):
        """Check if checked message is displayed"""
        message = self.get_display_message()
        return "checked" in message.lower()