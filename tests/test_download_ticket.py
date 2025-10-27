import pytest
from pages.page_login import Login
from pages.page_download_ticket import Download
from file_data_loader import DataLoad
import logging

@pytest.mark.download(8)
@pytest.mark.parametrize(
    "name, email, password",
    DataLoad().json_load_login("data/data_login.json")
)
def test_download_ticket(driver, name, email, password):
    login = Login(driver)
    download = Download(driver)

    driver.get("http://127.0.0.1:5000/")
    login.login(name, email, password)

    logging.info("Attempting to download ticket...")
    download.download()

    assert download.verify_file("ticket"), "Ticket download failed!"
    logging.info("Ticket downloaded successfully.")
