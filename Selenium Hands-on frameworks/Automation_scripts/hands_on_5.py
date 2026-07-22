import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

"""
TASK 1, STEP 35: LOCATOR STRATEGY RANKINGS (Most to Least Preferred)
1. By.ID: Most preferred. It is highly unique, fastest to query, and very readable.
2. By.CSS_SELECTOR: Extremely fast, versatile, and readable. Preferred when an ID is not available.
3. By.NAME / By.CLASS_NAME: Good if they are unique, but often multiple elements share the same name or class.
4. By.XPATH (Relative): Slower than CSS, but essential for complex DOM traversal.
5. By.TAG_NAME: Generally too broad unless dealing with highly specific elements.
6. By.XPATH (Absolute): Least preferred/Worst. Highly brittle and breaks if a single div or span is added/removed.
"""

def run_hands_on_5():
    # Setup WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    try:
        # ==========================================
        # TASK 1: LOCATOR STRATEGIES
        # ==========================================
        print("--- Starting Task 1: Locator Strategies ---")
        
        # 1. Simple Form Demo - Find same element 6 ways
        driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")
        
        id_loc = driver.find_element(By.ID, "user-message")
        
        # Handling the missing 'name' attribute gracefully
        try:
            name_loc = driver.find_element(By.NAME, "user-message")
        except NoSuchElementException:
            print("Note: The 'name' attribute is missing on this specific element in the LambdaTest DOM, but By.NAME syntax is correct.")
            
        class_loc = driver.find_element(By.CLASS_NAME, "w-full") 
        tag_loc = driver.find_elements(By.TAG_NAME, "input")[0] 
        xpath_abs = driver.find_element(By.XPATH, "/html/body/div[1]/div/section[2]/div/div/div/div[1]/div[2]/div/div[1]/input")
        xpath_rel = driver.find_element(By.XPATH, "//input[@id='user-message']")
        
        print("Successfully executed the 6 standard locator strategies.")

        # 2. Simple Form Demo - Find same element using 3 CSS Selectors
        css_id = driver.find_element(By.CSS_SELECTOR, "#user-message")
        css_attr = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Please enter your Message']")
        css_parent_child = driver.find_element(By.CSS_SELECTOR, "div > input#user-message")
        
        print("Successfully found message input using 3 CSS Selector strategies.")

        # 3. Checkbox Demo - XPath text() and contains()
        driver.get("https://www.lambdatest.com/selenium-playground/checkbox-demo")
        
        exact_text_label = driver.find_element(By.XPATH, "//label[text()='Option 1']")
        contains_text_labels = driver.find_elements(By.XPATH, "//label[contains(text(), 'Option')]")
        
        print(f"Found exact label: '{exact_text_label.text}'")
        print(f"Found {len(contains_text_labels)} labels containing the word 'Option'.")


        # ==========================================
        # TASK 2: EXPLICIT WAITS & EXPECTED CONDITIONS
        # ==========================================
        print("\n--- Starting Task 2: Explicit Waits ---")
        driver.get("https://www.lambdatest.com/selenium-playground/bootstrap-alert-messages-demo")

        # 1. WebDriverWait & Assertions
        success_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Normal Success')]")
        success_btn.click()
        
        # Wait for the success alert to become visible
        wait = WebDriverWait(driver, 10)
        success_alert = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success")))
        assert "successfully" in success_alert.text.lower(), "Alert text does not contain 'successfully'"
        print("Explicit wait for visibility successful and assertion passed.")

        # 2. time.sleep() vs Explicit Wait demonstration
        driver.refresh()
        time.sleep(1) # Small buffer for refresh
        btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Normal Success')]")
        
        # Measure time.sleep()
        start_sleep = time.time()
        btn.click()
        time.sleep(3) # Hard-coded sleep
        sleep_duration = time.time() - start_sleep
        print(f"time.sleep(3) took: {sleep_duration:.2f} seconds")

        driver.refresh()
        time.sleep(1)
        btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Normal Success')]")
        
        # Measure explicit wait
        start_wait = time.time()
        btn.click()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success")))
        wait_duration = time.time() - start_wait
        print(f"Explicit wait took: {wait_duration:.2f} seconds")
        
        # 3. element_to_be_clickable
        clickable_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Normal Success')]")))
        print("Wait for element to be clickable successful.")

        # 4. Fluent Wait implementation
        fluent_wait = WebDriverWait(
            driver, 
            timeout=10, 
            poll_frequency=0.5, 
            ignored_exceptions=[NoSuchElementException]
        )
        
        driver.refresh()
        driver.find_element(By.XPATH, "//button[contains(text(), 'Normal Success')]").click()
        fluent_alert = fluent_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success")))
        print("Fluent wait (polling every 500ms) successfully located the alert.")

    finally:
        driver.quit()

if __name__ == "__main__":
    run_hands_on_5()