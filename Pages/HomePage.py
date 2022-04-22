from selenium.webdriver.common.by import By
from Locators.locators import HomePageLocators

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.home_users_button = HomePageLocators.home_users_button

    def click_home_user_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.home_users_button).click()
