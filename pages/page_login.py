from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login:
    def __init__(self, driver):
        self.driver  = driver
        self.intialize_button = (By.XPATH, '//*[@id="bookBtn"]')
        self.email_in_path = (By.XPATH, '/html/body/form/input[1]')
        self.pass_in_path  = (By.XPATH, '/html/body/form/input[2]')
        self.button_path   = (By.XPATH, '/html/body/form/button')
        
    def login(self, name, email, password,):
        wait = WebDriverWait(self.driver, 10)
        
        login_page = wait.until(EC.element_to_be_clickable((self.intialize_button)))
        login_page.click()
        
        email_input = wait.until(EC.presence_of_element_located((self.email_in_path)))
        email_input.clear()
        email_input.send_keys(email) 
        
        password_input = wait.until(EC.presence_of_element_located((self.pass_in_path)))
        password_input.clear()
        password_input.send_keys(password)
        
        button_click = wait.until(EC.element_to_be_clickable((self.button_path)))
        button_click.click()
           
        
        