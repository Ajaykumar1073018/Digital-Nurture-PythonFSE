"""
Page Object for Select Dropdown List page - CORRECT LOCATORS
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
import logging

logger = logging.getLogger(__name__)


class DropdownPage(BasePage):
    """
    Page object for Select Dropdown List page.
    """
    
    # ============================================================
    # LOCATORS - Correct from debug
    # ============================================================
    DROPDOWN = (By.ID, "select-demo")  # Correct
    SELECTED_DISPLAY = (By.CLASS_NAME, "selected-value")  # Correct
    
    # ============================================================
    # PAGE ACTIONS
    # ============================================================
    
    def get_select_element(self):
        """Get the Select element"""
        element = self.wait_for_element_presence(self.DROPDOWN)
        return Select(element)
    
    def select_by_visible_text(self, text):
        """Select option by visible text"""
        logger.info(f"Selecting by visible text: '{text}'")
        select = self.get_select_element()
        select.select_by_visible_text(text)
        return self
    
    def get_selected_option(self):
        """Get the currently selected option"""
        select = self.get_select_element()
        return select.first_selected_option.text
    
    def get_display_value(self):
        """Get the displayed selected value"""
        try:
            element = self.wait_for_element(self.SELECTED_DISPLAY)
            return element.text
        except:
            # If class doesn't work, try finding by text
            elements = self.driver.find_elements(By.XPATH, "//div[contains(text(), 'Day selected')]")
            if elements:
                return elements[0].text
            return ""
    
    def select_and_verify(self, text):
        """Select an option and verify it was selected"""
        self.select_by_visible_text(text)
        selected = self.get_selected_option()
        logger.info(f"Selected: '{selected}', Expected: '{text}'")
        return selected == text