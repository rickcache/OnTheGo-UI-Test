import pytest
from pages.page_register import Register
from file_data_loader import DataLoad
import logging

@pytest.mark.order(1)
@pytest.mark.register
@pytest.mark.parametrize(
    "name, email, password, phone",
    DataLoad().json_load_register("data/data_register.json")
)


def test_register(driver, name, email, password, phone):
    
    register = Register(driver)
    
    driver.get("http://127.0.0.1:5000/")
    logging.info("Registering The User")
    register.register(name, email, password, phone)
    
    excepted_text = f"Welcome, {name}!"
    logging.info("Testing...")
    
    assert excepted_text in driver.page_source
    logging.info("Test Successful")