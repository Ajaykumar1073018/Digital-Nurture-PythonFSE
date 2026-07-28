"""
Hands-On 7: Page Object Model Tests - Fixed Class Structure
"""

import pytest
import time
from pages.simple_form_page import SimpleFormPage
from pages.checkbox_page import CheckboxPage
from pages.dropdown_page import DropdownPage
from pages.input_form_page import InputFormPage
import logging

logger = logging.getLogger(__name__)


class TestPOM:
    """Test class using Page Object Model."""
    
    def test_simple_form_pom(self, driver, base_url):
        """Test Simple Form using Page Object Model."""
        logger.info("\n📝 Testing Simple Form with POM...")
        
        page = SimpleFormPage(driver)
        page.navigate_to(base_url + "simple-form-demo")
        
        # Wait for page to load
        time.sleep(2)
        
        test_message = "Hello from POM!"
        page.enter_message(test_message)
        
        # Wait for button to be clickable
        time.sleep(1)
        page.click_submit()
        
        displayed = page.get_displayed_message()
        assert displayed == test_message, f"Expected '{test_message}', got '{displayed}'"
        logger.info(f"✓ Successfully submitted and verified: '{displayed}'")
    
    def test_checkbox_pom(self, driver, base_url):
        """Test Checkbox Demo using Page Object Model."""
        logger.info("\n☑️ Testing Checkbox with POM...")
        
        page = CheckboxPage(driver)
        page.navigate_to(base_url + "checkbox-demo")
        time.sleep(2)
        
        page.check_checkbox()
        assert page.is_checkbox_selected(), "Checkbox should be selected"
        assert page.is_checked_message_displayed(), "Checked message should be displayed"
        logger.info("✓ Checkbox checked successfully")
        
        page.uncheck_checkbox()
        assert not page.is_checkbox_selected(), "Checkbox should be deselected"
        logger.info("✓ Checkbox unchecked successfully")
    
    def test_dropdown_pom(self, driver, base_url):
        """Test Dropdown using Page Object Model."""
        logger.info("\n📋 Testing Dropdown with POM...")
        
        page = DropdownPage(driver)
        page.navigate_to(base_url + "select-dropdown-demo")
        time.sleep(2)
        
        days = ["Monday", "Wednesday", "Friday", "Sunday"]
        for day in days:
            result = page.select_and_verify(day)
            assert result, f"Failed to select '{day}'"
            logger.info(f"✓ Selected and verified: '{day}'")
        
        display = page.get_display_value()
        assert display is not None and len(display) > 0, "Display message should not be empty"
        logger.info(f"✓ Display message: '{display}'")
    
    def test_input_form_pom(self, driver, base_url):
        """Test Input Form using Page Object Model."""
        logger.info("\n📝 Testing Input Form with POM...")
        
        page = InputFormPage(driver)
        page.navigate_to(base_url + "input-form-demo")
        time.sleep(2)
        
        test_data = {
            "name": "John Doe",
            "email": "john@example.com",
            "phone": "1234567890",
            "address": "123 Main Street, City",
            "city": "New York",
            "zip": "10001",
            "website": "johndoe.com",
            "comment": "This is a test submission"
        }
        
        success_message = page.submit_form_with_data(**test_data)
        assert success_message is not None, "Success message should not be None"
        logger.info(f"✓ Form submitted: '{success_message}'")
    
    @pytest.mark.parametrize("name,email,phone,address", [
        ("Alice Johnson", "alice@test.com", "1112223333", "123 Elm St, Boston"),
        ("Bob Smith", "bob@test.com", "4445556666", "456 Oak Ave, Chicago"),
        ("Charlie Brown", "charlie@test.com", "7778889999", "789 Pine Rd, LA"),
    ])
    def test_input_form_parameterised(self, driver, base_url, name, email, phone, address):
        """Parameterised test for Input Form with different data."""
        logger.info(f"\n📝 Testing Input Form with: {name}")
        
        page = InputFormPage(driver)
        page.navigate_to(base_url + "input-form-demo")
        time.sleep(2)
        
        success = page.submit_form_with_data(
            name=name,
            email=email,
            phone=phone,
            address=address,
            city="Test City",
            zip="12345"
        )
        assert success is not None, f"Success message should not be None for {name}"
        logger.info(f"✓ Success for {name}: '{success}'")
    
    def test_method_chaining(self, driver, base_url):
        """Demonstrate method chaining with page objects."""
        logger.info("\n🔗 Testing Method Chaining with POM...")
        
        page = SimpleFormPage(driver)
        page.navigate_to(base_url + "simple-form-demo")
        time.sleep(2)
        
        page.enter_message("Method Chaining Test")
        time.sleep(1)
        page.click_submit()
        
        displayed = page.get_displayed_message()
        assert displayed == "Method Chaining Test"
        logger.info(f"✓ Method chaining successful: '{displayed}'")
    
    def test_multiple_form_submissions(self, driver, base_url):
        """Test multiple form submissions with different data."""
        logger.info("\n📝 Testing Multiple Form Submissions...")
        
        page = SimpleFormPage(driver)
        page.navigate_to(base_url + "simple-form-demo")
        time.sleep(2)
        
        test_messages = [
            "First Test Message",
            "Second Test Message",
            "Third Test Message"
        ]
        
        for message in test_messages:
            page.enter_message(message)
            time.sleep(1)
            page.click_submit()
            displayed = page.get_displayed_message()
            assert displayed == message, f"Expected '{message}', got '{displayed}'"
            logger.info(f"✓ Successfully submitted: '{message}'")
        
        logger.info(f"✓ All {len(test_messages)} submissions passed")


if __name__ == "__main__":
    pytest.main(["-v", "--html=../report.html", "--self-contained-html"])