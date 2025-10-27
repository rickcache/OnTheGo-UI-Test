from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class Review:
    def __init__(self, driver):
        self.driver = driver
        self.name_in = (By.CSS_SELECTOR, "input[name='name']")
        self.email_in = (By.CSS_SELECTOR, "input[name='email']")
        self.review_in = (By.CSS_SELECTOR, "textarea[name='comment']")
        self.dropdown_rating = (By.CSS_SELECTOR, "select[name='rating']")  # better than absolute XPath
        self.submit_btn = (By.CSS_SELECTOR, "button[type='submit']")        # better than absolute XPath

    def review(self, review_name, review_email, review_text):
        wait = WebDriverWait(self.driver, 10)

        # Fill Name
        name_input = wait.until(EC.element_to_be_clickable(self.name_in))
        name_input.clear()
        name_input.send_keys(review_name)

        # Fill Email
        email_input = wait.until(EC.element_to_be_clickable(self.email_in))
        email_input.clear()
        email_input.send_keys(review_email)

        # Fill Review
        review_input = wait.until(EC.element_to_be_clickable(self.review_in))
        review_input.clear()
        review_input.send_keys(review_text)

        # Select dropdown value
        dropdown = Select(wait.until(EC.element_to_be_clickable(self.dropdown_rating)))
        dropdown.select_by_value("5")

        # Scroll to submit button (important if offscreen)
        submit = wait.until(EC.element_to_be_clickable(self.submit_btn))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", submit)
        submit.click()
