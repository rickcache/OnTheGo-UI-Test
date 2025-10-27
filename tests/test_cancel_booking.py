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

@pytest.mark.cancel(9)
@pytest.mark.parametrize(
    "name, email, password",
    DataLoad().json_load_login("data/data_login.json")
)

def test_cancel_booking(driver, name, email, password):
    login = Login(driver)
    book  = Booking(driver)
    payment = Payment(driver)
    
    logging.info("Directing to the Website")
    driver.get("http://127.0.0.1:5000/")
    
    logging.info("Logging into the site")
    login.login(name, email, password)
    
    logging.info("Filling the booking")
    book.booking()
    logging.info("Booking successful")
    
    logging.info("Filling theh payment form")
    payment.payment()
    
    logging.info("Clicking the cancel button")
    canceL_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/table/tbody/tr/td[11]/form/button'))
        )
    canceL_btn.click()
    
    logging.info("Confirming the javascript alert")
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = Alert(driver)
    print(alert.text)  # optional — logs "Are you sure you want to cancel this booking?"
    alert.accept() 
    
    expected_text = "Booking cancelled."
    
    logging.info("Testing")
    assert expected_text in driver.page_source
    logging.info("Test Successful")