import pytest
from pages.page_login import Login
from pages.page_profile_update import Update_Profile
from file_data_loader import DataLoad
import logging

@pytest.mark.order(10)
@pytest.mark.update_profile
@pytest.mark.parametrize(
    "name, email, password",
    DataLoad().json_load_login("data/data_login.json")
)
@pytest.mark.parametrize(
    "updated_name, updated_phone, updated_password, filepath",
    DataLoad().json_load_update("data/data_update.json")
)

def test_update_profile(driver, name, email, password, updated_name, updated_phone, updated_password, filepath):
    login = Login(driver)
    update = Update_Profile(driver)
      
    driver.get("http://127.0.0.1:5000/")
    
    login.login(name, email, password)
    
    update.update_profile(updated_name, updated_phone, updated_password, filepath)
    
    expected_text = "Profile updated successfully!"
    
    assert expected_text in driver.page_source
        
    