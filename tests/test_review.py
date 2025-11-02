import pytest
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.page_login import Login
from pages.page_review import Review
from file_data_loader import DataLoad
from selenium.webdriver.common.by import By


@pytest.mark.order(4)
@pytest.mark.review
@pytest.mark.xfail(reason="Invalid js Error")
@pytest.mark.parametrize(
    "name, email, password",
    DataLoad().json_load_login("data/data_login.json")
)
@pytest.mark.parametrize(
    "review_name, review_email, review_text",
    DataLoad().json_load_review("data/data_review.json")
)
def test_review(driver, name, email, password, review_name, review_email, review_text):
    login = Login(driver)
    review = Review(driver)

    logging.info("Opening site...")
    driver.get("http://127.0.0.1:5000/")

    logging.info("Logging in...")
    login.login(name, email, password)

    # ✅ Wait until redirected to dashboard
    WebDriverWait(driver, 10).until(EC.url_contains("/dashboard"))

    # Optional: Zoom out if needed
    driver.execute_script("document.body.style.zoom='80%'")

    logging.info("Dashboard loaded. Filling review form...")
    review.review(review_name, review_email, review_text)

    expected_text = "Thank you for your review!"

    # Wait for the success message to appear
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, "body"), expected_text)
    )

    logging.info("Testing...")
    assert expected_text in driver.page_source

    logging.info("Test Successful")
