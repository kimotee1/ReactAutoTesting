from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Tools.test_data import *
from time import sleep

class AmbulatoryCaseInfo:
    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 10)
        self.driver = driver

    def amb_police_number(self, test_data):

        # Click button
        add_police_button = self.driver.find_element(By.XPATH, '//*[@id="active_insurance"]/div/div/div/div[1]/div/div/button').click()
        sleep(2)

        # Choose contragent
        counterparty_dropdown = self.driver.find_element(By.XPATH, '//*[@placeholder="{}"]'.format(contragent))
        counterparty_dropdown.click()
        sleep(1)
        counterparty_text = self.driver.find_element(By.ID, 'pd_insurance_company')
        counterparty_text.click()
        counterparty_text.send_keys(counterparty_name)
        sleep(1)
        sleep(1)
        counterparty_choose = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/li[1]')
        sleep(1)
        counterparty_choose.click()

        # Choose insurance
        insurance_package = self.driver.find_element(By.XPATH, '//*[@placeholder="{}"]'.format(insurance_package_name))
        insurance_package.click()
        sleep(2)
        insurance_package_choose = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/li[1]')
        insurance_package_choose.click()
        sleep(1)
        
        # Choose insurer
        insurer_text = self.driver.find_element(By.XPATH, '//*[@placeholder="{}"]'.format(insurer))
        insurer_text.send_keys(test)
    
    def amb_plastic_card(self, test_data):

        # Serie and Number
        serie = self.driver.find_element(By.XPATH, '//*[@placeholder="{}"]'.format(serie_name))
        serie.send_keys(number1)
        number = self.driver.find_element(By.XPATH, '//*[@placeholder="{}"]'.format(serie_number))
        number.send_keys(number1)
        
        issue_data = self.driver.find_element(By.XPATH, '//*[@placeholder="{}"]'.format(issue_data_name)).click()
        issue_data = self.driver.find_element(By.XPATH, '//*[@placeholder="{}"]'.format(issue_data_name)).send_keys(birth)

        unknown_checkbox = self.driver.find_element(By.XPATH,'//*[@id="add-insurance-policy"]/div[2]/div[3]/div[2]/label/div/span/input').click()

        save = self.driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/div[2]/button[1]').click()
        sleep(1)


class StationaryCaseInfo:
    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 10)
        self.driver = driver

    def stac_police_number(self, test_data):

        # Click button
        add_police_button = self.driver.find_element(By.XPATH, '//*[@id="active_insurance"]/div/div/div/div[1]/div/div/button').click()
        sleep(1)

        # Choose contragent
        counterparty_dropdown = self.driver.find_element(By.XPATH, '//*[@placeholder="{}"]'.format(contragent))
        counterparty_dropdown.click()
        sleep(1)
        counterparty_text = self.driver.find_element(By.ID, 'pd_insurance_company')
        counterparty_text.click()
        sleep(3)
        counterparty_text.send_keys(counterparty_name)
        sleep(2)
        counterparty_choose = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/li[1]')
        sleep(1)
        counterparty_choose.click()

        # Choose insurance
        insurance_package = self.driver.find_element(By.XPATH, '//*[@placeholder="{}"]'.format(insurance_package_name))
        insurance_package.click()
        sleep(2)
        insurance_package_choose = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/li[1]')
        insurance_package_choose.click()
        sleep(1)
        
        # Choose insurer
        insurer_text = self.driver.find_element(By.XPATH, '//*[@placeholder="{}"]'.format(insurer))
        insurer_text.send_keys(test)
    
    def stac_plastic_card(self, test_data):

        # Serie and Number
        serie = self.driver.find_element(By.XPATH, '//*[@placeholder="{}"]'.format(serie_name))
        serie.send_keys(number1)
        number = self.driver.find_element(By.XPATH, '//*[@placeholder="{}"]'.format(serie_number))
        number.send_keys(number1)
        
        issue_data = self.driver.find_element(By.XPATH, '//*[@placeholder="{}"]'.format(issue_data_name)).click()
        issue_data = self.driver.find_element(By.XPATH, '//*[@placeholder="{}"]'.format(issue_data_name)).send_keys(birth)

        unknown_checkbox = self.driver.find_element(By.XPATH,'//*[@id="add-insurance-policy"]/div[2]/div[3]/div[2]/label/div/span/input').click()

        save = self.driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/div[2]/button[1]').click()
        sleep(1)
        