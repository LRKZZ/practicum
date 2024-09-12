from pages.login_po import LoginPage
from pages.inventory_po import InventoryPage
from pages.cart_po import CartPage

def test_cart_persistence_after_logout(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    page.goto("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")

    item_names = ["Sauce Labs Backpack", "Sauce Labs Bike Light"]
    for item_id in ["sauce-labs-backpack", "sauce-labs-bike-light"]:
        inventory_page.add_to_cart(item_id)

    cart_count = inventory_page.get_cart_count()
    assert cart_count == len(item_names), f"Ожидалось, что в корзине будет {len(item_names)} товара(ов), но их {cart_count}"

    page.click("button#react-burger-menu-btn")
    page.click("a#logout_sidebar_link")

    assert page.url == "https://www.saucedemo.com/", "Ожидался переход на страницу логина после выхода"

    login_page.login("standard_user", "secret_sauce")

    inventory_page.open_cart()
    cart_items = cart_page.get_cart_items()

    print(f"Товары в корзине после повторного входа: {cart_items}")

    assert len(cart_items) == len(item_names), f"Ожидалось, что в корзине будет {len(item_names)} товара(ов) после повторного входа, но их {len(cart_items)}"

    for item_name in item_names:
        assert any(item_name in item for item in cart_items), f"Товар {item_name} не найден в корзине после повторного входа"
