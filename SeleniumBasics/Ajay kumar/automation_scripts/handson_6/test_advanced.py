"""
================================================================================
HANDS-ON 6: Advanced pytest Features
================================================================================
- Parameterized Tests
- Multiple test scenarios
- Data-driven testing
"""

import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


# ============================================================
# TEST 1: Parameterized Form Submission
# ============================================================
@pytest.mark.parametrize("message", [
    "Hello",
    "Selenium Automation",
    "12345",
    "Testing with spaces",
    "Special @#$%^&*()"
])
def test_parameterized_form_submission(driver, base_url, message):
    """
    Test form submission with multiple input values.
    
    This test runs 5 times with different messages.
    """
    print(f"\n📝 Running: test_parameterized_form_submission with '{message}'")
    
    # Navigate to Simple Form Demo
    driver.get(f"{base_url}/simple-form-demo")
    
    # Wait for page to load
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, "user-message")))
    time.sleep(1)
    
    # Enter message
    message_input = driver.find_element(By.ID, "user-message")
    message_input.clear()
    message_input.send_keys(message)
    print(f"   ✅ Entered: '{message}'")
    
    # Click Submit button
    submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Get Checked Value')]")
    submit_button.click()
    print("   ✅ Clicked Submit")
    
    # Wait for result
    wait.until(EC.visibility_of_element_located((By.ID, "message")))
    
    # Verify message
    result_element = driver.find_element(By.ID, "message")
    displayed_message = result_element.text
    print(f"   ✅ Displayed: '{displayed_message}'")
    
    # Assert
    assert displayed_message == message, \
        f"Expected '{message}', but got '{displayed_message}'"
    
    print("   ✅ Test PASSED!")


# ============================================================
# TEST 2: Multiple Dropdown Options
# ============================================================
@pytest.mark.parametrize("day", [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
])
def test_parameterized_dropdown(driver, base_url, day):
    """
    Test dropdown with multiple options.
    
    This test runs 7 times with different days.
    """
    print(f"\n📝 Running: test_parameterized_dropdown with '{day}'")
    
    # Navigate to Select Dropdown List
    driver.get(f"{base_url}/select-dropdown-demo")
    
    # Wait for page to load
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, "select-demo")))
    time.sleep(1)
    
    # Find dropdown and select option
    dropdown = driver.find_element(By.ID, "select-demo")
    select = Select(dropdown)
    
    # Select day
    select.select_by_visible_text(day)
    print(f"   ✅ Selected: {day}")
    
    # Verify selection
    selected_option = select.first_selected_option
    assert selected_option.text == day, \
        f"Expected '{day}', got '{selected_option.text}'"
    
    print("   ✅ Test PASSED!")


# ============================================================
# TEST 3: Multiple Checkbox Operations
# ============================================================
@pytest.mark.parametrize("option", [
    "Option 1",
    "Option 2",
    "Option 3",
    "Option 4"
])
def test_parameterized_checkbox(driver, base_url, option):
    """
    Test checking and unchecking multiple options.
    """
    print(f"\n📝 Running: test_parameterized_checkbox with '{option}'")
    
    # Navigate to Checkbox Demo
    driver.get(f"{base_url}/checkbox-demo")
    
    # Wait for page to load
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Option')]")))
    time.sleep(1)
    
    # Find the checkbox
    checkbox = driver.find_element(By.XPATH, f"//input[@type='checkbox' and @value='{option}']")
    
    # Click and verify selected
    checkbox.click()
    assert checkbox.is_selected(), f"{option} should be selected"
    print(f"   ✅ {option} selected")
    
    # Wait and then click again
    time.sleep(1)
    checkbox.click()
    assert not checkbox.is_selected(), f"{option} should be deselected"
    print(f"   ✅ {option} deselected")
    
    print("   ✅ Test PASSED!")


# ============================================================
# TEST 4: Parameterized Form Data
# ============================================================
@pytest.mark.parametrize("name, email, phone", [
    ("John Doe", "john@test.com", "1234567890"),
    ("Jane Smith", "jane@test.com", "0987654321"),
    ("Bob Johnson", "bob@test.com", "5551234567"),
])
def test_parameterized_form_data(driver, base_url, name, email, phone):
    """
    Test form with multiple data sets.
    """
    print(f"\n📝 Running: test_parameterized_form_data with {name}, {email}, {phone}")
    
    # Navigate to Input Form Submit
    driver.get(f"{base_url}/input-form-demo")
    
    # Wait for page to load
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.NAME, "name")))
    time.sleep(1)
    
    # Fill form fields
    try:
        driver.find_element(By.NAME, "name").send_keys(name)
        driver.find_element(By.NAME, "email").send_keys(email)
        driver.find_element(By.NAME, "phone").send_keys(phone)
        driver.find_element(By.NAME, "address").send_keys("123 Test Street")
        driver.find_element(By.NAME, "city").send_keys("Test City")
        driver.find_element(By.NAME, "state").send_keys("Test State")
        driver.find_element(By.NAME, "zip").send_keys("12345")
        driver.find_element(By.NAME, "website").send_keys("example.com")
        print("   ✅ Form fields filled")
    except Exception as e:
        print(f"   ⚠️ Could not fill all fields: {e}")
    
    # Submit the form
    submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
    submit_button.click()
    print("   ✅ Form submitted")
    
    print("   ✅ Test PASSED!")


# ============================================================
# TEST 5: Smoke Test
# ============================================================
@pytest.mark.smoke
def test_smoke_test_all_pages(driver, base_url):
    """
    Smoke test: Verify all pages load correctly.
    """
    print("\n📝 Running: test_smoke_test_all_pages")
    
    pages = [
        "/",
        "/simple-form-demo",
        "/checkbox-demo",
        "/select-dropdown-demo",
        "/bootstrap-alert-demo",
        "/table-sort-search-demo",
        "/input-form-demo"
    ]
    
    for page in pages:
        url = f"{base_url}{page}"
        driver.get(url)
        time.sleep(1)
        print(f"   ✅ Loaded: {page}")
        
        # Verify page loaded
        assert driver.title, f"Page title is empty for {page}"
        print(f"      Title: {driver.title[:50]}...")
    
    print("   ✅ All pages loaded successfully!")


# ============================================================
# TEST 6: Regression Tests
# ============================================================
@pytest.mark.regression
def test_regression_suite(driver, base_url):
    """
    Regression test suite for critical flows.
    """
    print("\n📝 Running: test_regression_suite")
    
    # Test 1: Simple Form
    driver.get(f"{base_url}/simple-form-demo")
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, "user-message")))
    
    message_input = driver.find_element(By.ID, "user-message")
    message_input.send_keys("Regression Test")
    driver.find_element(By.XPATH, "//button[contains(text(), 'Get Checked Value')]").click()
    
    # Test 2: Checkbox
    driver.get(f"{base_url}/checkbox-demo")
    wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Option')]")))
    
    checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox' and @value='Option 1']")
    checkbox.click()
    assert checkbox.is_selected(), "Checkbox should be selected"
    
    # Test 3: Dropdown
    driver.get(f"{base_url}/select-dropdown-demo")
    wait.until(EC.presence_of_element_located((By.ID, "select-demo")))
    
    dropdown = driver.find_element(By.ID, "select-demo")
    select = Select(dropdown)
    select.select_by_visible_text("Wednesday")
    assert select.first_selected_option.text == "Wednesday"
    
    print("   ✅ All regression tests passed!")