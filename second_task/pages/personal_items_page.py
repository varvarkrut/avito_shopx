from .base_page import BasePage
from .locators import PersonalItemsLocators


class PersonalItemsPage(BasePage):

    def go_to_item_page(self):
        self.first_item_exitst_and_clickable()
        link = self.browser.find_element(*PersonalItemsLocators.ITEM)
        link.click()
        self.browser.switch_to.window(self.browser.window_handles[1])

    def first_item_exitst_and_clickable(self):
        assert self.is_element_present(*PersonalItemsLocators.ITEM), \
            "First item not exist or not clickable"
