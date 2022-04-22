
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


#
#
# @pytest.fixture(autouse=True, scope='function')
# def setup(request):
#     global driver
#     driver = webdriver.Chrome("./features/chromedriver")
#
#     def fin():
#         driver.quit()
#         request.addfinalizer(fin)
#
#
# @scenario('UI\DexComUI.feature', 'Testing DexCom webpage with login')
# def test_testing_dexcom_webpage_with_login():
#     """Testing DexCom webpage with login."""
#
#
# @given('I am on DexCom website')
# def i_am_on_dexcom_website(self):
#     """I am on DexCom website."""
#     driver = self.driver
#
# @then('I click on DexCom login')
# def i_click_on_dexcom_login():
#     """I click on DexCom login."""
#     raise NotImplementedError
#
#
# @then('I enter login credential')
# def i_enter_login_credential():
#     """I enter login credential."""
#     raise NotImplementedError
#
#
# @then('I verify login successfully')
# def i_verify_login_successfully():
#     """I verify login successfully."""
#     raise NotImplementedError
