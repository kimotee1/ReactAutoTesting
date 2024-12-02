from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Tools.test_data import *
from time import sleep

class AmbulatoryCasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_text(self, placeholder_text, value):
        """Enter text into an input field identified by its placeholder attribute."""
        field = self.wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@placeholder="{placeholder_text}"]')))
        field.clear()
        field.send_keys(value)
        sleep(1)  # Pause for 2 seconds after entering text

    def click_button(self, xpath):
        """Wait for a button to be clickable and then click it."""
        button = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        button.click()
        sleep(1)  # Pause for 2 seconds after clicking the button

    def ambulatory_case(self, test_data):
        """Fill out the form for an ambulatory case."""

        # Enter personal details (ID, first name, last name)
        self.enter_text(pn0, num)
        self.enter_text(name0, test)
        self.enter_text(lastname0, test)

        # Click 'Search' button
        self.click_button('//*[@id="root"]/div/div[2]/div/div[2]/div[1]/div/div[3]/button')
        sleep(3)

        # Select gender
        gender_dropdown = self.wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@placeholder="{gender0}"]')))
        gender_dropdown.click()
        sleep(1)  # Pause before selecting gender option
        gender_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div/div[1]/div[1]/div[7]/div/div[2]/div/div/li[1]/div/span')))
        gender_option.click()
        sleep(1)  # Pause after gender selection

        # Enter date of birth
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="{}"]'.format(birth0)))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="{}"]'.format(birth0)))).send_keys(birth)
        sleep(1)

        # Enter address
        address_field = self.driver.find_element(By.XPATH, f'//*[@placeholder="{address01}"]')
        address_field.click()
        sleep(1)  # Pause before selecting address
        address_select = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div[1]/div[2]/div[1]/div/div[2]/div/div[2]/li[1]/div/span')
        address_select.click()
        sleep(1)  # Pause after selecting address
        self.enter_text(address02, test)

        # Click 'Submit Address' button
        self.click_button('//*[@id="root"]/div/div[2]/div/div[2]/div/div[1]/div[2]/div[3]/div/button')

        # Enter mobile number
        self.enter_text(mobnumber, number1)
        self.enter_text(mobnumber0, number2)

        # Enter email address
        self.enter_text(mail0, mail)

        # Scroll to the bottom of the page
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)  # Pause for 3 seconds before attempting to click 'Create Case'

        # Click 'Create Case' button
        creat_case = self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div/div[2]/div/div[5]/div[2]/button[2]').click()
        sleep(1)
