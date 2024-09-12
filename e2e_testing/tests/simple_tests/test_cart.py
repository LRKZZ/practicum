from pages.login_po import LoginPage
from pages.inventory_po import InventoryPage
from pages.cart_po import CartPage
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_checkout(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    
    page.goto("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_to_cart("sauce-labs-backpack")
    inventory_page.open_cart()
    cart_page.checkout()
    cart_page.fill_checkout_info("John", "Doe", "12345")
    cart_page.finish_checkout()
    
    assert page.is_visible("h2.complete-header")
