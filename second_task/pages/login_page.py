from .base_page import BasePage
from .locators import LoginPageLocators
from .credentials import LoginCredentials


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()

    def should_be_login_url(self):
        print(self.browser.current_url)
        assert (self.browser.current_url ==
                "https://www.avito.ru/sochi/lichnye_veschi?cd=1&d=1#login?authsrc=h"), "Invalid url or url has been changed"

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM), "Login link is not presented"

    def login_action(self):
        self.find_element(
            *LoginPageLocators.LOGIN_NAME).send_keys(LoginCredentials.login_name)
        self.find_element(
            *LoginPageLocators.LOGIN_PASSWORD).send_keys(LoginCredentials.password)
        self.find_element(*LoginPageLocators.ENTER_BUTTON).click()
