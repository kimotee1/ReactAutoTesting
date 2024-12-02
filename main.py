import logging
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from time import sleep

# Configure logging with encoding to handle Georgian characters
logging.basicConfig(
    filename='Log_file/test_log.log',  # Log file name
    level=logging.INFO,        # Set the logging level
    format='%(asctime)s - %(levelname)s - %(message)s',  # Log format
    encoding='utf-8'           # Ensure UTF-8 encoding
)

# Import necessary modules from project
from Ambulatory.ambulatory_case import *
from Ambulatory.Register_case import *
from Tools.test_data import *
from Tools.random_patient import *
from Stationary.stationary_case import *
from Booking.booking_case import *
from About_info.police import *
from About_info.connect_patients import *
from About_info.social_anamnesis import *
from About_info.ehr_doc import *
from About_info.open_all_block import *
from Tools.login_page import *

# Set up the path to your ChromeDriver
chrome_driver_path = r"C:\Users\lkimo\OneDrive\Desktop\Folder For Me\Code\vabaco\React_automation\chromedriver.exe"
service = Service(chrome_driver_path)

# Set Chrome options to keep the browser window open after the script completes
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Initialize the WebDriver with the specified options
driver = webdriver.Chrome(service=service, options=chrome_options)

def login_system(driver):
    """Log in to the system using the provided credentials."""
    try:
        logging.info("შესვლის პროცესის დაწყება")
        login_page = LoginPage(driver)
        login_page.open_page('https://front.evex.ge/registration/login')
        driver.maximize_window()
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_login()
        logging.info("შესვლა წარმატებით შესრულდა")
        sleep(3)
    except Exception as e:
        logging.error(f"შესვლა ვერ მოხერხდა: {e}")

def register_ambulatory_patient(driver):
    """Register a patient in the ambulatory system."""
    try:
        logging.info("ამბულატორიული პაციენტის რეგისტრაციის დაწყება")
        ambulatory_page = AmbulatoryCasePage(driver)
        ambulatory_page.ambulatory_case(test_data)
        logging.info("ამბულატორიული პაციენტი წარმატებით რეგისტრირდა")
        sleep(2)
    except Exception as e:
        logging.error(f"ამბულატორიული პაციენტის რეგისტრაცია ვერ მოხერხდა: {e}")

def enter_ambulatory_police_info(driver):
    """Enter police number and plastic card information for an ambulatory patient."""
    try:
        logging.info("ამბულატორიული პოლისის ინფორმაციის შეყვანის დაწყება")
        amb_info = AmbulatoryCaseInfo(driver)
        amb_info.amb_police_number(test_data)
        amb_info.amb_plastic_card(test_data)
        logging.info("ამბულატორიული პოლისის ინფორმაცია წარმატებით შეყვანილი")
        sleep(2)
    except Exception as e:
        logging.error(f"ამბულატორიული პოლისის ინფორმაციის შეყვანა ვერ მოხერხდა: {e}")

def connect_ambulatory_patient(driver):
    """Connect a patient in the ambulatory system."""
    try:
        logging.info("პაციენტის დაკავშირების დაწყება")
        amb_connect = AmbulatoryConnectPatient(driver)
        amb_connect.amb_connect_patient_button(test_data)
        logging.info("პაციენტი წარმატებით დაკავშირებულია")
        sleep(2)
    except Exception as e:
        logging.error(f"პაციენტის დაკავშირება ვერ მოხერხდა: {e}")

def enter_social_status(driver, is_stationary=False):
    """Enter social anamnesis details for the patient."""
    try:
        logging.info("სოციალური მდგომარეობის შეყვანის დაწყება")
        if is_stationary:
            social_anamnesis = StationarySocialanamnesis(driver)
            social_anamnesis.stac_social_anamnes(test_data)
        else:
            social_anamnesis = AmbulatorySocialanamnesis(driver)
            social_anamnesis.amb_social_anamnes(test_data)
        logging.info("სოციალური მდგომარეობის მონაცემები წარმატებით შეყვანილია")
        sleep(2)
    except Exception as e:
        logging.error(f"სოციალური მდგომარეობის შეყვანა ვერ მოხერხდა: {e}")

def update_ehr_status(driver, is_stationary=False):
    """Update EHR status for the patient."""
    try:
        logging.info("EHR სტატუსის განახლების დაწყება")
        ehr_status = EHRStatusStac(driver) if is_stationary else EHRStatus(driver)
        ehr_status.stac_ehr_status(test_data) if is_stationary else ehr_status.amb_ehr_status(test_data)
        logging.info("EHR სტატუსი წარმატებით განახლებულია")
        sleep(2)
    except Exception as e:
        logging.error(f"EHR სტატუსის განახლება ვერ მოხერხდა: {e}")

def handle_all_blocks(driver, is_stationary=False):
    """Interact with all blocks, including price list and cash register."""
    try:
        logging.info("ყველა ბლოკის მართვის დაწყება")
        blocks = AllBlock(driver)
        blocks.all_block(test_data)
        blocks.open_price_list(test_data)
        blocks.cash_register(test_data)
        logging.info("ყველა ბლოკი წარმატებით დამუშავდა")
        sleep(2)
    except Exception as e:
        logging.error(f"ყველა ბლოკის მართვა ვერ მოხერხდა: {e}")

def choose_random_patient(driver):
    """Select a random patient from the list."""
    try:
        logging.info("შემთხვევითი პაციენტის არჩევის დაწყება")
        random_patient = RandomPatients(driver)
        random_patient.choose_random_patient(test_data)
        logging.info("შემთხვევითი პაციენტი წარმატებით შერჩეული")
    except Exception as e:
        logging.error(f"შემთხვევითი პაციენტის არჩევა ვერ მოხერხდა: {e}")

def register_stationary_patient(driver):
    """Register a patient in the stationary system."""
    try:
        logging.info("სტაციონარული პაციენტის რეგისტრაციის დაწყება")
        stationary_case = StationaryCase(driver)
        stationary_case.navigation_pacient_case()
        stationary_case.stationary_case(test_data)
        logging.info("სტაციონარული პაციენტი წარმატებით რეგისტრირდა")
        sleep(2)
    except Exception as e:
        logging.error(f"სტაციონარული პაციენტის რეგისტრაცია ვერ მოხერხდა: {e}")

def enter_stationary_police_info(driver):
    """Enter police number and plastic card information for a stationary patient."""
    try:
        logging.info("სტაციონარული პოლიციის ინფორმაციის შეყვანის დაწყება")
        stac_police = StationaryCaseInfo(driver)
        stac_police.stac_police_number(test_data)
        stac_police.stac_plastic_card(test_data)
        logging.info("სტაციონარული პოლიციის ინფორმაცია წარმატებით შეყვანილია")
        sleep(2)
    except Exception as e:
        logging.error(f"სტაციონარული პოლიციის ინფორმაციის შეყვანა ვერ მოხერხდა: {e}")

def connect_stationary_patient(driver):
    """Connect a patient in the stationary system."""
    try:
        logging.info("სტაციონარული პაციენტის დაკავშირების დაწყება")
        stac_connect = StationaryConnectPatient(driver)
        stac_connect.stac_connect_patient_button(test_data)
        logging.info("სტაციონარული პაციენტი წარმატებით დაკავშირებულია")
        sleep(2)
    except Exception as e:
        logging.error(f"სტაციონარული პაციენტის დაკავშირება ვერ მოხერხდა: {e}")

def booking_calendar():
    try:
        logging.info("ჯავშნის კალენდრის მართვის დაწყება")
        booking = BookingCase(driver)
        booking.navigation_pacient_to_booking()
        booking.booking_create_patient(test_data)
        booking.navigation_to_calendar(test_data)
        booking.choose_visit_day(test_data)
        booking.update_visit(test_data)
        logging.info("ჯავშნის კალენდარი წარმატებით განახლდა")
        sleep(1)
    except Exception as e:
        logging.error(f"ჯავშნის კალენდრის მართვა ვერ მოხერხდა: {e}")

def register_Case(driver):
    """Register a case in the ambulatory system."""
    try:
        logging.info("Registering a new ambulatory case.")
        register = RegisterAmbulatoryCase(driver)
        register.navigation_register()
        register.register_case_ambulatory()
        logging.info("Ambulatory case registration successful.")
    except Exception as e:
        logging.error(f"Failed to register ambulatory case: {e}")


def run_test_workflow():
    """Run the full workflow of ambulatory and stationary patient registration and updates."""
    try:
        login_system(driver)

        # Ambulatory workflow
        register_ambulatory_patient(driver)
        register_Case(driver)
        enter_ambulatory_police_info(driver)
        connect_ambulatory_patient(driver)
        enter_social_status(driver)
        update_ehr_status(driver)
        handle_all_blocks(driver)

        # Stationary workflow
        register_stationary_patient(driver)
        enter_stationary_police_info(driver)
        connect_stationary_patient(driver)
        enter_social_status(driver, is_stationary=True)
        update_ehr_status(driver, is_stationary=True)
        handle_all_blocks(driver, is_stationary=True)

        # Booking calendar
        booking_calendar()

    except Exception as e:
        logging.error(f"ტესტის სამუშაო ნაკადის შესრულება ვერ მოხერხდა: {e}")

# Execute the test workflow
if __name__ == "__main__":
    run_test_workflow()

# Close the driver at the end if needed, but the browser will stay open
# driver.quit()  # Uncomment this line if you want to close the browser at the end