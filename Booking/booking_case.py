from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from Tools.test_data import *

class BookingCase:
    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 10)
        self.driver = driver

    def navigation_pacient_to_booking(self):
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/div/div/div[1]/div[2]/div/div[3]').click()
        sleep(1)
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div[3]/button[1]').click()

    def booking_create_patient(self, test_data):

        # find ID number
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="{}"]'.format(pn0)))).send_keys(num)
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="{}"]'.format(name0)))).send_keys(test)
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="{}"]'.format(lastname0)))).send_keys(test)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[1]/div/div/button'))).click()
        sleep(3)

        # Gender selection
        gender = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="{}"]'.format(gender0))))
        gender.click()
        gender_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div/div[1]/div[1]/div/div[7]/div/div[2]/div/div/li[1]/div/span')))
        gender_option.click()

        # Date of Birth
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="{}"]'.format(birth0)))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="{}"]'.format(birth0)))).send_keys(birth)

        # Address
        Address1 = self.driver.find_element(By.XPATH, '//*[@placeholder="{}"]'.format(address01))
        Address1.click()
        sleep(1)
        Address1 = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/div/div[2]/div/div[2]/li[1]/div/span')
        Address1.click()
        sleep(1)
        Address_repeat = self.driver.find_element(By.XPATH, '//*[@placeholder="{}"]'.format(address02)).send_keys(test)

        # Mobile Number
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="{}"]'.format(mobnumber)))).send_keys(number1)
        sleep(1)
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="{}"]'.format(mobnumber0)))).send_keys(number2)

        # Email
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="{}"]'.format(mail0)))).send_keys(mail)

        # Creat case
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        Creat_case = self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div/div[2]/div/div[2]/div/button').click()

    def navigation_to_calendar(self, test_data):

        # Go to calendar
        element = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[1]/div[3]')
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        sleep(1)

        # Choose doctor
        self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/table/thead/tr[2]/th[1]/div/div/div[1]/div[1]/div/input').send_keys(doctor)
        sleep(2)
        doctor_row = self.driver.find_element(By. XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/table/tbody/tr/td[1]')
        actions.double_click(doctor_row).perform()
        sleep(1)

    def choose_visit_day(self, test_data):
        
        # Choose next day
        actions = ActionChains(self.driver)
        next_day_button = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/button[3]')
        actions.double_click(next_day_button).perform()
        sleep(1)
        next_day_button.click()
        sleep(2)

        # Choose free time
        time_slot = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/span[3]/fieldset')
        time_slot.click()
        visit_book_button = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/button[1]')
        visit_book_button.click()

    def update_visit(self, test_data):

        update_button = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/span[3]/fieldset/div[1]/button[1]')
        update_button.click()
        sleep(1)

        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="{}"]'.format(update_time)))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="{}"]'.format(update_time)))).send_keys(time)
        sleep(1)

        just_click = self.driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/div[1]/div/div[5]')
        just_click.click()
        sleep(1)

        time_choose = self.driver.find_element(By.XPATH, '//*[@placeholder="{}"]'.format(update_time_sec))
        time_choose.click()
        sleep(1)
        choose = self.driver.find_element(By.XPATH,'')


        
    def delete_visit_day(self, test_data):

        visit_delete = self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/span[3]/fieldset/div[1]/button[2]')
        visit_delete.click()
        sleep(1)

        choose_reason = self.driver.find_element(By.XPATH,'')
        