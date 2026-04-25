import re   
from playwright.sync_api import Page, expect
from pages.loginp import LoginPage

def test_valid_login(page):

    login = LoginPage(page)
    page.goto("https://www.saucedemo.com/")
    login.login("standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator(".title")).to_have_text("Products")


def test_invalid_login(page):
    login_page = LoginPage(page)
    page.goto("https://www.saucedemo.com/")
    login_page.login("wrong_user", "wrong_pass")
    expect(page.locator('[data-test="error"]')).to_be_visible()