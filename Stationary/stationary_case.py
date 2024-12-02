from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Tools.test_data import *
from time import sleep

class StationaryCase:
    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 10)
        self.driver = driver

    def navigation_pacient_case(self):
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/div/div/div[1]/div[2]/div/div[2]').click()
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div[3]/button[1]').click()

    def stationary_case(self, test_data):
            
        # Use explicit waits instead of sleep
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="{}"]'.format(pn0)))).send_keys(num2)
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="{}"]'.format(name0)))).send_keys(test)
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="{}"]'.format(lastname0)))).send_keys(test)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[1]/div/div[2]/button'))).click()
        sleep(3)

        # Gender selection
        gender = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="{}"]'.format(gender0))))
        gender.click()
        gender_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div/div[1]/div[1]/div[7]/div/div[2]/div/div/li[1]/div/span')))
        gender_option.click()

        # Date of Birth
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="{}"]'.format(birth0)))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="{}"]'.format(birth0)))).send_keys(birth)

        # Address
        Address1 = self.driver.find_element(By.XPATH, '//*[@placeholder="{}"]'.format(address01))
        Address1.click()
        sleep(1)
        Address1 = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div[1]/div[2]/div[1]/div/div[2]/div/div[2]/li[1]/div/span')
        Address1.click()
        sleep(1)
        Address_repeat = self.driver.find_element(By.XPATH, '//*[@placeholder="{}"]'.format(address02)).send_keys(test)
        Address_repeat = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div/div[1]/div[2]/div[3]/div/button').click()

        # Mobile Number
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="{}"]'.format(mobnumber)))).send_keys(number1)
        sleep(1)
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="{}"]'.format(mobnumber0)))).send_keys(number2)

        # Email
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="{}"]'.format(mail0)))).send_keys(mail)

        # Creat case
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        Creat_case = self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div/div[2]/div/div[5]/div[2]/button[2]').click()
