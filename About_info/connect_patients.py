from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Tools.test_data import *
from time import sleep

class AmbulatoryConnectPatient:
    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 10)
        self.driver = driver

    def amb_connect_patient_button(self, test_data):

        # Click button
        connect_button = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div/div[3]/div/div[2]/div/div/div/div/div/div[1]/button/span')
        actions = ActionChains(self.driver)
        actions.double_click(connect_button).perform()
        sleep(1)
        connect_again_click = self.driver.find_element(By.XPATH, '//*[@id="add-related-connection"]/button').click()
        sleep(1)

        # Choose connect patient
        choose_patient_dropdown = self.driver.find_element(By.XPATH, '//*[@placeholder="{}"]'.format(connect_patient)).click()
        sleep(1)
        choose_patient_number = self.driver.find_element(By.ID, 'pd_related_patient').send_keys(pnnumber)
        sleep(1)
        choose_patient_button = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/li/div/span')
        choose_patient_button.click()

        # Choose patient type
        choose_patient_type = self.driver.find_element(By.XPATH, '//*[@placeholder="{}"]'.format(patient_type)).click()
        sleep(1)
        choose_patient_type_button = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/li[5]/div/span')
        choose_patient_type_button.click()
        sleep(1)

        # Choose connect type
        choose_connect_type = self.driver.find_element(By.XPATH,'//*[@id="add-related-connection"]/div[2]/div[4]/div/div[1]/div/div' ).click()
        sleep(1)
        choose_connect_type_button = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/li[5]/div/span')
        choose_connect_type_button.click()

        # Connect save
        connect_save_button = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/button[1]')
        connect_save_button.click()
        sleep(1)

class StationaryConnectPatient:
    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 10)
        self.driver = driver

    def stac_connect_patient_button(self, test_data):

        # Click button
        connect_button = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div/div[3]/div/div[2]/div/div/div/div/div/div[1]/button')
        actions = ActionChains(self.driver)
        actions.double_click(connect_button).perform()
        sleep(1)
        connect_again_click = self.driver.find_element(By.XPATH, '//*[@id="add-related-connection"]/button').click()
        sleep(1)

        # Choose connect patient
        choose_patient_dropdown = self.driver.find_element(By.XPATH, '//*[@placeholder="{}"]'.format(connect_patient)).click()
        sleep(2)
        choose_patient_number = self.driver.find_element(By.ID, 'pd_related_patient').send_keys(pnnumber)
        sleep(1)
        choose_patient_button = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/li/div/span')
        choose_patient_button.click()

        # Choose patient type
        choose_patient_type = self.driver.find_element(By.XPATH, '//*[@placeholder="{}"]'.format(patient_type)).click()
        sleep(1)
        choose_patient_type_button = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/li[5]/div/span')
        choose_patient_type_button.click()
        sleep(1)

        # Choose connect type
        choose_connect_type = self.driver.find_element(By.XPATH,'//*[@id="add-related-connection"]/div[2]/div[4]/div/div[1]/div/div' ).click()
        sleep(1)
        choose_connect_type_button = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/li[5]/div/span')
        choose_connect_type_button.click()

        # Connect save
        connect_save_button = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/button[1]')
        connect_save_button.click()
        sleep(1)