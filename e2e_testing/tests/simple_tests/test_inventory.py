from pages.login_po import LoginPage
from pages.inventory_po import InventoryPage
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_add_to_cart(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    
    page.goto("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_to_cart("sauce-labs-backpack")
    inventory_page.open_cart()
    
    assert page.is_visible("div.inventory_item_name")
