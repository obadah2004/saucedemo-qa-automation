from playwright.sync_api import Page ,expect
from pages.cart_page import CartPage
from pages.loginp import LoginPage
from pages.inventory_page import InventoryPage
def test_cart_page(page: Page):
    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)

    page.goto("https://www.saucedemo.com/")
    login.login("standard_user", "secret_sauce")

    inventory.add_first_item()
    inventory.open_cart()
    cart.check_cart_page_opened()
    cart.check_item_quantity("1")
    cart.check_item_name("Sauce Labs Backpack")
    cart.continue_to_flow()