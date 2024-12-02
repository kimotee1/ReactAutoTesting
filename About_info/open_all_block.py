from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from Tools.test_data import *
from time import sleep
import logging

class AllBlock:
    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 10)
        self.driver = driver

    def all_block(self, test_data):

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(1)

        # Locate the block element
        attached_files = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div/div[7]/div/div')
        attached_files.click()
        sleep(1)
        attached_files.click()
        sleep(1)

        # About block
        about_file = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div/div[8]/div/div/div[1]')
        about_file.click()
        sleep(1)
        about_file.click()
        sleep(1)

        # Additional block
        additional_block = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div/div[9]/div/div/div[2]')
        additional_block.click()
        sleep(1)
        additional_block.click()
        sleep(1)

        # History block
        history_block = self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div/div[2]/div/div[10]/div/div/div[2]')
        history_block.click()
        sleep(1)
        history_block.click()
        sleep(1)

        # Booking register
        booking_register_block = self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div/div[2]/div/div[11]/div/div/div[2]')
        booking_register_block.click()
        sleep(1)
        booking_register_block.click()
        sleep(1)

        # History result
        history_result_block = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div/div[12]/div/div/div[2]')
        history_result_block.click()
        sleep(1)
        history_result_block.click()
        sleep(1)

        # EHR consent block
        ehr_consent_block = self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div/div[2]/div/div[13]/div/div/div[2]')
        ehr_consent_block.click()
        sleep(1)
        ehr_consent_block.click()
        sleep(1)

    def open_price_list (self, test_data):

        price_list = self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div/div[1]/div[4]')
        price_list.click()
        sleep(1)

        internal_standard = self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div/div[2]/div[1]/form/div/div/div[1]/div/div/div[1]/label[1]/p')
        internal_standard.click()
        sleep(1)

        contractual_tariff = self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div/div[2]/div[1]/form/div/div/div[1]/div/div/div[1]/label[2]/p')
        contractual_tariff.click()
        sleep(1)

        contractual_tariff_choose = self.driver.find_element(By.XPATH, '//*[@placeholder="{}"]'.format(contragent))
        contractual_tariff_choose.click()
        sleep(1)
        contragent_choose = self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div/div[2]/div[1]/form/div/div/div[2]/div/div/div[2]/div/div[2]/li[1]/div/span')
        contragent_choose.click()
        sleep(1)

    def cash_register (self, test_data):

        cash_register = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[1]/div[5]')
        cash_register.click()
        sleep(1)

        terminal_cash = self.driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div[2]/div/div[2]/div[1]/div/a[2]')
        terminal_cash.click()
        sleep(1)

        correction_requested = self.driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[2]/div[1]/div/a[3]')
        correction_requested.click()
        sleep(1)

        encashment = self.driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[2]/div[1]/div/a[4]')
        encashment.click()
        sleep(1)

        fixing_the_problem = self.driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div[2]/div/div[2]/div[1]/div/a[5]')
        fixing_the_problem.click()
        sleep(1)


class AllBlockStac:
    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 10)
        self.driver = driver

    def all_block(self, test_data):

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(1)

        # Locate the block element
        attached_files = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div/div[7]/div/div')
        attached_files.click()
        sleep(1)
        attached_files.click()
        sleep(1)

        # About block
        about_file = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div/div[8]/div/div/div[1]')
        about_file.click()
        sleep(1)
        about_file.click()
        sleep(1)

        # Additional block
        additional_block = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div/div[9]/div/div/div[2]')
        additional_block.click()
        sleep(1)
        additional_block.click()
        sleep(1)

        # History block
        history_block = self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div/div[2]/div/div[10]/div/div/div[2]')
        history_block.click()
        sleep(1)
        history_block.click()
        sleep(1)

        # Booking register
        booking_register_block = self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div/div[2]/div/div[11]/div/div/div[2]')
        booking_register_block.click()
        sleep(1)
        booking_register_block.click()
        sleep(1)

        # History result
        history_result_block = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div/div[12]/div/div/div[2]')
        history_result_block.click()
        sleep(1)
        history_result_block.click()
        sleep(1)

        # EHR consent block
        ehr_consent_block = self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div/div[2]/div/div[13]/div/div/div[2]')
        ehr_consent_block.click()
        sleep(1)
        ehr_consent_block.click()
        sleep(1)

    def open_price_list (self, test_data):

        price_list = self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div/div[1]/div[4]')
        price_list.click()
        sleep(1)

        internal_standard = self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div/div[2]/div[1]/form/div/div/div[1]/div/div/div[1]/label[1]/p')
        internal_standard.click()
        sleep(1)

        contractual_tariff = self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div/div[2]/div[1]/form/div/div/div[1]/div/div/div[1]/label[2]/p')
        contractual_tariff.click()
        sleep(1)

        contractual_tariff_choose = self.driver.find_element(By.XPATH, '//*[@placeholder="{}"]'.format(contragent))
        contractual_tariff_choose.click()
        sleep(1)
        contragent_choose = self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div/div[2]/div[1]/form/div/div/div[2]/div/div/div[2]/div/div[2]/li[1]/div/span')
        contragent_choose.click()
        sleep(1)

    def cash_register (self, test_data):

        cash_register = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[1]/div[5]')
        cash_register.click()
        sleep(1)

        terminal_cash = self.driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div[2]/div/div[2]/div[1]/div/a[2]')
        terminal_cash.click()
        sleep(1)

        correction_requested = self.driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[2]/div[1]/div/a[3]')
        correction_requested.click()
        sleep(1)

        encashment = self.driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[2]/div[1]/div/a[4]')
        encashment.click()
        sleep(1)

        fixing_the_problem = self.driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div[2]/div/div[2]/div[1]/div/a[5]')
        fixing_the_problem.click()
        sleep(1)