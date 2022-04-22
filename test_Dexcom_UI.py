
import pytest
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.DexcomClarity import DexcomClarity
from Base.base import Base


@pytest.mark.usefixtures('set_up')
class TestDexcomUI(Base):
    def test_login_successfully(self):
        driver = self.driver
        homepage = HomePage(driver)
        login = LoginPage(driver)
        clarity = DexcomClarity(driver)
        homepage.click_home_user_button()
        login.enter_username("nilepatest001")
        login.enter_password("Password@1")
        login.click_login()

        try:
            assert "Installing Dexcom Uploader software is required to upload glucose data." == clarity.get_installing_text()
        except Exception as e:
            raise
            print("Wrong text", format(e))

