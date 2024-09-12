class CartPage:
    def __init__(self, page):
        self.page = page

    def checkout(self):
        self.page.click("button#checkout")

    def fill_checkout_info(self, first_name, last_name, postal_code):
        self.page.fill("input#first-name", first_name)
        self.page.fill("input#last-name", last_name)
        self.page.fill("input#postal-code", postal_code)
        self.page.click("input#continue")

    def finish_checkout(self):
        self.page.click("button#finish")

    def get_cart_items(self):
        return self.page.locator(".cart_item").all_text_contents()

    def remove_from_cart(self, item_id):
        self.page.click(f"button[id='remove-{item_id}']")

    def continue_checkout(self):
        self.page.click("input#continue")

    def is_checkout_error_displayed(self):
        return self.page.is_visible("h3[data-test='error']")
