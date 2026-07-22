import pytest
from pages.simple_form_page import SimpleFormPage
from pages.checkbox_page import CheckboxPage
from pages.dropdown_page import DropdownPage
from pages.input_form_page import InputFormPage

"""
TASK 2, STEP 59 POM MAINTENANCE COMMENT:
Q: What problem would occur in a flat script if the Submit button's ID changed from 'submit' to 'btn-submit'? How does POM solve this?
A: In a flat script, you would have to manually find and replace driver.find_element(By.ID, 'submit') in EVERY SINGLE test case that clicks that button. 
With POM, the locator is defined exactly once in the Page Class (e.g., SUBMIT_BTN = (By.ID, 'btn-submit')). You update that one single line of code, and all 50 tests that use it are instantly fixed!
"""

@pytest.mark.parametrize('message', ['Hello', 'Selenium Automation', '12345'])
def test_simple_form_submission(driver, base_url, message):
    page = SimpleFormPage(driver)
    page.navigate_to(base_url + 'simple-form-demo/')
    
    page.enter_message(message)
    page.click_submit()
    
    # Asserting from the page object
    assert page.get_displayed_message() == message, f"Expected '{message}'"

def test_checkbox_demo(driver, base_url):
    page = CheckboxPage(driver)
    page.navigate_to(base_url + 'checkbox-demo/')
    
    # Check and verify
    page.check_option()
    assert page.is_option_checked(), "Checkbox should be selected"
    
    # Uncheck and verify
    page.uncheck_option()
    assert not page.is_option_checked(), "Checkbox should be deselected"

def test_dropdown_selection(driver, base_url):
    page = DropdownPage(driver)
    page.navigate_to(base_url + 'select-dropdown-demo/')
    
    page.select_day("Wednesday")
    assert "Wednesday" in page.get_selected_text(), "Wednesday should be selected"

def test_input_form_submit(driver, base_url):
    page = InputFormPage(driver)
    page.navigate_to(base_url + 'input-form-demo/')
    
    page.fill_form("John Doe", "john@example.com", "555-1234", "123 Main St")
    page.submit_form()
    
    assert "Thanks for contacting us" in page.get_success_message(), "Form did not submit successfully"