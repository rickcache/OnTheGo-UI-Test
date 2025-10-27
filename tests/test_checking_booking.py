import pytest
import pytest_check as check
from pages.page_login import Login
from file_data_loader import DataLoad
import logging 
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.mark.order(7)
@pytest.mark.confirmation
@pytest.mark.parametrize(
    "name, email, password",
    DataLoad().json_load_login("data/data_login.json")
)
def test_confirm_booking(driver, name, email, password):
    login = Login(driver)
    
    logging.info("Directing to the site")
    driver.get("http://127.0.0.1:5000/")
    
    logging.info("Logging into the site")
    login.login(name, email, password)
    
    logging.info("Directing to the booking history page")
    history_page = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[text()='Booking History']"))
    )
    history_page.click()
    
    logging.info("Testing multiple parameters...")

    check.is_true("Japan" in driver.page_source, '"Japan" is present in the page')
    check.is_true("2025-10-29" in driver.page_source, '"2025-10-29" is present in the page')
    check.is_true("International" in driver.page_source, '"International" is present in the page')
    check.is_true("Business" in driver.page_source, '"Business" is present in the page')
    check.is_true("2" in driver.page_source, '"2" is present in the page')
    check.is_true("25500" in driver.page_source, '"25500" is present in the page')
    
    logging.info("All elements are present (or checked with soft assertions)")
