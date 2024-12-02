from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Tools.test_data import *
from time import sleep
import logging

class AmbulatorySocialanamnesis:
    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 10)
        self.driver = driver

    def amb_social_anamnes(self, test_data):

        # Employment
        employment = self.driver.find_element(By.XPATH,'//*[@placeholder="{}"]'.format(employments)).click()
        sleep(2)
        employment_button = self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div/div[2]/div/div[5]/div/div[2]/div/div/div/div/div/div/div[1]/div[1]/div/div[2]/div/div[2]/li[2]/div/span')
        employment_button.click()

        # Physical limited
        physical_limited = self.driver.find_element(By.XPATH,'//*[@placeholder="{}"]'.format(physical)).click()
        sleep(1)
        physical_limited_button = self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div/div[2]/div/div[5]/div/div[2]/div/div/div/div/div/div/div[1]/div[3]/div/div[2]/div/div[2]/li[4]/div/span')
        physical_limited_button.click()

        # Education
        education_dropdown = self.driver.find_element(By.XPATH,'//*[@placeholder="{}"]'.format(education)).click()
        sleep(1)
        education_button = self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div/div[2]/div/div[5]/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div[2]/div/div[2]/li[1]/div/span')
        education_button.click()

        # Number of sons 
        number_of_sons = self.driver.find_element(By.XPATH,'//*[@placeholder="{}"]'.format(suns)).send_keys(test_number)
        sleep(1)

        # workplace
        workplace = self.driver.find_element(By.XPATH,'//*[@placeholder="{}"]'.format(workplaces)).send_keys(test)
        sleep(1)

        # Additional information
        additional_information = self.driver.find_element(By.XPATH,'//*[@placeholder="{}"]'.format(additional)).send_keys(test)
        sleep(1)

        # Save all info
        save_all_info = self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div/div[2]/div/div[6]/div[2]/button[2]')
        save_all_info.click()
        sleep(1)

class StationarySocialanamnesis:
    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 10)
        self.driver = driver

    def stac_social_anamnes(self, test_data):

        # Employment
        employment = self.driver.find_element(By.XPATH,'//*[@placeholder="{}"]'.format(employments)).click()
        sleep(1)
        employment_button = self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div/div[2]/div/div[5]/div/div[2]/div/div/div/div/div/div/div[1]/div[1]/div/div[2]/div/div[2]/li[2]/div/span')
        employment_button.click()

        # Physical limited
        physical_limited = self.driver.find_element(By.XPATH,'//*[@placeholder="{}"]'.format(physical)).click()
        sleep(1)
        physical_limited_button = self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div/div[2]/div/div[5]/div/div[2]/div/div/div/div/div/div/div[1]/div[3]/div/div[2]/div/div[2]/li[4]/div/span')
        physical_limited_button.click()

        # Education
        education_dropdown = self.driver.find_element(By.XPATH,'//*[@placeholder="{}"]'.format(education)).click()
        sleep(1)
        education_button = self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div/div[2]/div/div[5]/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div[2]/div/div[2]/li[1]/div/span')
        education_button.click()

        # Number of sons 
        number_of_sons = self.driver.find_element(By.XPATH,'//*[@placeholder="{}"]'.format(suns)).send_keys(test_number)
        sleep(1)

        # workplace
        workplace = self.driver.find_element(By.XPATH,'//*[@placeholder="{}"]'.format(workplaces)).send_keys(test)
        sleep(1)

        # Additional information
        additional_information = self.driver.find_element(By.XPATH,'//*[@placeholder="{}"]'.format(additional)).send_keys(test)
        sleep(1)

        # Save all info
        save_all_info = self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div/div[2]/div/div[6]/div[2]/button[2]')
        save_all_info.click()
        sleep(1)