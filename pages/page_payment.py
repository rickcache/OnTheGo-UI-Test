from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait,Select

class Payment:
    def __init__(self, driver):
        self.driver = driver
        self.payment_method = (By.XPATH, '/html/body/div[2]/div/div/form/div/select')
        self.paynow  = (By.XPATH, '/html/body/div[2]/div/div/form/button')
        
    def payment(self):
        wait = WebDriverWait(self.driver, 10)
        
        payment_method = Select( wait.until(EC.presence_of_element_located((self.payment_method))))
        payment_method.select_by_visible_text("Debit Card")
        
        payment_btn = wait.until(EC.presence_of_element_located((self.paynow)))
        payment_btn.click()
          