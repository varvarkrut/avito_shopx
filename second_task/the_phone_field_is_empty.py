from .pages.personal_items_page import PersonalItemsPage
from .pages.login_page import LoginPage
from .pages.item_page import ItemPage
from .pages.order_page import OrderPage


def test_login_link(browser):

    link = "https://www.avito.ru/sochi/lichnye_veschi?cd=1&d=1"
    page = PersonalItemsPage(browser, link)
    page.open()

    page.go_to_login_page()

    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    login_page.login_action()
    page.go_to_item_page()
    page = ItemPage(browser, browser.current_url)
    page.click_on_buy_item_button()
    page = OrderPage(browser, browser.current_url)
    page.the_phone_field_is_empty()
