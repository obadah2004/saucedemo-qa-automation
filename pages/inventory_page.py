import re   
from playwright.sync_api import Page , expect

class InventoryPage:

    def __init__(self, page: Page):
        self.page = page
        self.add_to_cart_button = page.locator('[data-test="add-to-cart-sauce-labs-backpack"]')
        self.cart_badge = page.locator('.shopping_cart_badge')
        self.remove_button = page.locator('[data-test="remove-sauce-labs-backpack"]')
        self.cart_link = page.locator('[data-test="shopping-cart-link"]')

    def add_first_item(self):
        self.add_to_cart_button.click()

    def check_cart_count(self, count: str):
        expect(self.cart_badge).to_have_text(count)
    
    def click_remove_button(self):
        self.remove_button.click()

    def check_cart_empty(self):
        expect(self.cart_badge).to_have_count(0)

    def open_cart(self):
        self.cart_link.click()