from pages.login_po import LoginPage
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_login_success(page):
    login_page = LoginPage(page)
    page.goto("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    assert page.url == "https://www.saucedemo.com/inventory.html"
