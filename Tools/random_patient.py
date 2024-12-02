from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait

class RandomPatients:
    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 10)
        self.driver = driver

    # def navigation_stacpacient_case(self):
    #     stac = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/div/div/div[1]/div[2]/div/div[2]')
    #     stac.click()
    #     self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div[3]/button[1]').click()    

    def choose_random_patient(self, test_data):
        stac = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/div/div/div[1]/div[2]/div/div[2]')
        stac.click()
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div[3]/button[1]').click()
        sleep(3)
        patient = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[2]/div/div[2]/table/tbody/tr[1]/td[3]')
        actions = ActionChains(self.driver)
        sleep(2)
        actions.double_click(patient).perform()
