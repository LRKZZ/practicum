from pages.login_po import LoginPage
from pages.inventory_po import InventoryPage
from pages.cart_po import CartPage

def test_add_and_remove_multiple_items(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    page.goto("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")

    item_ids = ["sauce-labs-backpack", "sauce-labs-bike-light", "sauce-labs-bolt-t-shirt"]
    for item_id in item_ids:
        inventory_page.add_to_cart(item_id)
    
    inventory_page.open_cart()
    cart_items = cart_page.get_cart_items()
    assert len(cart_items) == len(item_ids), "Количество товаров в корзине не совпадает"

    for item_id in item_ids:
        cart_page.remove_from_cart(item_id)
    
    cart_items = cart_page.get_cart_items()
    assert len(cart_items) == 0, "Корзина должна быть пуста"
