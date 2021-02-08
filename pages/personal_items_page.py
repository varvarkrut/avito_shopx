from .base_page import BasePage
from selenium.webdriver.common.by import By


class PersonalItemsPage(BasePage):
    def go_to_item_page(self):
        login_link = self.browser.find_element(
            By.CSS_SELECTOR, '#i2045404879 > div:nth-child(1) > div.iva-item-slider-37uKh > a > div > div > ul > li > div > img')
        login_link.click()
