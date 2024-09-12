class InventoryPage:
    def __init__(self, page):
        self.page = page

    def add_to_cart(self, item_id):
        self.page.click(f"button[id='add-to-cart-{item_id}']")

    def open_cart(self):
        self.page.click("a.shopping_cart_link")

    def sort_by(self, sort_type):
        self.page.select_option("select.product_sort_container", sort_type)

    def get_item_prices(self):
        prices = self.page.locator(".inventory_item_price").all_text_contents()
        return [float(price.replace('$', '')) for price in prices]

    def add_all_items_to_cart(self):
        item_buttons = self.page.locator("button.btn_inventory").all()
        for button in item_buttons:
            button.click()

    def get_cart_count(self):
        cart_count_text = self.page.locator(".shopping_cart_badge").text_content()
        return int(cart_count_text) if cart_count_text else 0

    def get_total_item_count(self):
        return len(self.page.locator(".inventory_item").all())
