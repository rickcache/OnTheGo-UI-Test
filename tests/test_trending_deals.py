import pytest
from pages.page_trending_deals import Trending_Deals
from pages.page_login import Login
from file_data_loader import DataLoad
import logging

@pytest.mark.order(3)
@pytest.mark.trending_deals
@pytest.mark.parametrize(
    "name, email, password",
    DataLoad().json_load_login("data/data_login.json")    
)

def test_trending_deals(driver, name, email, password):
    login = Login(driver)
    trending =  Trending_Deals(driver)
    
    driver.get("http://127.0.0.1:5000/")
    
    logging.info("Logging in into the site")
    login.login(name, email, password)
    
    logging.info("Testing the Trending deals one by one")
    trending.trending_page()
    
    logging.info("Test Successful")
    
    
    