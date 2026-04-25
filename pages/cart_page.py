from playwright.sync_api import Page, expect

class CartPage:

    def __init__(self, page: Page):
        self.page = page
        self.page_title = page.locator(".title")
        self.item_quantity = page.locator('[data-test="item-quantity"]')
        self.item_name = page.locator('[data-test="inventory-item-name"]')
        self.checkout_continue = page.locator('[data-test="checkout"]')
        
    def check_cart_page_opened(self):
        expect(self.page_title).to_have_text("Your Cart")

    def check_item_quantity(self, quantity: str):
        expect(self.item_quantity).to_have_text(quantity)

    def check_item_name(self, item_name: str):
        expect(self.item_name).to_have_text(item_name)

    def continue_to_flow(self):
        self.checkout_continue.click()
    