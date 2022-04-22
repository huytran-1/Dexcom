from selenium.webdriver.common.by import By
from Locators.locators import DexcomClarityLocators


class DexcomClarity:
    def __init__(self, driver):
        self.driver = driver
        self.installing_text = DexcomClarityLocators.installing_text

    def get_installing_text(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.installing_text).text
