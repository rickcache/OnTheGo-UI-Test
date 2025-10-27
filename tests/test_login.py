import pytest
from pages.page_login import Login
from file_data_loader import DataLoad
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.order(2)
@pytest.mark.login
@pytest.mark.parametrize(
    "name, email, password",
    DataLoad().json_load_login("data/data_login.json")
)

def test_login(driver, name, email, password):
    login = Login(driver)
    
    logging.info("Directing to the site")
    driver.get("http://127.0.0.1:5000/")
    
   
    logging.info("Logging into the site")
    login.login(name, email, password)
    
    WebDriverWait(driver, 10).until(
        EC.url_contains("/dashboard")
    )

    excepted_text = f"Welcome, {name}!"
    
    logging.info("Testing...")
    
    assert excepted_text in driver.page_source
    
    logging.info("Test Successful")
    