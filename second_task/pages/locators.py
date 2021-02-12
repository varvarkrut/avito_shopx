from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (
        By.CSS_SELECTOR,
        "[data-marker='header/login-button']")


class PersonalItemsLocators():
    ITEM = (By.CSS_SELECTOR, "[itemprop=name]:nth-child(1)")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "[class=auth-app-login-form-2_SQa]")
    LOGIN_NAME = (By.CSS_SELECTOR, "[data-marker='login-form/login']")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "[data-marker='login-form/password']")
    ENTER_BUTTON = (
        By.CSS_SELECTOR,
        "[class='auth-form-auth-form__submit-rSWaC']")


class ItemPageLocators():
    THE_BUY_BUTTON = (
        By.CSS_SELECTOR,
        '[data-marker="delivery-item-button-main"]')


class OrderPageLocators():
    THE_PHONE_FIELD = (
        By.CSS_SELECTOR,
        '[data-marker="sd/order-widget-field/phone"]')
