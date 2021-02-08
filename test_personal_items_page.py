from .pages.personal_items_page import PersonalItemsPage
import time


def test_item_exist_and_clickable(browser):
    link = "https://www.avito.ru/sochi/lichnye_veschi?cd=1&d=1"
    page = PersonalItemsPage(browser, link)
    page.open()
    page.go_to_item_page()
    time.sleep(5)