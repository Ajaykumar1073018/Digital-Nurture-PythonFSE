from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def navigate_to(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def wait_for_element(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        # UPGRADE: Scroll to the CENTER of the screen to avoid sticky headers!
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        return self.wait.until(EC.element_to_be_clickable(locator))
        
    def wait_for_text(self, locator, text):
        self.wait.until(EC.text_to_be_present_in_element(locator, text))
        
    def js_click(self, locator):
        # UPGRADE: A universal JavaScript click to pierce through any overlapping UI menus
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].click();", element)