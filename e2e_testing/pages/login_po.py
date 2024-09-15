class LoginPage:
    def __init__(self, page):
        self.page = page
        # Локаторы
        self.username_input = "input#user-name"
        self.password_input = "input#password"
        self.login_button = "input#login-button"

    def login(self, username, password):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)
