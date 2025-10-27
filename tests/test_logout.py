import pytest
from pages.page_login import Login
from file_data_loader import DataLoad
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.mark.logout(9)
@pytest.mark.parametrize(
    "name, email, password",
    DataLoad().json_load_login("data/data_login.json")
)

def test_logout(driver, name, email, password):
    login = Login(driver)
    
    logging.info("Directing to the Website")
    driver.get("http://127.0.0.1:5000/")
    
    logging.info("Logging into the site")
    login.login(name, email, password)
    
    logging.info("Logging out")
    logout = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="navbarNav"]/ul/li[5]/a')))
    logout.click()
    
    logging.info("Testing...")
    assert driver.current_url == "http://127.0.0.1:5000/", "URL mismatch after navigation!"
    logging.info("Test Successful")