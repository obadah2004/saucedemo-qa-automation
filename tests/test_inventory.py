import re
from playwright.sync_api import Page , expect
from pages.loginp import LoginPage
from pages.inventory_page import InventoryPage

def test_add_to_cart(page : Page):
    login = LoginPage(page)
    inventory = InventoryPage(page)
    page.goto("https://www.saucedemo.com/")
    login.login("standard_user" , "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    inventory.add_first_item()
    inventory.check_cart_count("1")


def test_remove_from_cart(page: Page):
    login = LoginPage(page)
    inventory = InventoryPage(page)
    page.goto("https://www.saucedemo.com/")
    login.login("standard_user", "secret_sauce")
    inventory.add_first_item()
    inventory.check_cart_count("1")
    inventory.click_remove_button()
    inventory.check_cart_empty()


