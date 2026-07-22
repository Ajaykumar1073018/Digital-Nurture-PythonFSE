"""
SELENIUM ARCHITECTURE COMPONENTS:
- WebDriver: An API that allows you to control the browser natively, communicating directly with it to execute actions.
- Selenium Grid: A tool that solves the problem of cross-browser testing by allowing parallel test execution on multiple machines and browsers at the same time.
- Selenium IDE: A browser extension used for rapid test creation via record and playback, and for code generation.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def run_hands_on_4():
    # Setup ChromeOptions for headless mode
    options = Options()
    options.add_argument('--headless')
    
    # Import Chrome WebDriver using webdriver-manager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    # Add implicit wait
    driver.implicitly_wait(10)
    # COMMENT: Setting implicit wait globally is considered bad practice because it applies 
    # for the lifetime of the WebDriver instance. Mixing it with explicit waits can cause 
    # unpredictable timeout behaviors and slow down test execution significantly when elements are truly missing.

    try:
        # Navigate to the LambdaTest Selenium Playground
        driver.get("https://www.lambdatest.com/selenium-playground/")
        
        # Verify title is printed correctly in headless mode
        print("Playground Title:", driver.title)

        # Demonstrate getting window size
        print("Initial Window Size:", driver.get_window_size())
        
        # Set window size
        driver.set_window_size(1280, 800)
        # COMMENT: Consistent window size matters for responsive UI automation because 
        # applications render differently based on screen dimensions. Ensuring a set size 
        # prevents flaky tests caused by elements being hidden, resized, or obscured by mobile menus.

        # Navigate to the Simple Form Demo page by clicking the link
        driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()

        # Assert the URL contains 'simple-form-demo'
        assert 'simple-form-demo' in driver.current_url
        print("URL Assertion Passed. Current URL:", driver.current_url)

        # Navigate back to the previous page
        driver.back()

        # Open a new browser tab to Google
        driver.execute_script('window.open("https://www.google.com");')

        # List all open tabs and switch to the new tab (index 1)
        tabs = driver.window_handles
        driver.switch_to.window(tabs[1])
        
        # Print the title of the Google tab
        print("New Tab Title:", driver.title)

        # Switch back to the original tab (index 0)
        driver.switch_to.window(tabs[0])

        # Take a screenshot and save it
        driver.save_screenshot('playground_screenshot.png')
        print("Screenshot successfully saved as 'playground_screenshot.png'")

    finally:
        # Close the browser instance
        driver.quit()

if __name__ == "__main__":
    run_hands_on_4()