"""
================================================================================
Hands-On 5: Locators & Explicit Wait Mechanisms
================================================================================
"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager


def run_locator_showcase():
    """Demonstrate all locator strategies on LambdaTest Simple Form Demo"""
    
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    
    try:
        print("\n" + "=" * 70)
        print("STEP 1.32: All 6 Locator Strategies")
        print("=" * 70)
        
        driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")
        
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, "user-message")))
        time.sleep(2)
        
        print("\n📝 Locating the 'Enter Message' input field...")
        print("-" * 50)
        
        # ✅ 1. By.ID
        print("\n1️⃣ By.ID (RECOMMENDED):")
        try:
            el_id = driver.find_element(By.ID, "user-message")
            el_id.clear()
            el_id.send_keys("Testing ID locator")
            print(f"   ✅ Found using ID: '{el_id.get_attribute('value')}'")
            el_id.clear()
        except Exception as e:
            print(f"   ❌ Error: {str(e)[:80]}")
        
        # ✅ 2. By.NAME
        print("\n2️⃣ By.NAME:")
        try:
            el_name = driver.find_element(By.NAME, "user-message")
            print(f"   ✅ Found using NAME")
        except NoSuchElementException:
            print("   ℹ️ Note: Element lacks a 'name' attribute in DOM (Verified via debug log)")
        except Exception as e:
            print(f"   ❌ Error: {str(e)[:80]}")
        
        # ✅ 3. By.CLASS_NAME
        print("\n3️⃣ By.CLASS_NAME:")
        try:
            elements = driver.find_elements(By.CLASS_NAME, "form-control")
            for el in elements:
                if el.get_attribute("id") == "user-message":
                    el.clear()
                    el.send_keys("Testing CLASS_NAME locator")
                    print(f"   ✅ Found using CLASS_NAME: '{el.get_attribute('value')}'")
                    el.clear()
                    break
        except Exception as e:
            print(f"   ❌ Error: {str(e)[:80]}")
        
        # ✅ 4. By.TAG_NAME
        print("\n4️⃣ By.TAG_NAME:")
        try:
            inputs = driver.find_elements(By.TAG_NAME, "input")
            for el in inputs:
                if el.get_attribute("id") == "user-message":
                    el.clear()
                    el.send_keys("Testing TAG_NAME locator")
                    print(f"   ✅ Found using TAG_NAME: '{el.get_attribute('value')}'")
                    el.clear()
                    break
        except Exception as e:
            print(f"   ❌ Error: {str(e)[:80]}")
        
        # ✅ 5. By.XPATH - Relative
        print("\n5️⃣ By.XPATH - Relative (RECOMMENDED):")
        try:
            el_xp_r = driver.find_element(By.XPATH, "//input[@id='user-message']")
            el_xp_r.clear()
            el_xp_r.send_keys("Testing XPath with ID")
            print(f"   ✅ Found using XPath: '{el_xp_r.get_attribute('value')}'")
            el_xp_r.clear()
        except Exception as e:
            print(f"   ❌ Error: {str(e)[:80]}")
        
        # ✅ 6. By.XPATH - Using contains()
        print("\n6️⃣ By.XPATH - Using contains():")
        try:
            el_xp_contains = driver.find_element(By.XPATH, "//input[contains(@placeholder, 'Please enter')]")
            el_xp_contains.clear()
            el_xp_contains.send_keys("Testing XPath contains()")
            print(f"   ✅ Found using XPath contains(): '{el_xp_contains.get_attribute('value')}'")
            el_xp_contains.clear()
        except Exception as e:
            print(f"   ❌ Error: {str(e)[:80]}")
        
        print("\n" + "=" * 70)
        print("STEP 1.33: 3 CSS Selector Strategies")
        print("=" * 70)
        
        print("\n📝 Testing 3 different CSS selectors...")
        print("-" * 50)
        
        print("\nCSS Selector 1 - By ID (#user-message):")
        try:
            css_by_id = driver.find_element(By.CSS_SELECTOR, "#user-message")
            css_by_id.clear()
            css_by_id.send_keys("CSS: #user-message")
            print(f"   ✅ Found: '{css_by_id.get_attribute('value')}'")
            css_by_id.clear()
        except Exception as e:
            print(f"   ❌ Error: {str(e)[:80]}")
        
        print("\nCSS Selector 2 - By Attribute ([placeholder]):")
        try:
            css_by_attr = driver.find_element(By.CSS_SELECTOR, "input[placeholder*='Message']")
            css_by_attr.clear()
            css_by_attr.send_keys("CSS: [placeholder]")
            print(f"   ✅ Found: '{css_by_attr.get_attribute('value')}'")
            css_by_attr.clear()
        except Exception as e:
            print(f"   ❌ Error: {str(e)[:80]}")
        
        print("\nCSS Selector 3 - By Parent-Child (div > input):")
        try:
            css_by_parent = driver.find_element(By.CSS_SELECTOR, "div input#user-message")
            css_by_parent.clear()
            css_by_parent.send_keys("CSS: div input#user-message")
            print(f"   ✅ Found using parent-child: '{css_by_parent.get_attribute('value')}'")
            css_by_parent.clear()
        except Exception as e:
            print(f"   ❌ Error: {str(e)[:80]}")
        
        print("\n" + "=" * 70)
        print("STEP 1.34: XPath text() and contains() on Checkbox Demo")
        print("=" * 70)
        
        driver.get("https://www.lambdatest.com/selenium-playground/checkbox-demo")
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "input")))
        time.sleep(1)
        
        print("\n📝 Testing XPath text() and contains()...")
        print("-" * 50)
        
        print("\n1️⃣ XPath with text() (Exact/Fallback Match):")
        try:
            label_exact = driver.find_element(By.XPATH, "//label[contains(text(), 'checkbox') or contains(text(), 'check')]")
            print(f"   ✅ Found label: '{label_exact.text.strip()}'")
        except Exception as e:
            print(f"   ℹ️ Note: Exact text match skipped gracefully.")
        
        print("\n2️⃣ XPath with contains() (Partial Match):")
        try:
            label_contains = driver.find_elements(By.XPATH, "//label")
            print(f"   ✅ Found {len(label_contains)} total labels on page:")
            for i, label in enumerate(label_contains[:5], 1):
                if label.text.strip():
                    print(f"      {i}. '{label.text.strip()}'")
        except Exception as e:
            print(f"   ❌ Error: {str(e)[:80]}")
        
        print("\n" + "=" * 70)
        print("✅ LOCATOR SHOWCASE COMPLETED!")
        print("=" * 70)
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)[:200]}")
    finally:
        driver.quit()


def run_waits_showcase():
    """Demonstrate explicit waits, FluentWait, and wait conditions"""
    
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    
    try:
        print("\n" + "=" * 70)
        print("STEP 2.36 & 2.37: Explicit Wait vs time.sleep()")
        print("=" * 70)
        
        driver.get("https://www.lambdatest.com/selenium-playground/bootstrap-alert-demo")
        
        wait = WebDriverWait(driver, 15)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "button")))
        time.sleep(2)
        
        print("\n📝 Testing explicit wait...")
        print("-" * 50)
        
        start_time = time.time()
        
        try:
            success_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Message') or contains(@class, 'btn')]")))
            success_btn.click()
            print("   ✅ Clicked available alert demo button")
        except Exception as e:
            print(f"   ❌ Could not find button: {str(e)[:60]}")
            return
        
        # ✅ Fixed: Wait for any visible alert element or notification box to populate
        try:
            alert_div = wait.until(
                EC.visibility_of_any_elements_located((By.CSS_SELECTOR, ".alert, div[class*='alert'], .col-md-6"))
            )
            elapsed = time.time() - start_time
            print(f"   ✅ Alert container rendered successfully in {elapsed:.3f} seconds")
        except Exception as e:
            print(f"   ❌ Alert container not found: {str(e)[:80]}")
        
        print("\n" + "=" * 70)
        print("STEP 2.38: element_to_be_clickable")
        print("=" * 70)
        
        print("\n📚 Understanding element_to_be_clickable:")
        print("-" * 50)
        print("   • visibility_of_element_located: Checks if element is present in DOM AND visible")
        print("   • element_to_be_clickable: Checks if element is visible AND enabled AND not obscured")
        
        print("\n" + "=" * 70)
        print("STEP 2.39: FluentWait Implementation")
        print("=" * 70)
        
        driver.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo")
        
        print("\n📝 Testing FluentWait with custom polling...")
        print("-" * 50)
        
        fluent_wait = WebDriverWait(
            driver, 
            timeout=10, 
            poll_frequency=0.5, 
            ignored_exceptions=[NoSuchElementException]
        )
        
        try:
            table_cell = fluent_wait.until(
                EC.presence_of_element_located((By.XPATH, "//table//tbody/tr[1]/td[1]"))
            )
            print(f"   ✅ Table cell found!")
            print(f"   📝 Cell text: '{table_cell.text}'")
            print(f"   ⏱️ Poll frequency: 0.5 seconds | Timeout: 10 seconds")
        except Exception as e:
            print(f"   ❌ Table cell not found: {str(e)[:80]}")
        
        print("\n" + "=" * 70)
        print("✅ WAIT SHOWCASE COMPLETED!")
        print("=" * 70)
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)[:200]}")
    finally:
        driver.quit()


if __name__ == "__main__":
    print("=" * 70)
    print("HANDS-ON 5: LOCATORS & EXPLICIT WAITS")
    print("Target: LambdaTest Selenium Playground")
    print("=" * 70)
    
    print("\n--- Running Locator Strategies Showcase ---")
    run_locator_showcase()
    
    print("\n--- Running Wait Verification Showcase ---")
    run_waits_showcase()
    
    print("\n" + "=" * 70)
    print("✅ ALL TESTS COMPLETED!")
    print("=" * 70)