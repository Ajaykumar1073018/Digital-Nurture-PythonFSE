from selenium.webdriver.common.by import By
from .base_page import BasePage

class CheckboxPage(BasePage):
    # Our bulletproof XPath from earlier
    FIRST_CHECKBOX = (By.XPATH, "(//input[@type='checkbox'])[1]")

    def check_option(self):
        element = self.wait_for_element(self.FIRST_CHECKBOX)
        if not element.is_selected():
            self.driver.execute_script("arguments[0].click();", element)

    def uncheck_option(self):
        element = self.wait_for_element(self.FIRST_CHECKBOX)
        if element.is_selected():
            self.driver.execute_script("arguments[0].click();", element)

    def is_option_checked(self):
        element = self.wait_for_element(self.FIRST_CHECKBOX)
        return element.is_selected()