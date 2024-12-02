from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from Tools.test_data import *
from time import sleep
import logging

class RegisterAmbulatoryCase:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def navigation_register(self):
        self.driver.execute_script("window.scrollTo(0, 0)")
        sleep(3)
        navigation = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[1]/div[3]/div[1]')
        navigation.click()
        sleep(1)
        close_button = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div[3]/button[1]')
        close_button.click()
        sleep(1)
        navigation.click()
        sleep(4)

    def register_case_ambulatory(self):
        add_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mainContainer"]/div/div/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/cd-steps-medical-case/div/div[2]/div[1]/div/div[3]/div[1]/div/button[1]')))
        add_button.click()
        sleep(2)

        service = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cd-dynamic-select-head-208"]/div[2]/table/tbody/tr/td/button')))
        service.click()
        sleep(2)
        
        input = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cd-dynamic-select-body-208"]/div[1]/input')))
        input.send_keys('84845')
        sleep(3)

        choose_service = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cd-dynamic-select-body-208"]/ul/li/span/table/tbody[2]/tr/td[2]')))
        sleep(3)
        actions = ActionChains(self.driver)
        actions.double_click(choose_service).perform()

        choose_doctor = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cd-dynamic-select-head-940"]/div[2]/table/tbody/tr/td/button')))
        sleep(1)
        doctor_name = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cd-dynamic-select-body-312"]/div[1]/input')))
        sleep(3)
        doctor_name.send_keys('კიმოთიძე ლუკა')

        doctor = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cd-dynamic-select-body-312"]/ul')))
        sleep(1)

        save_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/div[3]/div/button[1]')))
        sleep(1)
        pay_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mainContainer"]/div/div/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/cd-steps-medical-case/div/div[2]/div[3]/div[2]/cd-medical-case-subcomponent-groups-footer/div/button[3]')))
        sleep(3)
        pay = self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div[3]/div/div[4]/button')))
        sleep(1)
        pay_accept = self.wait.until(EC.element_to_be_clickable((By.XPATH, 'html/body/div[1]/div/div/div/div/div[2]/div[3]/div/button')))
        sleep(2)
        
