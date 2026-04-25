from playwright.sync_api import Page , expect
from pages.loginp import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout import CheckoutPage

def test_checkout_flow(page: Page):
    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)
    page.goto("https://www.saucedemo.com/")
    login.login("standard_user", "secret_sauce")
    inventory.add_first_item()
    inventory.open_cart()
    cart.check_cart_page_opened()
    cart.continue_to_flow()
    checkout.fill_checkout_info("Obadah", "Test", "12345")
    checkout.click_continue()
    checkout.check_overview_page()
    checkout.finish_click.click()
    checkout.check_order_success()


def test_checkout_empty_fields(page: Page):
        login = LoginPage(page)
        inventory = InventoryPage(page)
        cart = CartPage(page)
        checkout = CheckoutPage(page)
        page.goto("https://www.saucedemo.com/")
        login.login("standard_user", "secret_sauce")
        inventory.add_first_item()
        inventory.open_cart()
        cart.continue_to_flow()
        checkout.click_continue()
        checkout.check_error_visible()


def test_checkout_missing_first_name(page: Page):
    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)
    page.goto("https://www.saucedemo.com/")
    login.login("standard_user", "secret_sauce")
    inventory.add_first_item()
    inventory.open_cart()
    cart.continue_to_flow()
    checkout.fill_checkout_info("", "Test", "12345")
    checkout.click_continue()
    checkout.check_error_visible()