class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.add_to_cart_button_prefix = "button[id='add-to-cart-"
        self.cart_link = "a.shopping_cart_link"
        self.sort_container = "select.product_sort_container"
        self.item_price_locator = ".inventory_item_price"
        self.add_all_buttons = "button.btn_inventory"
        self.cart_badge = ".shopping_cart_badge"
        self.inventory_item = ".inventory_item"

    def add_to_cart(self, item_id):
        self.page.click(f"{self.add_to_cart_button_prefix}{item_id}']")

    def open_cart(self):
        self.page.click(self.cart_link)

    def sort_by(self, sort_type):
        self.page.select_option(self.sort_container, sort_type)

    def get_item_prices(self):
        prices = self.page.locator(self.item_price_locator).all_text_contents()
        return [float(price.replace('$', '')) for price in prices]

    def add_all_items_to_cart(self):
        item_buttons = self.page.locator(self.add_all_buttons).all()
        for button in item_buttons:
            button.click()

    def get_cart_count(self):
        cart_count_text = self.page.locator(self.cart_badge).text_content()
        return int(cart_count_text) if cart_count_text else 0

    def get_total_item_count(self):
        return len(self.page.locator(self.inventory_item).all())
