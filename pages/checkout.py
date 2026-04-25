import re   
from playwright.sync_api import Page , expect

class CheckoutPage:
    def __init__(self , page : Page):
        self.page = page
        self.first_name = page.locator('[data-test="firstName"]')
        self.last_name = page.locator('[data-test="lastName"]')
        self.postal_code = page.locator('[data-test="postalCode"]')
        self.continue_click = page.locator('[data-test="continue"]')
        self.finish_click = page.locator('[data-test="finish"]')
        self.page_title = page.locator(".title")
        self.success_message = page.locator('[data-test="complete-header"]')
        self.error_message = page.locator('[data-test="error"]')

    def fill_checkout_info(self, first_name: str, last_name: str, postal_code: str):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.postal_code.fill(postal_code)

    def click_continue(self):
        self.continue_click.click()

    def check_overview_page(self):
        expect(self.page_title).to_have_text("Checkout: Overview")

    def click_finish(self):
        self.finish_click.click()

    def check_order_success(self):
        expect(self.success_message).to_have_text("Thank you for your order!")

    def check_error_visible(self):
        expect(self.error_message).to_be_visible()