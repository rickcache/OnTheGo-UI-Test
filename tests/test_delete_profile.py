import pytest
from pages.page_book import Booking
from pages.page_login import Login
from pages.page_payment import Payment
from file_data_loader import DataLoad
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

@pytest.mark.order(12)
@pytest.mark.delete
@pytest.mark.parametrize(
    "name, email, password",
    DataLoad().json_load_login("data/data_delete.json")
)

def test_cancel_booking(driver, name, email, password):
    login = Login(driver)
 
    logging.info("Directing to the Website")
    driver.get("http://127.0.0.1:5000/") 
    
    logging.info("Logging into the site")
    login.login(name, email, password)
    
    logging.info("Directing to the profile page")
    wait = WebDriverWait(driver, 10) 
    profile_page = wait.until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/a[1]'))
    )
    profile_page.click()
    
    logging.info("Clicking the delete profile button")
    delete_profile = wait.until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/form[2]/button'))
    )    
    delete_profile.click()
    
    logging.info("Confirming the alert button")
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = Alert(driver)
    print(alert.text) 
    alert.accept()
    
    logging.info("Testing")   
    expected_text = "Profile and all bookings deleted successfully."
    logging.info("Test Successful")