class CartPage:
    def __init__(self, page):
        self.page = page
        self.checkout_button = "button#checkout"
        self.first_name_input = "input#first-name"
        self.last_name_input = "input#last-name"
        self.postal_code_input = "input#postal-code"
        self.continue_button = "input#continue"
        self.finish_button = "button#finish"
        self.cart_item_locator = ".cart_item"
        self.remove_button_prefix = "button[id='remove-"
        self.error_message = "h3[data-test='error']"

    def checkout(self):
        self.page.click(self.checkout_button)

    def fill_checkout_info(self, first_name, last_name, postal_code):
        self.page.fill(self.first_name_input, first_name)
        self.page.fill(self.last_name_input, last_name)
        self.page.fill(self.postal_code_input, postal_code)
        self.page.click(self.continue_button)

    def finish_checkout(self):
        self.page.click(self.finish_button)

    def get_cart_items(self):
        return self.page.locator(self.cart_item_locator).all_text_contents()

    def remove_from_cart(self, item_id):
        self.page.click(f"{self.remove_button_prefix}{item_id}']")

    def continue_checkout(self):
        self.page.click(self.continue_button)

    def is_checkout_error_displayed(self):
        return self.page.is_visible(self.error_message)
