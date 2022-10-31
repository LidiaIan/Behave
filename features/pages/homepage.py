from selenium.webdriver.common.by import By


class Homepage:

    URL = "https://the-internet.herokuapp.com"
    FORM_AUTHENTICATION_SELECTOR = (By.LINK_TEXT, "Form Authentication")
    SECURE_FILE_SELECTOR = (By.LINK_TEXT, "Secure File Download")
    ADD_ELEMENTS_SELECTOR= (By.LINK_TEXT, "Add/Remove Elements")

    def __int__(self, driver):
        self.driver = driver

    def go_home(self):
        self.driver.get(self.URL)

    def go_to(self, url_text):
        element = self.driver.find_element(By.LINK_TEXT, url_text)
        element.click()