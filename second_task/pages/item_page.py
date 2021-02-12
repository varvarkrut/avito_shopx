from .base_page import BasePage
from .locators import ItemPageLocators


class ItemPage(BasePage):
    def buy_button_exitst_and_clickable(self):
        assert self.is_element_present(
            *ItemPageLocators.THE_BUY_BUTTON), "The Buy button not exist \
            or not clickable"

    def click_on_buy_item_button(self):
        link = self.browser.find_element(*ItemPageLocators.THE_BUY_BUTTON)
        self.buy_button_exitst_and_clickable()
        link.click()
        self.browser.switch_to.window(self.browser.window_handles[1])
