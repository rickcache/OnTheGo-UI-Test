from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class Register:
    
    def __init__(self, driver):
        self.driver  = driver
        self.intialize_button = (By.XPATH, '//*[@id="bookBtn"]')
        self.signup_page_path = (By.PARTIAL_LINK_TEXT, "Sign up here")
        self.name_in_path     = (By.XPATH, '/html/body/div[2]/div/div/form/div[1]/input')
        self.email_in_path    = (By.XPATH, '/html/body/div[2]/div/div/form/div[2]/input')
        self.password_in_path = (By.XPATH, '/html/body/div[2]/div/div/form/div[3]/input')
        self.phone_in_path    = (By.XPATH, '/html/body/div[2]/div/div/form/div[4]/input')
        self.register_btn     = (By.XPATH, '/html/body/div[2]/div/div/form/div[5]/button')
    
    def register(self, name, email, password, phone):
        wait = WebDriverWait(self.driver, 10)
        
        page_access = wait.until(EC.element_to_be_clickable((self.intialize_button)))
        page_access.click()
        
        signup_path = wait.until(EC.presence_of_element_located((self.signup_page_path)))
        signup_path.click()
        
        name_input = wait.until(EC.presence_of_element_located((self.name_in_path)))
        name_input.clear()
        name_input.send_keys(name)
        
        email_input = wait.until(EC.presence_of_element_located((self.email_in_path)))
        email_input.clear()
        email_input.send_keys(email)
        
        password_input = wait.until(EC.presence_of_element_located((self.password_in_path)))
        password_input.clear()
        password_input.send_keys(password)
        
        phone_input = wait.until(EC.presence_of_element_located((self.phone_in_path)))
        phone_input.clear()
        phone_input.send_keys(phone)
        
        register = wait.until(EC.element_to_be_clickable((self.register_btn)))
        register.click()
        
        