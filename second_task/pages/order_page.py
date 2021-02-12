from .base_page import BasePage
from .locators import OrderPageLocators


class OrderPage(BasePage):
    def the_phone_field_is_empty(self):
        self.the_phone_field_is_exitsts()
        self.browser.execute_script("window.scrollTo(0, 5000)")
        phone_field = self.browser.find_element(
            *OrderPageLocators.THE_PHONE_FIELD)
        phone_field_value = phone_field.get_attribute("value")

        assert phone_field_value == "", "The phone field is not empty!"
         
    def the_phone_field_is_exitsts(self):
        assert self.is_element_present(*OrderPageLocators.THE_PHONE_FIELD), \
            "THe phone field does not exist"
