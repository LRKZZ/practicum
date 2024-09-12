class LoginPage:
    def __init__(self, page):
        self.page = page

    def login(self, username, password):
        self.page.fill("input#user-name", username)
        self.page.fill("input#password", password)
        self.page.click("input#login-button")
