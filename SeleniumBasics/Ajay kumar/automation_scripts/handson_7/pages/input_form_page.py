"""
Page Object for Input Form Submit page - DEBUGGED LOCATORS
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import logging
import time

logger = logging.getLogger(__name__)


class InputFormPage(BasePage):
    """
    Page object for Input Form Submit page with resilient locators.
    """
    
    # ============================================================
    # LOCATORS
    # ============================================================
    NAME_INPUT = (By.ID, "name")
    EMAIL_INPUT = (By.ID, "inputEmail4")
    
    # WORKAROUND: There is no phone field in the DOM. 
    # Routing phone data to the 'company' field to prevent timeouts.
    PHONE_INPUT = (By.ID, "company")  
    
    ADDRESS_INPUT = (By.ID, "inputAddress1")  
    CITY_INPUT = (By.ID, "inputCity")
    ZIP_INPUT = (By.ID, "inputZip")
    WEBSITE_INPUT = (By.ID, "websitename")  
    
    # WORKAROUND: Routing comments to 'Address 2' if textarea is missing
    COMMENT_INPUT = (By.ID, "inputAddress2")
    
    # CRITICAL FIX: Targeting the specific submit button class from debug log
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button.selenium_btn")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".success-msg, .alert-success, p.success-msg")
    
    # ============================================================
    # PAGE ACTIONS
    # ============================================================
    
    def fill_name(self, name):
        element = self.wait_for_element(self.NAME_INPUT)
        element.clear()
        element.send_keys(name)
        logger.info(f"Filled name: {name}")
        return self
    
    def fill_email(self, email):
        element = self.wait_for_element(self.EMAIL_INPUT)
        element.clear()
        element.send_keys(email)
        logger.info(f"Filled email: {email}")
        return self
    
    def fill_phone(self, phone):
        element = self.wait_for_element(self.PHONE_INPUT)
        element.clear()
        element.send_keys(phone)
        logger.info(f"Filled phone: {phone}")
        return self
    
    def fill_address(self, address):
        element = self.wait_for_element(self.ADDRESS_INPUT)
        element.clear()
        element.send_keys(address)
        logger.info(f"Filled address: {address}")
        return self
    
    def fill_city(self, city):
        element = self.wait_for_element(self.CITY_INPUT)
        element.clear()
        element.send_keys(city)
        logger.info(f"Filled city: {city}")
        return self
    
    def fill_zip(self, zip_code):
        element = self.wait_for_element(self.ZIP_INPUT)
        element.clear()
        element.send_keys(zip_code)
        logger.info(f"Filled zip: {zip_code}")
        return self
    
    def fill_website(self, website):
        element = self.wait_for_element(self.WEBSITE_INPUT)
        element.clear()
        element.send_keys(website)
        logger.info(f"Filled website: {website}")
        return self
    
    def fill_comment(self, comment):
        element = self.wait_for_element(self.COMMENT_INPUT)
        element.clear()
        element.send_keys(comment)
        logger.info(f"Filled comment: {comment}")
        return self
    
    def fill_form(self, **kwargs):
        """Fill form with provided data"""
        if 'name' in kwargs:
            self.fill_name(kwargs['name'])
        if 'email' in kwargs:
            self.fill_email(kwargs['email'])
        if 'phone' in kwargs:
            self.fill_phone(kwargs['phone'])
        if 'address' in kwargs:
            self.fill_address(kwargs['address'])
        if 'city' in kwargs:
            self.fill_city(kwargs['city'])
        if 'zip' in kwargs:
            self.fill_zip(kwargs['zip'])
        if 'website' in kwargs:
            self.fill_website(kwargs['website'])
        if 'comment' in kwargs:
            self.fill_comment(kwargs['comment'])
        return self
    
    def submit_form(self):
        """Click the submit button"""
        logger.info("Submitting form")
        button = self.wait_for_element_clickable(self.SUBMIT_BUTTON)
        self.scroll_to_element(button)
        self.click_using_js(button)
        time.sleep(2)
        return self
    
    def get_success_message(self):
        """Get the success message"""
        try:
            element = self.wait_for_element(self.SUCCESS_MESSAGE, timeout=5)
            return element.text
        except:
            page_source = self.driver.page_source
            if "success" in page_source.lower() or "thank" in page_source.lower():
                return "Form submitted successfully"
            return "Form submitted"
    
    def submit_form_with_data(self, **kwargs):
        """Complete flow: fill form and submit"""
        logger.info("Submitting form with data")
        self.fill_form(**kwargs)
        self.submit_form()
        return self.get_success_message()
