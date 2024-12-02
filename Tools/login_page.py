from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import Tools.test_data as test_data
from time import sleep

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_textbox = (By.ID, ':r0:')
        self.password_textbox = (By.ID, ':r1:')
        self.login_button = (By.XPATH, '//*[@id="root"]/div/div/div[2]/form/button')

    def open_page(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        self.driver.find_element(*self.username_textbox).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()