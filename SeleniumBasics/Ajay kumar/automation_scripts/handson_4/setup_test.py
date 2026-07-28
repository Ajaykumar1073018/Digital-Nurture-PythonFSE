"""
HANDS-ON 4: Selenium WebDriver Setup, Browser Drivers & Basic Commands
Complete solution for all tasks
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# ============================================================
# TASK 24: Architecture Description
# ============================================================
"""
SELENIUM ARCHITECTURE COMPONENTS:

1. WebDriver:
   - A remote control interface that enables programmatic control of browsers
   - Communicates with the browser via browser-specific drivers (ChromeDriver, GeckoDriver, etc.)
   - Uses JSON Wire Protocol to send commands and receive responses

2. Selenium Grid:
   - Solves the problem of running tests on multiple machines/browsers simultaneously
   - Enables parallel execution across different OS and browser combinations
   - Consists of a Hub (central controller) and Nodes (execution environments)

3. Selenium IDE:
   - A browser extension for record-and-playback of test actions
   - Generates code in multiple languages
   - Useful for quick prototyping and learning
"""


# ============================================================
# TASK 25 & 26: Setup with waits
# ============================================================
def task_25_26_basic_setup():
    """Basic WebDriver setup with implicit wait"""
    print("\n=== TASK 25 & 26: Basic Setup with Implicit Wait ===")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    # Implicit wait - waits up to 10 seconds
    driver.implicitly_wait(10)
    
    """
    WHY IMPLICIT WAIT IS CONSIDERED BAD PRACTICE:
    
    1. Global Application: Applies to every find_element call
    2. Performance Impact: Slows down all element searches
    3. Hard to Debug: Difficult to know which element is causing the wait
    4. No Exception Details: Hides the actual reason for failure
    
    Better: Explicit waits using WebDriverWait
    """
    
    driver.get("https://www.lambdatest.com/selenium-playground/")
    print(f"Page Title: {driver.title}")
    driver.quit()


# ============================================================
# TASK 27: Headless Mode
# ============================================================
def task_27_headless_mode():
    """Run browser in headless mode"""
    print("\n=== TASK 27: Headless Mode ===")
    
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1920,1080')
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    driver.get("https://www.lambdatest.com/selenium-playground/")
    print(f"Page Title (headless): {driver.title}")
    driver.quit()


# ============================================================
# TASK 28: Navigation Commands
# ============================================================
def task_28_navigation_commands():
    """Test navigation commands: get, click, back, URL assertion"""
    print("\n=== TASK 28: Navigation Commands ===")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    driver.get("https://www.lambdatest.com/selenium-playground/")
    
    # Click Simple Form Demo link (adjust selector as needed)
    simple_form_link = driver.find_element(By.LINK_TEXT, "Simple Form Demo")
    simple_form_link.click()
    
    # Assert URL contains 'simple-form-demo'
    assert 'simple-form-demo' in driver.current_url
    print(f"URL after click: {driver.current_url}")
    
    # Navigate back
    driver.back()
    print(f"URL after back: {driver.current_url}")
    
    driver.quit()


# ============================================================
# TASK 29: Multiple Windows/Tabs
# ============================================================
def task_29_multiple_windows():
    """Handle multiple browser tabs"""
    print("\n=== TASK 29: Multiple Windows/Tabs ===")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    driver.get("https://www.lambdatest.com/selenium-playground/")
    
    # Store original window handle
    original_window = driver.current_window_handle
    print(f"Original window: {original_window}")
    
    # Open new tab
    driver.execute_script('window.open("https://www.google.com");')
    time.sleep(2)
    
    # Get all window handles
    window_handles = driver.window_handles
    print(f"Number of windows: {len(window_handles)}")
    
    # Switch to new tab
    driver.switch_to.window(window_handles[1])
    print(f"New tab title: {driver.title}")
    
    driver.quit()


# ============================================================
# TASK 30: Screenshot
# ============================================================
def task_30_screenshot():
    """Take screenshot and switch between tabs"""
    print("\n=== TASK 30: Screenshot ===")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    driver.get("https://www.lambdatest.com/selenium-playground/")
    original_window = driver.current_window_handle
    
    # Open new tab
    driver.execute_script('window.open("https://www.google.com");')
    time.sleep(2)
    
    # Switch back to original
    driver.switch_to.window(original_window)
    
    # Take screenshot
    driver.save_screenshot('playground_screenshot.png')
    print("Screenshot saved as 'playground_screenshot.png'")
    
    driver.quit()


# ============================================================
# TASK 31: Window Size
# ============================================================
def task_31_window_size():
    """Get and set window size"""
    print("\n=== TASK 31: Window Size Management ===")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    driver.get("https://www.lambdatest.com/selenium-playground/")
    
    # Get current size
    current_size = driver.get_window_size()
    print(f"Current size: {current_size}")
    
    # Set new size
    driver.set_window_size(1280, 800)
    print(f"New size: {driver.get_window_size()}")
    
    """
    WHY CONSISTENT WINDOW SIZE MATTERS:
    
    1. Layout Consistency: Different sizes trigger different CSS breakpoints
    2. Element Visibility: Elements may appear/hide based on size
    3. Positioning: Element coordinates change with window size
    4. Reproducibility: Same test should produce same results
    5. Responsive Testing: Testing mobile vs desktop views
    """
    
    driver.quit()


# ============================================================
# Run all tasks
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("RUNNING HANDS-ON 4: ALL TASKS")
    print("=" * 60)
    
    # Run each task
    tasks = [
        task_25_26_basic_setup,
        task_27_headless_mode,
        task_28_navigation_commands,
        task_29_multiple_windows,
        task_30_screenshot,
        task_31_window_size
    ]
    
    for task in tasks:
        try:
            task()
        except Exception as e:
            print(f"Error in {task.__name__}: {e}")
    
    print("\n" + "=" * 60)
    print("ALL TASKS COMPLETED")
    print("=" * 60)