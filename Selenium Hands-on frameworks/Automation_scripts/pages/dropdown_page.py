from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .base_page import BasePage

class DropdownPage(BasePage):
    SELECT_DROPDOWN = (By.ID, 'select-demo')
    SELECTED_VALUE = (By.CSS_SELECTOR, '.selected-value')

    def select_day(self, day_name):
        element = self.wait_for_element(self.SELECT_DROPDOWN)
        dropdown = Select(element)
        dropdown.select_by_visible_text(day_name)
        # Wait for the JS to update the text on screen
        self.wait_for_text(self.SELECTED_VALUE, day_name)

    def get_selected_text(self):
        return self.driver.find_element(*self.SELECTED_VALUE).text