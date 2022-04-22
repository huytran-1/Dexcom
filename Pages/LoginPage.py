from Locators.locators import LoginPageLocators
from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_txtbox = LoginPageLocators.user_name
        self.password_txtbox = LoginPageLocators.password
        self.submit_button = LoginPageLocators.login_button

    def enter_username(self, username):
        self.driver.find_element(By.CSS_SELECTOR, self.username_txtbox).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.username_txtbox).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.CSS_SELECTOR, self.password_txtbox).click()
        self.driver.find_element(By.CSS_SELECTOR, self.password_txtbox).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.password_txtbox).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.CSS_SELECTOR, self.submit_button).click()
