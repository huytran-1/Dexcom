import pytest
from selenium import webdriver


class Base:

    @pytest.fixture(autouse=True)
    def set_up(self):
        print("Initiating Chrome driver")
        self.driver = webdriver.Chrome(executable_path="./Drivers/chromedriver.exe")
        print("-----------------------------------------")
        print("Test is started")
        self.driver.implicitly_wait(20)
        self.driver.get("https://clarity.dexcom.com")
        self.driver.maximize_window()

        yield self.driver
        if self.driver is not None:
            print("-----------------------------------------")
            print("Tests is finished")
            self.driver.close()
            self.driver.quit()