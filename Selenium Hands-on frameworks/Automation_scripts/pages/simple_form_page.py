from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class SimpleFormPage(BasePage):
    MESSAGE_INPUT = (By.ID, 'user-message')
    SUBMIT_BTN = (By.ID, 'showInput')
    MESSAGE_DISPLAY = (By.ID, 'message')

    def enter_message(self, text):
        element = self.wait_for_element(self.MESSAGE_INPUT)
        element.clear()
        element.send_keys(text)

    def click_submit(self):
        # Using the bulletproof JS click from BasePage
        self.js_click(self.SUBMIT_BTN)

    def get_displayed_message(self):
        element = self.wait.until(EC.visibility_of_element_located(self.MESSAGE_DISPLAY))
        return element.text