from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from Tools.test_data import *
from time import sleep

class EHRStatus:
    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 10)
        self.driver = driver

    def amb_ehr_status(self, test_data):

        # Open block
        ehr_block = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div/div[7]/div/div')
        ehr_block.click()
        sleep(1)
    
        # Patient ehr form
        patient_ehr_form = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div/div[7]/div/div[2]/div/div/div/div/div/form/div/div[1]/div[1]/div/div/div/div[1]/label[2]/div/span')
        patient_ehr_form.click()
        patient_ehr_status = self.driver.find_element(By.XPATH, '//*[@placeholder="{}"]'.format(ehr_approval_status))
        patient_ehr_status.click()
        form = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div/div[7]/div/div[2]/div/div/div/div/div/form/div/div[2]/div[1]/div/div/div/div/div[2]/div/div/li[1]/div/span')
        form.click()

        # Click the print button
        print_ehr = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div/div[7]/div/div[2]/div/div/div/div/div/form/div/div[2]/div[2]/div/button')
        print_ehr.click()
        sleep(5)
        self.driver.refresh()

class EHRStatusStac:
    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 10)
        self.driver = driver

    def stac_ehr_status(self, test_data):

        # Open block
        ehr_block = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div/div[7]/div/div/div[2]')
        ehr_block.click()
        sleep(1)
    
        # Patient ehr form
        patient_ehr_form = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div/div[7]/div/div[2]/div/div/div/div/div/form/div/div[1]/div[1]/div/div/div/div[1]/label[2]/div/span')
        patient_ehr_form.click()
        patient_ehr_status = self.driver.find_element(By.XPATH, '//*[@placeholder="{}"]'.format(ehr_approval_status))
        patient_ehr_status.click()
        form = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div/div[7]/div/div[2]/div/div/div/div/div/form/div/div[2]/div[1]/div/div/div/div/div[2]/div/div/li[1]/div/span')
        form.click()

        # Click the print button
        print_ehr = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div/div[7]/div/div[2]/div/div/div/div/div/form/div/div[2]/div[2]/div/button')
        print_ehr.click()
        sleep(5)
        self.driver.refresh()
        sleep(2)
