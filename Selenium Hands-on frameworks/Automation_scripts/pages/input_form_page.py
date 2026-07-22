from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class InputFormPage(BasePage):
    NAME_INPUT = (By.ID, "name")
    EMAIL_INPUT = (By.ID, "inputEmail4")
    PASSWORD_INPUT = (By.ID, "inputPassword4")
    COMPANY_INPUT = (By.ID, "company")
    WEBSITE_INPUT = (By.ID, "websitename")
    COUNTRY_DROPDOWN = (By.NAME, "country")
    CITY_INPUT = (By.ID, "inputCity")
    ADDRESS_1 = (By.ID, "inputAddress1")
    ADDRESS_2 = (By.ID, "inputAddress2")
    STATE_INPUT = (By.ID, "inputState")
    ZIP_INPUT = (By.ID, "inputZip")
    SUBMIT_BTN = (By.XPATH, "//button[text()='Submit']")
    SUCCESS_MSG = (By.CSS_SELECTOR, ".success-msg.hidden")

    def fill_form(self, name, email, phone, address):
        self.wait_for_element(self.NAME_INPUT).send_keys(name)
        self.wait_for_element(self.EMAIL_INPUT).send_keys(email)
        self.wait_for_element(self.PASSWORD_INPUT).send_keys("Pass1234!")
        self.wait_for_element(self.COMPANY_INPUT).send_keys("Tech Corp")
        self.wait_for_element(self.WEBSITE_INPUT).send_keys("https://example.com")
        
        country_dropdown = Select(self.wait_for_element(self.COUNTRY_DROPDOWN))
        country_dropdown.select_by_visible_text("United States")
        
        self.wait_for_element(self.CITY_INPUT).send_keys("New York")
        self.wait_for_element(self.ADDRESS_1).send_keys(address)
        self.wait_for_element(self.ADDRESS_2).send_keys(phone)
        self.wait_for_element(self.STATE_INPUT).send_keys("NY")
        self.wait_for_element(self.ZIP_INPUT).send_keys("10001")

    def submit_form(self):
        # Using the bulletproof JS click from BasePage
        self.js_click(self.SUBMIT_BTN)

    def get_success_message(self):
        element = self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MSG))
        return element.text