"""
Debug script to find correct locators on LambdaTest site
Run this to see what elements are actually on the page
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def setup_driver():
    options = Options()
    options.add_argument('--start-maximized')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def debug_checkbox_page(driver):
    """Debug Checkbox Demo page to find correct locators"""
    print("\n" + "="*60)
    print("DEBUG: CHECKBOX DEMO PAGE")
    print("="*60)
    
    driver.get("https://www.lambdatest.com/selenium-playground/checkbox-demo")
    time.sleep(3)
    
    print("\n--- All input elements ---")
    inputs = driver.find_elements(By.TAG_NAME, "input")
    for i, inp in enumerate(inputs):
        print(f"  {i}: type={inp.get_attribute('type')}, id={inp.get_attribute('id')}, class={inp.get_attribute('class')}")
    
    print("\n--- All labels ---")
    labels = driver.find_elements(By.TAG_NAME, "label")
    for label in labels:
        print(f"  Label text: '{label.text}', for={label.get_attribute('for')}")
    
    print("\n--- All buttons ---")
    buttons = driver.find_elements(By.TAG_NAME, "button")
    for btn in buttons:
        print(f"  Button text: '{btn.text}', id={btn.get_attribute('id')}, class={btn.get_attribute('class')}")
    
    print("\n--- All divs with IDs ---")
    divs = driver.find_elements(By.XPATH, "//div[@id]")
    for div in divs:
        print(f"  Div id: {div.get_attribute('id')}")

def debug_input_form_page(driver):
    """Debug Input Form Demo page to find correct locators"""
    print("\n" + "="*60)
    print("DEBUG: INPUT FORM DEMO PAGE")
    print("="*60)
    
    driver.get("https://www.lambdatest.com/selenium-playground/input-form-demo")
    time.sleep(3)
    
    print("\n--- All input elements ---")
    inputs = driver.find_elements(By.TAG_NAME, "input")
    for i, inp in enumerate(inputs):
        print(f"  {i}: type={inp.get_attribute('type')}, id={inp.get_attribute('id')}, placeholder={inp.get_attribute('placeholder')}, name={inp.get_attribute('name')}")
    
    print("\n--- All textarea elements ---")
    textareas = driver.find_elements(By.TAG_NAME, "textarea")
    for ta in textareas:
        print(f"  Textarea: id={ta.get_attribute('id')}, placeholder={ta.get_attribute('placeholder')}")
    
    print("\n--- All buttons ---")
    buttons = driver.find_elements(By.TAG_NAME, "button")
    for btn in buttons:
        print(f"  Button text: '{btn.text}', type={btn.get_attribute('type')}, class={btn.get_attribute('class')}")
    
    print("\n--- All divs with class containing 'alert' or 'success' ---")
    alerts = driver.find_elements(By.XPATH, "//div[contains(@class, 'alert') or contains(@class, 'success')]")
    for alert in alerts:
        print(f"  {alert.get_attribute('class')}: {alert.text[:50]}")

def debug_dropdown_page(driver):
    """Debug Dropdown Demo page to find correct locators"""
    print("\n" + "="*60)
    print("DEBUG: DROPDOWN DEMO PAGE")
    print("="*60)
    
    driver.get("https://www.lambdatest.com/selenium-playground/select-dropdown-demo")
    time.sleep(3)
    
    print("\n--- All select elements ---")
    selects = driver.find_elements(By.TAG_NAME, "select")
    for sel in selects:
        print(f"  Select: id={sel.get_attribute('id')}, class={sel.get_attribute('class')}")
        options = sel.find_elements(By.TAG_NAME, "option")
        print(f"    Options: {[opt.text for opt in options]}")
    
    print("\n--- All divs with class containing 'selected' ---")
    divs = driver.find_elements(By.XPATH, "//div[contains(@class, 'selected')]")
    for div in divs:
        print(f"  Div: class={div.get_attribute('class')}, text={div.text}")

def debug_simple_form_page(driver):
    """Debug Simple Form Demo page to find correct locators"""
    print("\n" + "="*60)
    print("DEBUG: SIMPLE FORM DEMO PAGE")
    print("="*60)
    
    driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")
    time.sleep(3)
    
    print("\n--- All input elements ---")
    inputs = driver.find_elements(By.TAG_NAME, "input")
    for i, inp in enumerate(inputs):
        print(f"  {i}: type={inp.get_attribute('type')}, id={inp.get_attribute('id')}, placeholder={inp.get_attribute('placeholder')}")
    
    print("\n--- All buttons ---")
    buttons = driver.find_elements(By.TAG_NAME, "button")
    for btn in buttons:
        print(f"  Button text: '{btn.text}', id={btn.get_attribute('id')}, class={btn.get_attribute('class')}")
    
    print("\n--- All divs with IDs ---")
    divs = driver.find_elements(By.XPATH, "//div[@id]")
    for div in divs:
        print(f"  Div id: {div.get_attribute('id')}, text: {div.text[:50]}")

def main():
    driver = setup_driver()
    try:
        debug_simple_form_page(driver)
        debug_checkbox_page(driver)
        debug_dropdown_page(driver)
        debug_input_form_page(driver)
    finally:
        print("\n" + "="*60)
        print("DEBUG COMPLETE - Press Enter to close browser")
        input()
        driver.quit()

if __name__ == "__main__":
    main()