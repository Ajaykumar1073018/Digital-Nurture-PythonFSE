"""
================================================================================
HANDS-ON 5: TASK 2 - EXPLICIT WAITS
================================================================================
Topics Covered:
- WebDriverWait and Expected Conditions
- Implicit vs Explicit vs Fluent Waits
- Avoiding Hard-Coded Sleeps
- element_to_be_clickable
- FluentWait with custom polling

Target: LambdaTest Selenium Playground
================================================================================
"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager


# ============================================================
# Setup Function
# ============================================================
def setup_driver():
    """Initialize WebDriver"""
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver


# ============================================================
# STEP 36: Bootstrap Alerts with Explicit Wait
# ============================================================
def step_36_bootstrap_alerts():
    """
    Click Success Message button and wait for alert using explicit wait
    """
    print("\n" + "=" * 70)
    print("STEP 36: Bootstrap Alerts with Explicit Wait")
    print("=" * 70)
    
    driver = setup_driver()
    
    try:
        print("\n📌 Navigating to Bootstrap Alerts Demo...")
        driver.get("https://www.lambdatest.com/selenium-playground/")
        
        # Find and click Bootstrap Alerts link
        bootstrap_link = driver.find_element(By.LINK_TEXT, "Bootstrap Alerts")
        bootstrap_link.click()
        print("✅ Clicked 'Bootstrap Alerts' link")
        
        # Wait for page to load
        time.sleep(2)
        
        # Click the Success Message button
        print("\n📝 Clicking 'Success Message' button...")
        success_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Success Message')]")
        success_button.click()
        print("✅ Clicked 'Success Message' button")
        
        # ✅ EXPLICIT WAIT: Wait for alert to become visible
        print("\n⏳ Waiting for alert to appear (Explicit Wait - 10 seconds max)...")
        wait = WebDriverWait(driver, 10)
        success_alert = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success"))
        )
        
        # Verify the alert text
        alert_text = success_alert.text
        print(f"✅ Alert found! Text: '{alert_text}'")
        
        # Assert alert contains 'successfully'
        if 'successfully' in alert_text.lower():
            print("✅ Alert contains 'successfully' - TEST PASSED!")
        else:
            print(f"⚠️ Alert does NOT contain 'successfully' - Actual: '{alert_text}'")
            
    except TimeoutException:
        print("❌ TIMEOUT: Alert not found within 10 seconds")
        print("   The element might not have appeared or the selector might be wrong")
    except Exception as e:
        print(f"❌ Error: {str(e)[:200]}")
    finally:
        driver.quit()
        print("\n" + "=" * 70)


# ============================================================
# STEP 37: time.sleep() vs Explicit Wait Comparison
# ============================================================
def step_37_wait_comparison():
    """
    Compare time.sleep() vs explicit wait performance
    """
    print("\n" + "=" * 70)
    print("STEP 37: time.sleep() vs Explicit Wait Comparison")
    print("=" * 70)
    
    # ========== Test 1: time.sleep() (BAD PRACTICE) ==========
    print("\n1️⃣  Using time.sleep(3) - HARD CODED SLEEP (BAD):")
    print("-" * 50)
    
    driver1 = setup_driver()
    try:
        start = time.time()
        
        driver1.get("https://www.lambdatest.com/selenium-playground/")
        bootstrap_link = driver1.find_element(By.LINK_TEXT, "Bootstrap Alerts")
        bootstrap_link.click()
        time.sleep(2)
        
        success_button = driver1.find_element(By.XPATH, "//button[contains(text(), 'Success Message')]")
        success_button.click()
        
        # ❌ BAD: Hard-coded sleep - always waits 3 seconds
        print("   ⏳ Sleeping for 3 seconds (fixed wait)...")
        time.sleep(3)
        
        # Try to find the element after sleep
        try:
            alert = driver1.find_element(By.CSS_SELECTOR, ".alert-success")
            print(f"   ✅ Alert found after 3 second sleep")
            print(f"   ✅ Alert text: '{alert.text}'")
        except NoSuchElementException:
            print("   ❌ Alert NOT found after 3 second sleep")
            
        sleep_time = time.time() - start
        print(f"   ⏱️  Total time: {sleep_time:.2f} seconds")
        print("   ❌ Wastes time even if alert appears earlier")
        print("   ❌ Fails if alert takes longer than 3 seconds")
        
    finally:
        driver1.quit()
    
    # ========== Test 2: Explicit Wait (GOOD PRACTICE) ==========
    print("\n2️⃣  Using Explicit Wait - WebDriverWait (GOOD):")
    print("-" * 50)
    
    driver2 = setup_driver()
    try:
        start = time.time()
        
        driver2.get("https://www.lambdatest.com/selenium-playground/")
        bootstrap_link = driver2.find_element(By.LINK_TEXT, "Bootstrap Alerts")
        bootstrap_link.click()
        time.sleep(2)
        
        success_button = driver2.find_element(By.XPATH, "//button[contains(text(), 'Success Message')]")
        success_button.click()
        
        # ✅ GOOD: Explicit wait - waits up to 10 seconds
        print("   ⏳ Waiting for alert (dynamic wait - up to 10 seconds)...")
        wait = WebDriverWait(driver2, 10)
        alert = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success"))
        )
        print(f"   ✅ Alert found using explicit wait")
        print(f"   ✅ Alert text: '{alert.text}'")
        
        explicit_time = time.time() - start
        print(f"   ⏱️  Total time: {explicit_time:.2f} seconds")
        print("   ✅ Only waits as long as needed")
        print("   ✅ Works on both fast and slow machines")
        
    except TimeoutException:
        print("   ❌ Timeout: Alert not found within 10 seconds")
    finally:
        driver2.quit()
    
    # ========== Conclusion ==========
    print("\n📊 COMPARISON SUMMARY:")
    print("-" * 50)
    print(f"   time.sleep(3) took:     {sleep_time:.2f} seconds")
    print(f"   Explicit wait took:     {explicit_time:.2f} seconds")
    print("\n   ✅ Explicit wait is FASTER on fast machines")
    print("   ✅ Explicit wait is MORE RELIABLE on slow machines")
    print("   ✅ Explicit wait stops as soon as element appears")
    print("   ❌ time.sleep() wastes time even if element appears early")
    print("   ❌ time.sleep() fails if element takes longer than 3 seconds")
    print("\n" + "=" * 70)


# ============================================================
# STEP 38: element_to_be_clickable
# ============================================================
def step_38_element_clickable():
    """
    Demonstrate EC.element_to_be_clickable vs visibility
    """
    print("\n" + "=" * 70)
    print("STEP 38: element_to_be_clickable vs visibility")
    print("=" * 70)
    
    driver = setup_driver()
    
    try:
        driver.get("https://www.lambdatest.com/selenium-playground/")
        bootstrap_link = driver.find_element(By.LINK_TEXT, "Bootstrap Alerts")
        bootstrap_link.click()
        time.sleep(2)
        
        print("\n📚 Understanding Wait Conditions:")
        print("-" * 50)
        
        print("\n   🔍 visibility_of_element_located:")
        print("   • Checks if element is present in DOM AND visible")
        print("   • Does NOT check if element is enabled or clickable")
        print("   • Example: A disabled button is visible but not clickable")
        print("   • Use when: You just need the element to be visible")
        
        print("\n   🔍 element_to_be_clickable:")
        print("   • Checks if element is visible AND enabled AND not obscured")
        print("   • Waits for element to be ready for interaction")
        print("   • Example: A button that is grayed out (disabled) fails this check")
        print("   • Use when: You are about to click on the element")
        
        print("\n🔍 Demonstration:")
        print("-" * 50)
        
        # ✅ Wait for button to be clickable
        print("   ⏳ Waiting for button to be clickable...")
        wait = WebDriverWait(driver, 10)
        button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Success Message')]"))
        )
        
        print("   ✅ Button found and is clickable!")
        print(f"   📝 Button text: '{button.text}'")
        print(f"   ✓ Is button enabled? {button.is_enabled()}")
        print(f"   ✓ Is button displayed? {button.is_displayed()}")
        
        # Click the button
        button.click()
        print("   ✅ Button clicked successfully!")
        
        print("\n💡 SUMMARY:")
        print("-" * 50)
        print("   visibility_of_element_located: Element is visible")
        print("   element_to_be_clickable:       Element is visible AND enabled AND not obscured")
        print("\n   ⚠️ ALWAYS use element_to_be_clickable before clicking elements!")
        
    except TimeoutException:
        print("❌ Timeout: Element not clickable within 10 seconds")
    except Exception as e:
        print(f"❌ Error: {str(e)[:200]}")
    finally:
        driver.quit()
        print("\n" + "=" * 70)


# ============================================================
# STEP 39: FluentWait Implementation
# ============================================================
def step_39_fluent_wait():
    """
    Implement FluentWait - polling every 500ms with ignored exceptions
    """
    print("\n" + "=" * 70)
    print("STEP 39: FluentWait - Custom Polling")
    print("=" * 70)
    
    driver = setup_driver()
    
    try:
        # Navigate to Table Sort Demo
        driver.get("https://www.lambdatest.com/selenium-playground/")
        table_link = driver.find_element(By.LINK_TEXT, "Table Data Search")
        table_link.click()
        time.sleep(2)
        
        print("\n⌛ Waiting for table to load with FluentWait...")
        print("-" * 50)
        
        # ✅ FLUENTWAIT IMPLEMENTATION
        # Poll every 500ms for up to 10 seconds
        # Ignore NoSuchElementException during polling
        
        print("   ⏱️  Configuration:")
        print("      • Timeout: 10 seconds")
        print("      • Poll frequency: 500ms (0.5 seconds)")
        print("      • Ignored exceptions: NoSuchElementException")
        
        wait = WebDriverWait(driver, 10, poll_frequency=0.5)
        wait.ignored_exceptions = [NoSuchElementException]
        
        # Wait for table to be present
        print("\n   🔍 Searching for table...")
        table = wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "table"))
        )
        
        print("   ✅ Table found successfully!")
        print(f"   📝 Table tag: {table.tag_name}")
        
        # Get table rows
        rows = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//table//tr"))
        )
        print(f"   📊 Number of rows: {len(rows)}")
        
        print("\n📋 FLUENTWAIT PROPERTIES:")
        print("-" * 50)
        print("   ✅ Polling every 500ms (not every second)")
        print("   ✅ Maximum wait time: 10 seconds")
        print("   ✅ Stops as soon as condition is met")
        print("   ✅ More efficient than time.sleep()")
        print("   ✅ More flexible than implicit wait")
        
    except TimeoutException:
        print("❌ Timeout: Table not found within 10 seconds")
    except Exception as e:
        print(f"❌ Error: {str(e)[:200]}")
    finally:
        driver.quit()
        print("\n" + "=" * 70)


# ============================================================
# BONUS: All Expected Conditions Reference
# ============================================================
def bonus_expected_conditions_reference():
    """
    Complete reference of all expected conditions
    """
    print("\n" + "=" * 70)
    print("BONUS: Expected Conditions Reference")
    print("=" * 70)
    
    reference = """
    📚 COMPLETE EXPECTED CONDITIONS REFERENCE
    
    ═══════════════════════════════════════════════════════════════════
    
    1️⃣  ELEMENT PRESENCE & VISIBILITY
        ──────────────────────────────────────────────────────────────
        • presence_of_element_located(locator)
          → Element exists in DOM (may not be visible)
          → Use: When checking if element is loaded
        
        • visibility_of_element_located(locator)
          → Element is present AND visible
          → Use: Before interacting with visible elements
        
        • visibility_of(element)
          → Same as above but with WebElement object
          → Use: When you already have the element
        
        • invisibility_of_element_located(locator)
          → Element is not visible or not present
          → Use: After clicking to wait for element to disappear
        
        • presence_of_all_elements_located(locator)
          → All matching elements are present
          → Use: When checking multiple elements
    
    2️⃣  ELEMENT INTERACTION
        ──────────────────────────────────────────────────────────────
        • element_to_be_clickable(locator)
          → Element is visible AND enabled AND not obscured
          → Use: BEFORE clicking any button/link
        
        • element_to_be_selected(element)
          → Element is selected (checkbox/radio)
          → Use: To verify selection state
        
        • element_selection_state_to_be(element, is_selected)
          → Selection state matches expected
          → Use: To verify expected selection state
        
        • staleness_of(element)
          → Element is no longer attached to DOM
          → Use: After page refresh or dynamic updates
    
    3️⃣  TEXT & ATTRIBUTES
        ──────────────────────────────────────────────────────────────
        • text_to_be_present_in_element(locator, text_)
          → Text appears in element
          → Use: To verify specific text
        
        • text_to_be_present_in_element_value(locator, text_)
          → Text appears in value attribute
          → Use: To verify input field value
        
        • text_to_be_present_in_element_attribute(locator, attr, text_)
          → Text appears in specific attribute
          → Use: To verify attribute values
    
    4️⃣  FRAMES & WINDOWS
        ──────────────────────────────────────────────────────────────
        • frame_to_be_available_and_switch_to_it(locator)
          → Frame is available and ready
          → Use: Before interacting with iframe content
        
        • number_of_windows_to_be(num)
          → Number of windows matches expected
          → Use: After opening new window/tab
    
    5️⃣  ALERTS
        ──────────────────────────────────────────────────────────────
        • alert_is_present()
          → JavaScript alert dialog appears
          → Use: To handle alert popups
    
    6️⃣  URL & TITLE
        ──────────────────────────────────────────────────────────────
        • title_is(title)
          → Page title matches exactly
          → Use: To verify page loaded correctly
        
        • title_contains(title)
          → Page title contains text
          → Use: For partial title verification
        
        • url_contains(url)
          → URL contains text
          → Use: To verify navigation
        
        • url_to_be(url)
          → URL matches exactly
          → Use: To verify exact page location
    
    ═══════════════════════════════════════════════════════════════════
    
    💡 BEST PRACTICE TIPS:
    • Always use the most specific condition for your need
    • Use element_to_be_clickable before clicking
    • Use visibility_of_element_located before interacting
    • Use presence_of_element_located when only checking existence
    • Avoid time.sleep() - use explicit waits instead
    """
    
    print(reference)


# ============================================================
# BONUS: Wait Best Practices
# ============================================================
def bonus_wait_best_practices():
    """
    Summary of wait best practices
    """
    print("\n" + "=" * 70)
    print("BONUS: Wait Best Practices Summary")
    print("=" * 70)
    
    best_practices = """
    💡 WAIT BEST PRACTICES GUIDE
    
    ═══════════════════════════════════════════════════════════════════
    
    ✅ DO's:
    
    1. Use WebDriverWait with expected_conditions for specific elements
       ✅ wait.until(EC.visibility_of_element_located((By.ID, "element")))
    
    2. Use element_to_be_clickable before clicking
       ✅ wait.until(EC.element_to_be_clickable((By.ID, "button")))
    
    3. Use visibility_of_element_located before interacting
       ✅ wait.until(EC.visibility_of_element_located((By.ID, "input")))
    
    4. Set appropriate timeouts (5-10 seconds is usually enough)
       ✅ WebDriverWait(driver, 10)
    
    5. Use FluentWait for custom polling needs
       ✅ WebDriverWait(driver, 10, poll_frequency=0.5)
    
    6. Handle TimeoutException gracefully
       ✅ try: wait.until(...) except TimeoutException: handle_error()
    
    ❌ DON'Ts:
    
    1. NEVER use time.sleep() in production tests
       ❌ time.sleep(3)  # WRONG!
    
    2. Avoid implicit waits (they're global and slow)
       ❌ driver.implicitly_wait(10)  # NOT RECOMMENDED
    
    3. Don't mix implicit and explicit waits
       ❌ driver.implicitly_wait(10) + WebDriverWait(...)  # BAD!
    
    4. Don't use excessive wait times
       ❌ WebDriverWait(driver, 60)  # Too long!
    
    5. Don't ignore TimeoutException
       ❌ wait.until(...)  # No try-except
    
    ═══════════════════════════════════════════════════════════════════
    
    ⚠️ REMEMBER:
    • Explicit waits are specific to elements
    • Each wait condition serves a different purpose
    • Choose the right condition for the right situation
    • Always provide a reasonable timeout (5-10 seconds)
    • Consider page load times in different environments
    • Tests should be reliable, not just fast
    """
    
    print(best_practices)


# ============================================================
# Main Execution
# ============================================================
if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("HANDS-ON 5: TASK 2 - EXPLICIT WAITS")
    print("Target: LambdaTest Selenium Playground")
    print("=" * 70 + "\n")
    
    # Run all steps
    step_36_bootstrap_alerts()
    step_37_wait_comparison()
    step_38_element_clickable()
    step_39_fluent_wait()
    bonus_expected_conditions_reference()
    bonus_wait_best_practices()
    
    print("\n" + "=" * 70)
    print("✅ TASK 2 COMPLETED SUCCESSFULLY!")
    print("=" * 70)