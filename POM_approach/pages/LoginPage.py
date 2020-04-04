class LoginPage():
    # -------------------------------------------------------------------------------------//Locator of the all elements
    textbox_email_by_id = "Email"
    textbox_password_by_id = "Password"
    button_login_by_xpath = "//input[@value='Log in']"
    link_login_link_by_text = "John Smith"
    link_logout_link_by_text = "Logout"

    # -------------------------------------------------------------------------------------// Constructor
    def __init__(self, driver):
        self.driver = driver

    # -------------------------------------------------------------------------------------// Methods
    def set_user_name(self, username):
        self.driver.find_element_by_id(self.textbox_email_by_id).send_keys(username)

    def set_user_password(self, password):
        self.driver.find_element_by_id(self.textbox_password_by_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.button_login_by_xpath).click()

    def login_name_check(self, name):
        self.driver.find_element_by_text(self.link_login_link_by_text)

    def click_logout(self):
        self.driver.find_element_by_text(self.link_logout_link_by_text).click()
    # -------------------------------------------------------------------------------------//
    # -------------------------------------------------------------------------------------//
