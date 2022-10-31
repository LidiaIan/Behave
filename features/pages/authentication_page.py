
class Authentication:
    URL = "https://the-internet.herokuapp.com/login"
    PAGE_TITLE = "Login Page"


    def __int__(self, driver):
        self.driver = driver

    def go_home(self):
        self.driver.get(self.URL)

    def input_username(self, username):
        username_element = self.driver.find_element()
        username_element.send_keys(username)

    def input_password(self, password):
        password_element = self.driver.find_element()
        password_element.send.keys(password)

    def submit_login(self):
        self.submit_login.click
