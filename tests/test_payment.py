import pytest
from pages.page_login import Login
from pages.page_book import Booking
from pages.page_payment import Payment
from file_data_loader import DataLoad
import logging

@pytest.mark.order(6)
@pytest.mark.payment 
@pytest.mark.parametrize(
    "name, email, password",
    DataLoad().json_load_login("data/data_login.json")
)

def test_payment(driver, name, email, password):
    login = Login(driver)
    book = Booking(driver)
    payment = Payment(driver)

    logging.info("Directing to the Website")
    driver.get("http://127.0.0.1:5000/")      
    
    logging.info("Logging into the Website")
    login.login(name, email, password)
    
    logging.info("Filling the booking form")
    book.booking()
    
    logging.info("Filling the Payment form")
    payment.payment()
    
    expected_text = "Payment successful! Booking confirmed."
    
    logging.info("Testing...")
    assert expected_text in driver.page_source
    logging.info("Test Successful")