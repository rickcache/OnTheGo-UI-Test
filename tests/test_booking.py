import pytest
from pages.page_login import Login
from pages.page_book import Booking
from file_data_loader import DataLoad
import logging 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.order(5)
@pytest.mark.book
@pytest.mark.parametrize(
    "name, email, password",
    DataLoad().json_load_login("data/data_login.json")
)

def test_book(driver, name, email, password):
    login = Login(driver)
    book = Booking(driver)
    
    logging.info("Directing to the Website")
    driver.get("http://127.0.0.1:5000/")
    
    logging.info("Logging into the site")
    login.login(name, email, password)
    
    logging.info("Filling the booking")
    book.booking()
    logging.info("Booking successful")
    
    WebDriverWait(driver, 10).until(
        EC.url_contains("/payment")
    )

    assert "http://127.0.0.1:5000/payment" in driver.current_url

    